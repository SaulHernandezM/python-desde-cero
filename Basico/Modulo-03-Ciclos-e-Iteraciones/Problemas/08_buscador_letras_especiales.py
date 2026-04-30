"""
Problema: El Buscador de Letras Especiales (for + break)
Objetivo: Aprender a detener un proceso en cuanto encontramos lo que buscamos (eficiencia).
    Descripción: Buscar si una frase contiene la letra "z".
    Instrucciones: Pide una frase al usuario. Recorre la frase letra por letra. 
    En el momento en que encuentres una "z", imprime "¡Letra crítica detectada!" y 
    detén el bucle inmediatamente (no sigas revisando el resto de la frase).
    Resultado esperado: Si no hay ninguna "z", el programa simplemente termina 
    (o puedes poner un mensaje final).
"""

frase = input("Ingresa una frase: ").strip().lower()

for x in frase:
    if "z" in frase:
        print("¡Letra crítica detectada!")
        break
    else:
        break
    
print("No se encontro ninguna letra critica.")

"""
Problema (Buscador de 'z'): Tu código hace if "z" in frase. Eso no está usando el bucle 
para recorrer la frase, sino que le pregunta a Python si la letra está en todo el texto de golpe. 
Además, el else: break hace que si la primera letra no es "z", el programa se detenga sin revisar el resto.
"""



