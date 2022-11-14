from cmath import log
import psycopg2
from logger_db import logger

conexion = psycopg2.connect(user="postgres", password="admin", host="127.0.0.1",
                            port="5432", database="clase_db")

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "DELETE FROM personas WHERE id IN %s"
            idsPorEliminar = (tuple(input('Dame IDS por eliminar').split(',')))
            valores = (idsPorEliminar,)
            cursor.execute(sentencia, valores)
            registrosAfectados = cursor.rowcount
            logger.debug(f"Registros afectados: {registrosAfectados}")
except Exception as ex:
    logger.error(ex)
finally:
    conexion.close()
