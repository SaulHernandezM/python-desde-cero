"""
Problema: El Filtro de Invitados Duplicados (Sets/Conjuntos)
En programación, a menudo recibimos listas de datos "sucios" con elementos repetidos. 
Los conjuntos (set) son la herramienta perfecta para limpiar esto porque no permiten duplicados.
    Crea una lista llamada invitados_sucia que tenga varios nombres repetidos 
    (ej: ["Ana", "Luis", "Ana", "Pedro", "Luis", "Marta"]).
    Lógica:
        Muestra la lista original y cuántos nombres hay en total (len).
        Convierte la lista en un conjunto usando set(invitados_sucia) y guárdalo en una variable 
        llamada invitados_limpios.
        Convierte ese conjunto de nuevo a una lista.
    Resultado: Muestra la nueva lista y cuántos invitados quedaron tras eliminar los duplicados.
"""

invitados_sucio = ["Ana", "Luis", "Ana", "Pedro", "Luis", "Marta"]

print(f"Lista: {invitados_sucio}. Nombres: {len(invitados_sucio)}.")

invitados_limpios = set(invitados_sucio)

invitados_limpios = list(invitados_limpios)

print(f"Lista: {invitados_limpios}. Nombres: {len(invitados_limpios)}.")


