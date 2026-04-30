biblioteca = ["Correr o Morir", "Los juegos del hambre", "Viernes 13", "Re:zero", "Harry Potter"]

print("#### MENU ####")
print("1. Agregar libro")
print("2. Buscar libro")
opcion = int(input("Ingrese una opcion: "))

if opcion == 1:
    nuevo = input("Nombre del nuevo libro: ").strip()
    # Usamos 'in' para verificar si ya existe (sin necesidad de bucles extra)
    if nuevo in biblioteca:
        print("Error: El libro ya existe en la biblioteca.")
    else:
        biblioteca.append(nuevo)
        print(f"Libro '{nuevo}' agregado con éxito.")

elif opcion == 2:
    busqueda = input("Libro a buscar: ").strip()
    if busqueda in biblioteca:
        # .index() nos dice en qué posición está
        pos = biblioteca.index(busqueda)
        print(f"Libro disponible en la posición {pos}.")
    else:
        print("Libro no disponible.")

# Ordenamos y mostramos la lista final
biblioteca.sort()
print("\nLista actualizada y ordenada:")
print(biblioteca)