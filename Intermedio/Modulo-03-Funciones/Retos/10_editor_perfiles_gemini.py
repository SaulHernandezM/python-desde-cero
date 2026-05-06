def actualizar_habilidad(nombre, nueva_habilidad, diccionario):
    if nombre in diccionario:
        # Si el usuario existe, verificamos si ya tiene la habilidad
        if nueva_habilidad not in diccionario[nombre]:
            diccionario[nombre].append(nueva_habilidad)
    else:
        # Si no existe, lo creamos con una lista que contiene la nueva habilidad
        diccionario[nombre] = [nueva_habilidad]
    
    return diccionario

# Ejemplo de uso
usuarios_it = {"Alice": ["Python", "SQL"], "Bob": ["Java"]}
# Si agregamos "Java" a Alice, se añade. Si agregamos "Python" a Alice, no se duplica.

nombre_user = input("Nombre: ")
habilidad_user = input("Habilidad (Python, SQL, Java): ")

usuario = actualizar_habilidad(nombre_user, habilidad_user, usuarios_it)

print(usuario)