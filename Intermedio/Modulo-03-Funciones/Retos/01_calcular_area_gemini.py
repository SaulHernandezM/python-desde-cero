def area_rectangulo(base, altura):
    area = base * altura
    return area

def es_area_grande(area):
    if area > 50:
        return True
    else:
        return False

base = float(input("Base: "))
altura = float(input("Altura: "))

# Guardamos el resultado en una variable
calculo_area = area_rectangulo(base, altura) 

# Usamos ESE resultado para la segunda función
es_grande = es_area_grande(calculo_area)

print(f"Area: {calculo_area}")
print(f"¿Es un área grande?: {es_grande}")


"""
Tu lógica dentro de es_area_grande es impecable. Un pequeño truco de profesional: cuando 
una condición solo devuelve True o False, puedes simplificarla así:
def es_area_grande(area):
    return area > 50  # Esto ya devuelve True o False por sí solo
"""