"""
Reto: El Club de Lectura (Diccionarios + Sets)
Aquí vamos a usar un diccionario para guardar qué géneros de libros le gustan a cada persona.
    Crea un diccionario llamado preferencias. Las llaves son nombres de personas y los valores 
    son conjuntos (sets) de géneros.
    Ejemplo:
    preferencias = {
    "Juan": {"terror", "sci-fi", "drama"},
    "Maria": {"drama", "romance", "historia"}
    }
Misión:
        El programa debe comparar los gustos de Juan y Maria.
        Debe mostrar qué géneros tienen en común (intersección).
        Debe mostrar qué géneros le gustan a Juan que Maria no conoce (diferencia).
        Extra: Agrega un nuevo género al conjunto de Maria usando el método .add().
"""

preferencias = {
    "Juan": {"terror", "sci-fi", "drama"}, "Maria": {"drama", "romance", "historia"},
    "Pepe": {"misterio", "sci-fi", "drama"}, "Carlos": {"drama", "terror", "historia"}, 
    "Pedro": {"drama", "misterio", "historia"}, "Saul": {"drama", "terror", "historia"}
    }


print("#### Comparacion de gustos ####")
comparacion_uno = input("Persona 1: ")
comparacion_dos = input("Persona 2: ")

generos_comun = preferencias[comparacion_uno].intersection(preferencias[comparacion_dos])
generos_diferencia = preferencias[comparacion_uno].difference(preferencias[comparacion_dos])

print(f"Los generos en comun de {comparacion_uno} y {comparacion_dos} son: {generos_comun}")
print(f"Los generos que le gustan a {comparacion_uno} que a {comparacion_dos} son: {generos_diferencia}")

nuevo_genero = input(f"Agregar nuevo genero a {comparacion_dos}: ")

preferencias[comparacion_dos].add(nuevo_genero)
print(preferencias[comparacion_dos])



"""
Siempre es bueno validar con un if comparacion_uno in preferencias and comparacion_dos in preferencias: 
antes de operar.
"""