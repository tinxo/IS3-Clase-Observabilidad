from flask import Flask, render_template, request
from operaciones import sueldos
import sqlite3
from werkzeug.exceptions import abort

app = Flask(__name__)


@app.route('/')
def index():
    conn = get_db_connection()
    empleados = conn.execute('SELECT * FROM empleados').fetchall()
    conn.close()
    return render_template('index.html', empleados=empleados)


@app.route('/calculate_salary', methods=['POST'])
def calculate_salary():
    apellido = request.form['apellido']
    nombre = request.form['nombre']
    nro_documento = request.form['nro_documento']
    antiguedad = int(request.form['antiguedad'])
    horas_trabajadas = int(request.form['horas_trabajadas'])

    liquidacion = sueldos.Liquidacion()
    sueldo_neto = liquidacion.calcular_sueldo_empleado(horas_trabajadas, antiguedad)

    return render_template('salary_result.html', apellido=apellido, nombre=nombre, nro_documento=nro_documento, antiguedad=antiguedad, horas_trabajadas=horas_trabajadas, sueldo_neto=sueldo_neto)


def get_db_connection():
    conn = sqlite3.Connection('conf/database.db')  # A qué BD se va a conectar
    # Para configurar cómo se devuelven los resultados (diccionarios)
    conn.row_factory = sqlite3.Row
    return conn


# def get_post(post_id):
#     conn = get_db_connection()
#     post = conn.execute('SELECT * FROM posts WHERE id = ?',
#                         (post_id,)).fetchone()
#     conn.close()
#     if post is None:
#         abort(404)
#     return post

if __name__ == '__main__':
    app.run(debug=True)