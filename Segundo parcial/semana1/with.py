from cmath import log
import psycopg2
from logger_db import logger

conexion = psycopg2.connect(user="postgres", password="admin", host="127.0.0.1",
                            port="5432", database="clase_db")

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "INSERT INTO personas(nombre,apellido,email) VALUES (%s, %s, %s)"
            valores = (('Humberto', 'Perez', 'hperez@gmail.com'),
                       ('Jesus', 'Ortiz', 'jsusortiz@gmail.com'))
            cursor.executemany(sentencia, valores)
            registrosInsertados = cursor.rowcount
            logger.debug(f"Registros insertados: {registrosInsertados}")
except Exception as ex:
    logger.error(ex)
finally:
    conexion.close()
