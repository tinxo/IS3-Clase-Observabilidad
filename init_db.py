import sqlite3

connection = sqlite3.connect('conf/database.db')


with open('conf/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO empleados (apellido, nombre, nro_documento, antiguedad) VALUES (?, ?, ?, ?)",
            ('Fulanito', 'Cosme', '45321567', 5)
            )

cur.execute("INSERT INTO empleados (apellido, nombre, nro_documento, antiguedad) VALUES (?, ?, ?, ?)",
            ('Simpson', 'Homero', '24987654', 15)
            )

connection.commit()
connection.close()