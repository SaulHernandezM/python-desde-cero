"""
Reto: El Sistema de Descuentos Inteligente.
Una tienda ofrece descuentos según el monto de la compra y si el cliente tiene una membresía:
    Si la compra es mayor a $1000 y tiene membresía: 20% de descuento.
    Si la compra es mayor a $1000 pero NO tiene membresía: 10% de descuento.
    Si la compra es entre $500 y $1000 (inclusive): 5% de descuento (tenga o no membresía).
    Si es menor a $500: No hay descuento.
Objetivo: El programa debe pedir el monto y si es socio (True/False), y mostrar: Monto original, Descuento aplicado y Total a pagar.
"""

print("### Sistema de descuento ###")

# Variable que guarda el monto de la compra y si el cliente tienen una membresia
compra = float(input("Ingrese el monto de la compra: "))
membresia_tienda = input("Usted tiene una membresia activa?, responda solo con Si/No: ")

# Verificar si el cliente tiene membresia activa
if membresia_tienda == "SI" or "Si" or "si" or "s" or "S":
    membresia_tienda == True
elif membresia_tienda == "NO" or "No" or "no" or "n" or "N":
    membresia_tienda == False
else:
    print("¡ERROR! Ingrese solo Si o No")

# Calculo descuento
descuento_20 = compra * 0.20
descuento_10 = compra * 0.10
descuento_5 = compra * 0.05

# Resta del descuento al total de compra
total_compra_20 = compra - descuento_20
total_compra_10 = compra - descuento_10
total_compra_5 = compra - descuento_5

# Aplicar descuento
if compra > 1000 and membresia_tienda == True:
    print(f"Su compra es de {compra}")
    print(f"Cuenta con una membresia activa, por lo cual se aplica un descuento del 20% que equivale a {descuento_20} pesos del total de su compra")
    print(f"El total a pagar por su compra es de {total_compra_20}")
elif compra > 1000:
    print(f"Su compra es de {compra}")
    print(f"No cuenta con una membresia activa, por lo cual se aplica un descuento del 10% que equivale a {descuento_10} pesos del total de su compra")
    print(f"El total a pagar por su compra es de {total_compra_10}")
elif compra > 500:
    print(f"Su compra es de {compra}")
    print(f"Su compra es mayor a 500 pesos pero no supera los 1000 pesos, por lo cual se aplica un descuento del 5% que equivale a {descuento_5} pesos del total de su compra")
    print(f"El total a pagar por su compra es de {total_compra_5}")
else:
    print(f"Su compra es de {compra}")
    print(f"Su compra no supera los 500 pesos, por lo cual no se aplica un descuento al total de su compra")
    print(f"El total a pagar por su compra es de {compra}")