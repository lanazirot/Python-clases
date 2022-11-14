from FiguraGeometrica import FiguraGeometrica 
from Color import Color

# Manda a llamar el constructor de la primera clase, es decir FG
# Pero los podemos utilizar con las clases directamente
class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, color, lado) -> None:
        FiguraGeometrica.__init__(self,lado, lado)
        Color.__init__(self, color)
    
    def Area(self):
        return self.alto * self.ancho