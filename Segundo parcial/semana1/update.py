from cmath import log
import psycopg2
from logger_db import logger

conexion = psycopg2.connect(user="postgres", password="admin", host="127.0.0.1",
                            port="5432", database="clase_db")

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "UPDATE personas SET nombre = %s WHERE id = %s"
            id = input('ID por actualizar: ')
            nombre = input('Nuevo nombre: ')
            valores = (nombre, id)
            cursor.execute(sentencia, valores)
            
            registrosActualizados = cursor.rowcount
            logger.debug(f"Registros insertados: {registrosActualizados}")
except Exception as ex:
    logger.error(ex)
finally:
    conexion.close()
