"""
Reto: El Sistema de Biblioteca (Listas)
Este reto simula un sistema real de gestión de inventario.
    Crea una lista llamada biblioteca que contenga 5 títulos de libros 
    (pueden ser los que quieras).
    Requerimientos del Sistema:
        El usuario debe poder ingresar un nuevo libro, pero SOLO si el libro no 
        existe ya en la lista (evita duplicados).
        El usuario debe poder buscar un libro. Si existe, muestra: "Libro disponible 
        en la posición [índice]".
        El sistema debe mostrar la lista de libros ordenada alfabéticamente antes de cerrar.
"""

biblioteca = ["Correr o Morir", "Los juegos del hambre", "Viernes 13", "Re:zero", "Harry Potter"]
libro = biblioteca
print("#### MENU ####")
print("1. Agregar libro.")
print("2. Buscar libro.")
opcion = int(input("Ingrese una opcion: "))

while opcion == 1:
    nuevo_libro = input("Ingrese un libro: ")
    
    for nuevo_libro in biblioteca:
        if nuevo_libro == biblioteca:
            print("Libro ya disponible en bibilioteca.")
        else:
            print(f"Libro {nuevo_libro} agregado a la biblioteca.")
            biblioteca.append(nuevo_libro)
            break
    break

while opcion == 2:
    buscar_libro = input("Ingrese el libro a buscar: ")
    
    for buscar_libro in biblioteca:
        if buscar_libro == libro:
            print(f"Libro {buscar_libro} disponible en la posicion {biblioteca[buscar_libro]}.")
            break
        else:
            print("Libro no disponible.")
            break
    break       

print(biblioteca.sort)
   
    



    
    

    


