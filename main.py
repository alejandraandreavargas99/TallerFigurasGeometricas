from cuadrado import Cuadrado
from rectangulo import Rectangulo


def sumar_areas(figuras):
    """Suma el área de todas las figuras"""
    total = 0
    for figura in figuras:
        total += figura.area()
    return total


def sumar_perimetros(figuras):
    """Suma el perímetro de todas las figuras"""
    total = 0
    for figura in figuras:
        total += figura.perimetro()
    return total


# Programa principal
if __name__ == "__main__":
    print("=" * 60)
    print("TALLER EN CLASES - FIGURAS GEOMÉTRICAS")
    print("=" * 60)

    # Crear dos cuadrados
    print("\n--- CREANDO CUADRADOS ---")
    cuadrado1 = Cuadrado(5)
    print(f"Cuadrado 1: {cuadrado1}")

    cuadrado2 = Cuadrado(8)
    print(f"Cuadrado 2: {cuadrado2}")

    # Crear dos rectángulos
    print("\n--- CREANDO RECTÁNGULOS ---")
    rectangulo1 = Rectangulo(4, 6)
    print(f"Rectángulo 1: {rectangulo1}")

    rectangulo2 = Rectangulo(3, 9)
    print(f"Rectángulo 2: {rectangulo2}")

    # Demostrar encapsulamiento con valores válidos
    print("\n--- MODIFICANDO VALORES (VÁLIDOS) ---")
    cuadrado1.ancho = 7
    print(f"Cuadrado 1 modificado: {cuadrado1}")

    rectangulo1.ancho = 10
    rectangulo1.alto = 5
    print(f"Rectángulo 1 modificado: {rectangulo1}")

    # Demostrar validación con valores inválidos
    print("\n--- INTENTANDO VALORES INVÁLIDOS (VALIDACIÓN) ---")
    try:
        cuadrado2.ancho = -3
    except ValueError as e:
        print(f"Error al asignar valor negativo: {e}")

    try:
        rectangulo2.alto = 0
    except ValueError as e:
        print(f"Error al asignar valor cero: {e}")

    # Crear lista de figuras
    figuras = [cuadrado1, cuadrado2, rectangulo1, rectangulo2]

    # Mostrar áreas y perímetros individuales
    print("\n--- ÁREAS Y PERÍMETROS INDIVIDUALES ---")
    for i, figura in enumerate(figuras, 1):
        print(f"Figura {i}: Área = {figura.area()}, Perímetro = {figura.perimetro()}")

    # Calcular sumas totales
    print("\n--- TOTALES ---")
    total_areas = sumar_areas(figuras)
    total_perimetros = sumar_perimetros(figuras)

    print(f"Suma total de áreas: {total_areas}")
    print(f"Suma total de perímetros: {total_perimetros}")

    print("\n" + "=" * 60)