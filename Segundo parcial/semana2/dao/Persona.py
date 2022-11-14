class Persona:
    def __init__(self, id=None, nombre=None, apellido=None, email=None, edad=None):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return f"{self.id} {self.nombre} {self.apellido} {self.email} {self.edad}"

    @property
    def Nombre(self):
        return self.nombre

    @property
    def Apellido(self):
        return self.apellido

    @property
    def Email(self):
        return self.email

    @property
    def Edad(self):
        return self.edad


