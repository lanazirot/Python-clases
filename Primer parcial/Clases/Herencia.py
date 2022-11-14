class Persona:
    def __init__(self, nombre, edad) -> None:
        self._nombre = nombre
        self._edad = edad
    
    @property
    def Nombre(self):
        return self._nombre
    
    @Nombre.setter
    def Nombre(self, nombre):
        self._nombre = nombre
        
    @property
    def Edad(self):
        return self._edad
    
    @Edad.setter
    def Edad(self, edad):
        self._edad = edad

    def __str__(self) -> str:
        return f"{self._nombre} {self._edad} "

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo
    
    @property
    def Sueldo(self):
        return self._sueldo
    @Sueldo.setter
    def Sueldo(self, sueldo):
        self._sueldo = sueldo
    
    def __str__(self) -> str:
        return f"{super().__str__()} {self.Sueldo}"
    
employee =  Empleado('Juan', 20, 500)
print(employee)