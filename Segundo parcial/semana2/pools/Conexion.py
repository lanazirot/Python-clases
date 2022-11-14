from psycopg2 import pool
from logger_db import logger as log


class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'

    _conexion = None
    _cursor = None

    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def ObtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON, cls._MAX_CON, host=cls._HOST, user=cls._USERNAME,
                    password=cls._PASSWORD, port=cls._DB_PORT, database=cls._DATABASE)
                log.debug(f'Creacion del pool {cls._pool}')
                return cls._pool
            except:
                log.error(f'Error en la conexion del pool {cls._pool}')
        else:
            return cls._pool

    @classmethod
    def ObtenerConexionPool(cls):
        try:
            conexion = cls.ObtenerPool().getconn()
            log.info(f'Conexion obtenida: {conexion}')
            return conexion
        except Exception as e:
            log.error(f'Error al obtener el pool: {e}')
        return conexion

    @classmethod
    def LiberarConexion(cls, conexion):
        cls.ObtenerPool().putconn(conexion)
        log.info(f'Conexion regresada: {conexion}')

    @classmethod
    def CerrarConexiones(cls):
        cls.ObtenerPool().closeall()
        log.warn('Conexiones cerradas')


if __name__ == '__main__':
    conexion1 = Conexion.ObtenerConexionPool()
    conexion2 = Conexion.ObtenerConexionPool()
    conexion3 = Conexion.ObtenerConexionPool()
    conexion4 = Conexion.ObtenerConexionPool()
    conexion5 = Conexion.ObtenerConexionPool()
    conexion6 = Conexion.ObtenerConexionPool()
    conexion7 = Conexion.ObtenerConexionPool()
    conexion8 = Conexion.ObtenerConexionPool()
