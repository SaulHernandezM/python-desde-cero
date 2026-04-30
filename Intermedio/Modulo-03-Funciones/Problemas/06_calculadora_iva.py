"""
Problema: La Calculadora de IVA (Parámetros por Defecto)
A veces queremos que una función tenga un valor "de fábrica".
    Crea una función llamada calcular_total_iva(precio, impuesto = 16).
        El parámetro impuesto debe tener el valor 16 por defecto.
        La función debe retornar el precio final con el impuesto aplicado.
    Misión: Pide al usuario el precio de un producto.
        Llama a la función solo con el precio (para que use el 16%).
        Luego, llama a la función con el precio y un impuesto diferente (ej: 8%) para ver cómo cambia.
"""

def calcular_total_iva(precio, impuesto = 16):
    return precio + (precio * (impuesto/100))
    

print("#### Calculadora IVA ####")
precio_producto = float(input("Precio producto: "))

precio_iva = calcular_total_iva(precio_producto)
print(f"Precio con IVA (16%): {precio_iva:.2f}")

impuesto = 8
precio_iva = calcular_total_iva(precio_producto, impuesto)
print(f"Precio con IVA (8%): {precio_iva:.2f}")