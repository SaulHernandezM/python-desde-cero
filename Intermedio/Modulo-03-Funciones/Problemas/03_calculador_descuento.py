"""
Problema: El Calculador de Descuento
Vamos a practicar funciones que reciben más de un dato y toman decisiones.
    Crea una función llamada aplicar_descuento que reciba el precio_original y el porcentaje_descuento. 
    Debe retornar el precio final.
    Crea otra función llamada es_oferta_especial que reciba el precio final. Si es menor a $100, retorna 
    el texto "¡Gran Oferta!", si no, retorna "Precio regular".
    Flujo: Pide el precio y el descuento al usuario, calcula el precio final con la primera función y usa 
    ese resultado para imprimir si es una oferta especial o no.
"""

def aplicar_descuento(precio_original, porcentaje_descuento):
    return precio_original - (precio_original * (porcentaje_descuento/100))

def es_oferta_especial(precio_final):
    if precio_final < 100:
        return "¡Gran Oferta!"
    else:
        return "Precio regular"
    
    
print("#### Calculador de Descuento ####")    
precio = float(input("Precio: "))
descuento = float(input("Descuento: "))

calculo_descuento = aplicar_descuento(precio, descuento)

oferta_especial = es_oferta_especial(calculo_descuento)

print(f"Precio final: {calculo_descuento:.2f}.")
print(f"Oferta especial?: {oferta_especial}.")






