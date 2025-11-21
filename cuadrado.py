from figura_geometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica):
    """Clase que representa un cuadrado"""

    def __init__(self, lado):
        """Constructor que recibe un solo parámetro: lado"""
        super().__init__(lado, lado)

    def area(self):
        """Calcular el área del cuadrado"""
        return self._ancho ** 2

    def perimetro(self):
        """Calcular el perímetro del cuadrado"""
        return 4 * self._ancho

    def __str__(self):
        """Representación en string del cuadrado"""
        return f"Cuadrado: lado={self._ancho}, área={self.area()}, perímetro={self.perimetro()}"