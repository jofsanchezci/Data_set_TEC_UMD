import csv
import sqlite3
conn = sqlite3.connect('mi_base_de_datos.db')
with open('datos.csv', 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
cursor = conn.cursor()
cursor.execute('CREATE TABLE datos (id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER)')

for fila in lector_csv:
    cursor.execute('INSERT INTO datos (id, nombre, edad) VALUES (?, ?, ?)', fila)
conn.commit()


