"""
Reto: Crea un programa que permita ingresar precios de productos uno por uno.
    El programa debe seguir pidiendo precios hasta que el usuario escriba el número 0.
    Al final, debe mostrar:
        El total de la cuenta.
        Cuántos productos se compraron.
        El precio promedio por producto.
"""

while True:
    producto = float(input("Ingrese el precio de un producto: "))
    #cuenta += cuenta
    detener = input("¿Desea ingresar el precio de otro producto (S/N)?: ").strip().lower() in ["si", "s"]
    
    if detener != "si" or detener != "s":
        break
    
print(f"El total de su cuenta es de {producto}.")
#print(f"El total de productos comprados es de {cuenta}.")
#print(f"El precio promedio del producto es de {producto / cuenta}.")

