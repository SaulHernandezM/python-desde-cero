"""
Reto: Registro de Propiedades (Tuplas)
Este reto simula una base de datos de una inmobiliaria.
    Crea una lista de tuplas llamada propiedades. Cada tupla será: (id, zona, precio, estado).
    Ejemplo: [(1, "Norte", 50000, "Disponible"), (2, "Sur", 75000, "Vendido")].
    Requerimientos:
        El sistema debe pedir al usuario un presupuesto máximo.
        Debe recorrer la lista y mostrar solo las propiedades que estén "Disponible" 
        Y cuyo precio sea menor o igual al presupuesto del usuario.
        Al final, debe mostrar cuántas opciones se encontraron en total.
"""

propiedades = [(1, "Norte", 50000, "Disponible"), (2, "Sur", 75000, "Vendido"), 
               (3, "Oeste", 90000, "Vendido"), (4, "Sur", 65000, "Disponible"),
               (5, "Norte", 1000000, "Disponible"), (6, "Sur", 350000, "Disponible")]

presupuesto = float(input("Presupuesto: "))

for id, zona, precio, estado in propiedades:
    if "Disponible" in estado and precio <= presupuesto:
        print(f"Propiedades disponibles en base a su presupuesto de ${presupuesto}: {len(propiedades)}")
        break
    else:
        print("No hay opciones disponibles para su presupuesto.")    
        break

