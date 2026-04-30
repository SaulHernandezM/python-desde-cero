"""
Problema: Generador de Credenciales
Las funciones no solo sirven para números; son poderosas para estandarizar texto.
    Crea una función llamada generar_usuario(nombre, apellido) que:
        Convierta ambos a minúsculas.
        Retorne la unión del nombre y el apellido con un punto en medio (ej: "saul.perez").
    Crea una función llamada validar_seguridad(password) que reciba un texto y:
        Retorne True si tiene 8 caracteres o más.
        Retorne False si es más corta.
    Misión: Pide los datos al usuario y usa las funciones para mostrarle su nuevo nombre de usuario y 
    decirle si su contraseña elegida es segura o no.
"""

def generar_usuario(nombre, apellido):
    # Guardamos el resultado o lo procesamos en el return
    # nombre_min = nombre.lower()
    # apellido_min = apellido.lower()
    # return f"{nombre_min}.{apellido_min}" Usar f-strings es más limpio
    
    nombre.lower(), apellido.lower()
    return nombre + "." + apellido 

def validar_seguridad(password): 
    return len(password) >= 8


nombre = input("Nombre: ")
apellido = input("Apellido: ")
contraseña = input("Contraseña: ")

usuario = generar_usuario(nombre, apellido)
contraseña_elegible = validar_seguridad(contraseña)

print(f"Usuario generado: {usuario}")
print(f"Contraseña aprobada: {contraseña_elegible}")


"""
En la función generar_usuario, escribiste nombre.lower(), apellido.lower().
Lo que pasó: En Python, los strings son inmutables. Esto significa que .lower() no cambia la variable
original, sino que "crea" una nueva versión en minúsculas. Si no guardas ese resultado en una variable 
(o lo usas directamente en el return), el cambio se pierde.
"""
