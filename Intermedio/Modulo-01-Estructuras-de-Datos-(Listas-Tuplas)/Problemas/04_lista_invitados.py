"""
Problema: La Lista de Invitados (Listas)
Este ejercicio te obligará a insertar elementos en posiciones específicas.
    Crea una lista inicial: invitados = ["Ana", "Juan", "Pedro"].
    Lógica:
        Un nuevo invitado, "María", debe ser la primera de la lista 
        (investiga el método .insert(posicion, valor)).
        Resulta que "Juan" no puede venir. Búscalo en la lista y 
        reemplázalo por "Ricardo" usando su índice.
        Ordena la lista alfabéticamente.
    Muestra la lista final.
"""

invitados = ["Ana", "Juan", "Pedro"]

nuevo_invitado = input("Agrega un nuevo invitado a la lista: ")

invitados.insert(0, nuevo_invitado)

print(invitados)

invitados[2] = "Ricardo"

invitados.sort()

print(invitados)





