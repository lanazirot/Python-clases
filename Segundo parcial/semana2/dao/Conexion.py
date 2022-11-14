import psycopg2 as db
from psycopg2 import pool
import sys
from logger_db import logger as log


class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'

    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = db.connect(host=cls._HOST,
                                           user=cls._USERNAME, port=cls._DB_PORT,
                                           password=cls._PASSWORD,
                                           database=cls._DATABASE)
                log.info(cls._conexion)
                return cls._conexion
            except Exception as ex:
                log.error(ex)
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.info(cls._cursor)
                return cls._cursor
            except Exception as ex:
                log.error(ex)
        else:
            return cls._cursor


if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()
