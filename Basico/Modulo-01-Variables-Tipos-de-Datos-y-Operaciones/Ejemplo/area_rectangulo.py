"""
Este script calcula el área de un rectángulo, asegurando que los datos sean legibles y
el código siga la guía de estilo PEP 8.
"""

# Definición de variables con nombres descriptivos (Snake Case)
ancho_rectangulo = 10.5  # Tipo: float
alto_rectangulo = 5      # Tipo: int

# Realizamos una operación aritmética básica
# Python 3 maneja la precisión de forma dinámica
area = ancho_rectangulo * alto_rectangulo

# Uso de f-strings (literales de cadena con formato) para una salida limpia
# Esta es la forma más eficiente y legible de mostrar variables en texto
print(f"El ancho es: {ancho_rectangulo}")
print(f"El alto es: {alto_rectangulo}")
print(f"El área total calculada es: {area}")

# Verificación de tipos (para entender qué sucede internamente)
print(f"La variable 'area' es de tipo: {type(area)}")