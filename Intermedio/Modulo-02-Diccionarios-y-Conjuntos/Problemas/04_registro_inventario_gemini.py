stock = {"camisas": 10, "pantalones": 5, "zapatos": 8}

nombre = input("Nombre Producto: ").lower()
cantidad_nueva = int(input("¿Cuántas unidades llegaron?: "))

if nombre in stock:
    # Actualizamos el valor directamente en el diccionario
    stock[nombre] += cantidad_nueva
    print(f"Stock actualizado de {nombre}.")
else:
    # Creamos el registro nuevo
    stock[nombre] = cantidad_nueva
    print(f"Nuevo producto {nombre} registrado.")

print("\n--- INVENTARIO FINAL ---")
# nombre y cant reciben los datos directamente de .items()
for nombre, cant in stock.items():
    print(f"Producto: {nombre.capitalize()} | Cantidad: {cant}")