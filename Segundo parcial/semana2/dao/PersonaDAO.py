from Conexion import Conexion
from Persona import Persona


class PersonaDAO:

    CONSULTAS = {
        'SELECCIONAR': "SELECT * FROM persona ORDER BY id_persona",
        'CREAR': "INSERT INTO personas(nombre,apellido,email,edad) VALUES (%s, %s, %s, %s)",
        "ACTUALIZAR": "UPDATE persona SET nombre = %s, apellido = %s, email = %s, edad = %s WHERE id = %s",
        "ELIMINAR": "DELETE FROM persona WHERE id = %s",
        "ENCONTRAR": "SELECT * FROM persona WHERE id = %s"
    }

    def __init__(self):
        pass

    @classmethod
    def create(cls, persona):
        pass

    @classmethod
    def delete(cls, persona) -> None:
        pass

    @classmethod
    def update(cls, persona) -> None:
        pass

    @classmethod
    def findByID(cls, id: int):
        persona = None
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                sentencia =  cls.CONSULTAS['']
                cursor.execute(sentencia, (id,))
                record = cursor.fetchone()
                persona = Persona(record[0],record[1],record[2],record[3],record[4])                
        return persona

    @classmethod
    def findAll(cls) -> list:
        personas = []
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                sentencia = cls.CONSULTAS['SELECCIONAR']
                cursor.execute(sentencia)
                records = cursor.fetchall()
                for p in records:
                    p = Persona(p[0], p[1], p[2], p[3], p[4])
                    personas.append(p)
        return personas

