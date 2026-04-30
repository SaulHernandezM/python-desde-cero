"""
Reto: La Calculadora de Áreas.
    Crea una función llamada area_rectangulo que reciba base y altura. Debe retornar el resultado.
    Crea otra función llamada es_area_grande que reciba un número. Si el área es mayor a 50, debe 
    retornar True, de lo contrario False.
    Misión: Pide al usuario la base y altura, usa la primera función para sacar el área y luego pasa 
    ese resultado a la segunda función para decirle al usuario si su rectángulo es "Grande" o "Pequeño".
"""

def area_rectangulo(base, altura):
    area = base * altura
    return area

def es_area_grande(area):
    if area > 50:
        return True
    else:
        return False
    
print("#### Calcular Area de un Rectangulo ####")  
base = float(input("Base: "))
altura = float(input("Altura: "))
area = area_rectangulo()

resultado_area = area_rectangulo(base, altura)
rectangulo_grande = es_area_grande(area)

print(f"Area: {resultado_area}.")
print(f"El rectangulo es grande: {rectangulo_grande}.")
    




