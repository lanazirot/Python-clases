from logger_db import logger as log
from Conexion import Conexion

class CursorDelPool:
    def __init__(self) -> None:
        self.conexion = None
        self.cursor = None
    
    def __enter__(self):
        log.debug('Inicio metodo with')
        self.conexion = Conexion.ObtenerConexionPool()
        self.cursor = self.conexion.cursor()
        return self.cursor
    
    def __exit__(self, tipo_excepcion, valor_excepcion, detalleExcepcion):
        log.debug('Se ejecuta exit')
        if valor_excepcion:
            log.error(tipo_excepcion, valor_excepcion, detalleExcepcion)
            self.conexion.rollback()
        else:
            self.conexion.commit()
        self.cursor.close()
        Conexion.LiberarConexion(self.conexion)
    
if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug('Bloque with')
        cursor.execute("SELECT * FROM Persona")
        log.debug(cursor.fetchall())