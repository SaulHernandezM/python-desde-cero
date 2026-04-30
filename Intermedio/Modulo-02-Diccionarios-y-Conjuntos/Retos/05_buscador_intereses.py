"""
Reto: El Buscador de Intereses Únicos (Sets + Listas)
Imagina que eres un analista de datos para una red social.
    Crea una lista de listas llamada intereses_usuarios. Cada sub-lista contiene los intereses 
    de un usuario diferente.
        Ejemplo: [["musica", "cine"], ["cine", "deporte", "arte"], ["arte", "musica", "viajes"]]
Misión:
    Crea un conjunto (set) vacío llamado todos_los_intereses.
    Recorre la lista principal con un bucle for y, por cada sub-lista, agrega sus elementos al conjunto. 
    (Pista: puedes usar el método .update() de los conjuntos para agregar varios elementos de golpe).
Resultado:
    Muestra cuántos intereses únicos hay en total en toda la plataforma.
    Muestra la lista de intereses ordenada alfabéticamente.
"""

intereses_usuarios = [["musica", "cine"], ["cine", "deporte", "arte"], ["arte", "musica", "viajes"]]

todos_los_intereses = {}

for lista in intereses_usuarios:
    lista
