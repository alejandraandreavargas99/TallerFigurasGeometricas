class FiguraGeometrica:
    """Clase base para figuras geométricas"""

    def __init__(self, ancho, alto):
        self._ancho = None
        self._alto = None
        self.ancho = ancho
        self.alto = alto

    @property
    def ancho(self):
        """Obtener el ancho"""
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        """Establecer el ancho con validación"""
        if valor <= 0:
            raise ValueError("El ancho debe ser mayor que 0")
        self._ancho = valor

    @property
    def alto(self):
        """Obtener el alto"""
        return self._alto

    @alto.setter
    def alto(self, valor):
        """Establecer el alto con validación"""
        if valor <= 0:
            raise ValueError("El alto debe ser mayor que 0")
        self._alto = valor

    def area(self):
        """Calcular el área"""
        return self._ancho * self._alto

    def perimetro(self):
        """Calcular el perímetro (no implementado en clase base)"""
        pass

    def __str__(self):
        """Representación en string de la figura"""
        return f"Figura Geométrica: ancho={self._ancho}, alto={self._alto}"