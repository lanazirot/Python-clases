from ast import Delete
from Persona import Persona
from CursorDelPool import CursorDelPool
from logger_db import logger as log

class PersonaDAO:

    SELECCIONAR = "SELECT * FROM persona ORDER BY id"
    CREAR = "INSERT INTO persona (nombre,apellido,email,edad) VALUES (%s, %s, %s, %s)"
    ACTUALIZAR = "UPDATE persona SET nombre = %s, apellido = %s, email = %s, edad = %s WHERE id = %s"
    ELIMINAR = "DELETE FROM persona WHERE id = %s"
    ENCONTRAR = "SELECT * FROM persona WHERE id = %s"

    def __init__(self):
        pass

    @classmethod
    def create(cls, persona):
        '''
            Crea una nueva persona e insertala a la base de datos
        '''
        with CursorDelPool() as cursor:
            valores = (persona.Nombre, persona.Apellido,
                       persona.Email, persona.Edad)
            cursor.execute(cls.CREAR, valores)
            log.info(f'{cursor.rowcount} persona fue creada {persona}')
            return cursor.rowcount

    @classmethod
    def delete(cls, persona) -> int:
        '''
            Elimina una persona en base a su ID
        '''
        with CursorDelPool() as cursor:
            valores = (persona.ID,)
            cursor.execute(cls.ELIMINAR, valores)
            log.warn(f'{cursor.rowcount} persona fue eliminada con id {persona.ID}')
            return cursor.rowcount

    @classmethod
    def update(cls, persona) -> int:
        '''
            Actualiza una persona en base a su ID
        '''
        with CursorDelPool() as cursor:
                cursor.execute(cls.ACTUALIZAR, (persona.Nombre,
                               persona.Apellido, persona.Email, persona.Edad, persona.ID))
                log.info(f'{cursor.rowcount} persona fue actualizada con id {persona.ID}')
                return cursor.rowcount

    @classmethod
    def findByID(cls, persona: Persona) -> Persona:
        '''
            Encuentra una persona por su ID
        '''
        find = None
        with CursorDelPool() as cursor:
                cursor.execute(cls.ENCONTRAR, (persona.ID,))
                record = cursor.fetchone()
                find = Persona(record[0],record[1],record[2],record[3],record[4])                
        return find

    @classmethod
    def findAll(cls) -> list:
        '''
            Regresar una lista de personas
        '''
        personas = []
        with CursorDelPool() as cursor:
            sentencia = cls.SELECCIONAR
            cursor.execute(sentencia)
            records = cursor.fetchall()
            for p in records:
                p = Persona(p[0], p[1], p[2], p[3], p[4])
                personas.append(p)
        return personas


if __name__ == '__main__':
    # List personas
    dao = PersonaDAO()
    for p in dao.findAll():
         print(p)
    
    # Find persona
    x = Persona(id=1)
    encontrado = dao.findByID(x)
    print(encontrado)
    
    # Create persona
    new = Persona(nombre='Juan', apellido='Perez', email='juanperez@gmail.com', edad=20)
    dao.create(new)
    
    #Delete persona
    eliminar = Persona(id=3)
    dao.delete(eliminar)