from figura_geometrica import FiguraGeometrica


class Rectangulo(FiguraGeometrica):
    """Clase que representa un rectángulo"""

    def area(self):
        """Calcular el área del rectángulo"""
        return self._ancho * self._alto

    def perimetro(self):
        """Calcular el perímetro del rectángulo"""
        return 2 * (self._ancho + self._alto)

    def __str__(self):
        """Representación en string del rectángulo"""
        return f"Rectángulo: ancho={self._ancho}, alto={self._alto}, área={self.area()}, perímetro={self.perimetro()}"