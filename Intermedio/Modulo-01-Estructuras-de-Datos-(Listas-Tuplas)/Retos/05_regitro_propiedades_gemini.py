propiedades = [(1, "Norte", 50000, "Disponible"), (2, "Sur", 75000, "Vendido"), 
                (3, "Oeste", 90000, "Vendido"), (4, "Sur", 65000, "Disponible"),
                (5, "Norte", 1000000, "Disponible"), (6, "Sur", 350000, "Disponible")]

presupuesto = float(input("¿Cual es tu presupuesto maximo?: "))
encontrados = 0

print(f"\nBuscando opciones hasta ${presupuesto}...")

for id, zona, precio, estado in propiedades:
    # Filtro de seguridad: Disponible Y dentro del precio
    if estado == "Disponible" and precio <= presupuesto:
        encontrados += 1
        print(f"[{id}] Zona: {zona} | Precio: ${precio}")

if encontrados == 0:
    print("No hay opciones disponibles que coincidan con tu presupuesto.")
else:
    print(f"\nSe encontraron {encontrados} propiedades para ti.")