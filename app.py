from flask import Flask, render_template, request
from operaciones.sueldos import Liquidacion
import sqlite3
from werkzeug.exceptions import abort
import sqlalchemy
import os
from pathlib import Path

import dotenv


app = Flask(__name__)


@app.route('/')
def index():
    conn = get_db_connection()
    query = 'SELECT * FROM empleados'
    conn.connect()
    results = conn.execute(query).fetchall()
    conn.close()
    return render_template('index.html', empleados=results)


@app.route('/calculate_salary', methods=['POST'])
def calculate_salary():
    apellido = request.form['apellido']
    nombre = request.form['nombre']
    nro_documento = request.form['nro_documento']
    antiguedad = int(request.form['antiguedad'])
    horas_trabajadas = int(request.form['horas_trabajadas'])

    liquidacion = Liquidacion()
    sueldo_neto = liquidacion.calcular_sueldo_empleado(horas_trabajadas, antiguedad)

    return render_template('salary_result.html', apellido=apellido, nombre=nombre, nro_documento=nro_documento, antiguedad=antiguedad, horas_trabajadas=horas_trabajadas, sueldo_neto=sueldo_neto)

def init_db():
    conn = get_db_connection()
    query = """
        DROP TABLE IF EXISTS empleados;

        CREATE TABLE empleados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            apellido TEXT NOT NULL,
            nombre TEXT NOT NULL,
            nro_documento TEXT NOT NULL,
            antiguedad INTEGER NOT NULL
        );
    """
    conn.connect()
    conn.execute(query)
    conn.close()

def get_db_connection(): 
    host = os.environ['DB_HOST']
    user = os.environ['DB_USER']
    password = os.environ['DB_PASS']
    database = os.environ['DB_NAME']

    db_URI = 'postgresql+psycopg2://'+ user +':'+ password +'@'+ host +'/'+database
    db = sqlalchemy.create_engine(db_URI, echo=False)
    return db


if __name__ == '__main__':
    # Se cargan las variables de entorno definidas
    dotenv_file = "conf/.env"
    if os.path.isfile(dotenv_file):
        dotenv.load_dotenv(dotenv_file)
    init_db()
    app.run(debug=True)