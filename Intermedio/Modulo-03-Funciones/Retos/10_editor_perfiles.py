"""
Reto: El Editor de Perfiles (Modificación)
Imagina que un usuario quiere actualizar sus habilidades tecnológicas.
    Crea un diccionario usuarios_it donde la llave es el nombre y el valor es una lista de habilidades.
        usuarios_it = {"Alice": ["Python", "SQL"], "Bob": ["Java"]}
    Crea una función actualizar_habilidad(nombre, nueva_habilidad, diccionario).
    Misión:
        Si el usuario existe, añade la nueva_habilidad a su lista (pero solo si no la tiene ya).
        Si el usuario no existe, agrégalo al diccionario con esa única habilidad inicial.
        Retorna el diccionario actualizado.
"""

def actualizar_habilidad(nombre, nueva_habilidad, diccionario):
    if nombre in diccionario:
        if nueva_habilidad in diccionario:
            nombre[nueva_habilidad] = nueva_habilidad
        else:
            nombre[nueva_habilidad] += nueva_habilidad
        
        return diccionario
            
    if nombre not in diccionario:
        diccionario += nombre[nueva_habilidad]
    else:
        diccionario = nombre[nueva_habilidad]
        
        return diccionario

usuarios_it = {"Alice": ["Python", "SQL"], "Bob": ["Java"]}


nombre_user = input("Nombre: ")
habilidad_user = input("Habilidad (Python, SQL, Java): ")

usuario = actualizar_habilidad(nombre_user, habilidad_user, usuarios_it)

print(usuario)

