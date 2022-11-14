from sys import intern
from typing import overload


class Figura:
    def __init__(self, ancho: float, largo: float) -> None:
        self._ancho = ancho
        self._largo = largo

    def calcularPerimetro(self) -> float:
        return self._ancho * self._largo;

class Rectangulo:
    """
        Una clase rectangulo
    """
    def __init__(self, ancho: float, largo: float) -> None:
        """
            Inicializa un objeto Rectangulo con ancho y largo
        """
        self._ancho = ancho
        self._largo = largo
        
    @property
    def Ancho(self) -> float:
        return self._ancho
    
    @Ancho.setter
    def Ancho(self, ancho):
        self._ancho = ancho
    
    @property
    def Largo(self) -> float:
        return self._largo
    
    @Largo.setter
    def Largo(self, largo):
        self._largo = largo
    
    def calcularArea(self) -> float:
        """
            Calcula el area multiplicando el ancho por el largo
        """
        return self._ancho * self._largo
    
    def Perimetro(self) -> float:
        """
            Calcula el perimetro del rectangulo
        """
        return 2 * (self._ancho * self._largo)


class Cuadrado(Figura):
    pass