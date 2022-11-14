import psycopg2
from logger_db import logger

conexion = psycopg2.connect(user="postgres", password="admin", host="127.0.0.1",
                            port="5432", database="clase_db")


try:
    conexion.autocommit = False
    cursor = conexion.cursor()

    # Sentencia insert
    sentencia = "INSERT INTO personas(nombre,apellido,email) VALUES (%s, %s, %s)"
    valores = ('Juan', 'Perez', 'jperez@gmail.com')

    # Ejecuta la sentencia
    cursor.execute(sentencia, valores)
    logger.debug('Sentencia insert')
    # Sentencia update
    sentencia = "UPDATE personas set nombre=%s, apellido=%s, email=%s WHERE id = %s"
    valores = ('Nuevo nombre', 'Super apellido', 'email@gmail.com', 1)
    logger.debug('Sentencia update')

    cursor.execute(sentencia, valores)


    conexion.commit()
    logger.info(f'Cambios guardados con {cursor.rowcount} rows afectados')
except Exception as ex:
    conexion.rollback()
    logger.error(f'Hubo un error en la transaccion {ex}')
finally:
    conexion.close()
    logger.debug('Se cierra la conexion')
