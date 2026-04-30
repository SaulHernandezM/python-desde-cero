"""
Problema: Traductor de Países (Acceso Directo Sin Bucle)
    Crea un diccionario llamado capitales donde la llave sea el país y el valor sea la capital.
        {"Mexico": "CDMX", "Francia": "Paris", "Japon": "Tokio"}
    Crea una función llamada obtener_capital(pais, diccionario).
    Misión: La función no debe usar bucles for. Solo debe verificar si el país está en el diccionario.
        Si está, retorna la capital.
        Si no está, retorna "País no registrado".
    Uso: Pide al usuario un país y muestra el resultado de la función.
"""

def obtener_capital(pais, diccionario):
    if pais in diccionario:
        return diccionario[pais]
    else:
        return "País no registrado"

capitales =  {"Mexico": "CDMX", "Francia": "Paris", "Japon": "Tokio"}

pais_user = input("Pais: ")

mostras_cap = obtener_capital(pais_user, capitales)

print(f"Capital: {mostras_cap}.")
