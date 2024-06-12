from flask import Flask, render_template
import sqlite3
from werkzeug.exceptions import abort

app = Flask(__name__)


@app.route('/')
def index():
    conn = get_db_connection()
    empleados = conn.execute('SELECT * FROM empleados').fetchall()
    conn.close()
    return render_template('index.html', empleados=empleados)


# @app.route('/<int:post_id>')
# def post(post_id):
#     post = get_post(post_id)
#     return render_template('post.html', post=post)


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