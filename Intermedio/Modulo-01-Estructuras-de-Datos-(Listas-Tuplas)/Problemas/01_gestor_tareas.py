"""
Problema: El Gestor de Tareas.
Crea una lista llamada tareas que contenga 3 actividades iniciales.
    Lo que se espera:
    1.  Pide al usuario una nueva tarea y agrégala a la lista.
    2.  Muestra la lista completa.
    3.  Elimina la segunda tarea de la lista (índice 1).
    4.  Muestra cuántas tareas quedan en total usando len().
"""

tareas = ["Barrer", "Lavar ropa", "Limpiar cuarto"]

nueva_tarea = input("Agrega una nueva tarea: ")

tareas.append(nueva_tarea)

print(f"Lista de tareas: {tareas}")

tareas.pop(1)

print(f"Tareas por realizar:",len(tareas))

