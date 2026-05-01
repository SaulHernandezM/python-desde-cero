"""
Reto: El Buscador de "Gamer" (Diccionario de Listas de Diccionarios)
Este simula una base de datos de una red social de juegos.
    Tienes este diccionario:
usuarios = {
    "user1": {"nombre": "Saul", "juegos": [{"titulo": "Halo", "puntos": 500}, 
    {"titulo": "Zelda", "puntos": 100}]}, "user2": {"nombre": "Ana", "juegos": 
    [{"titulo": "Halo", "puntos": 900}]}
}
    Crea una función buscar_pro_gamers(dicc_usuarios, puntos_minimos).
    Misión: La función debe recorrer a todos los usuarios y sus juegos. Debe retornar una lista 
    de nombres de aquellos usuarios que tengan al menos un juego con puntos mayores o iguales a 
    puntos_minimos.
    Si llamo a la función con 800, debería devolver ["Ana"].
"""

def buscar_pro_gamers(dicc_usuarios, puntos_minimos):
    ganadores = []
    for user_id, info in dicc_usuarios.items():
        # info["juegos"] es una LISTA, entramos con otro bucle
        for juego in info["juegos"]:
            # juego es un DICCIONARIO: {"titulo": "...", "puntos": ...}
            if juego["puntos"] >= puntos_minimos:
                ganadores.append(info["nombre"])
                break # Con que gane en uno es suficiente, pasamos al siguiente usuario
    return ganadores
                

usuarios = {
    "user1": {"nombre": "Saul", "juegos": [{"titulo": "Halo", "puntos": 500}, {"titulo": "Zelda", "puntos": 100}]}, 
    "user2": {"nombre": "Ana", "juegos": [{"titulo": "Halo", "puntos": 900}]}}

puntos = float(input("Puntos: "))

buscar = buscar_pro_gamers(usuarios, puntos)

print(buscar)
