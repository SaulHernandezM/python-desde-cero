"""
Problema: El Ranking de Jugadores (Ordenamiento y Slicing)
En Python, podemos ordenar listas fácilmente. Investiga el método .sort().
    Crea una lista vacía llamada puntajes.
    Usa un bucle para pedir al usuario 6 puntajes de un videojuego.
    Lógica:
        Una vez tengas los 6 puntajes, ordénalos de mayor a menor (Pista: usa .sort(reverse=True)).
        Muestra el "Top 3" de los mejores puntajes (Investiga el Slicing: lista[0:3]).
        Muestra el puntaje más bajo de la lista usando el índice -1.
"""

puntajes = []

for x in range(6):
    nuevo_puntaje = input(f"Ingresa puntaje {x + 1}: ")
    puntajes.append(nuevo_puntaje)
   
 
puntajes_ordenados = puntajes.sort(reverse = True)     
    
print(f"Top 3 de los mejores puntajes: {puntajes_ordenados[0:3]}")
print(f"Puntaje mas bajo: {puntajes_ordenados[-1]}")    
    






