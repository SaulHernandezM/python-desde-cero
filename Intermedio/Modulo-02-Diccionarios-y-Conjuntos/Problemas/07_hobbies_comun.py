"""
Problema: Hobbies en Común (Conjuntos / Sets)
Los conjuntos no solo sirven para borrar duplicados, también sirven para comparar colecciones.
    Crea dos conjuntos:
        mis_hobbies = {"leer", "correr", "cine", "nadar"}
        hobbies_amigo = {"cine", "futbol", "leer", "videojuegos"}
    Misión: Investiga y usa los métodos de conjuntos para mostrar:
        Intersección: Los hobbies que ambos tienen en común (usa mis_hobbies.intersection(hobbies_amigo)).
        Diferencia: Los hobbies que tú tienes pero tu amigo no (usa mis_hobbies.difference(hobbies_amigo)).
    Imprime ambos resultados. 
"""

mis_hobbies = {"leer", "correr", "cine", "nadar"}
hobbies_amigo = {"cine", "futbol", "leer", "videojuegos"}

print(mis_hobbies.intersection(hobbies_amigo))
print(mis_hobbies.difference(hobbies_amigo))

