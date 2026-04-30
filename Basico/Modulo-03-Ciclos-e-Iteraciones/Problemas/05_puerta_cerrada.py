"""
Problema: La Puerta Cerrada (while con centinela)
Objetivo: Usar una condición de texto para detener un proceso.
    Descripción: El programa es un guardia que no te deja pasar hasta que digas la palabra "por favor".
    Instrucciones: Crea un bucle while que pida una palabra al usuario. El bucle debe repetirse mientras 
    la palabra NO sea igual a "por favor".
    Resultado esperado: El programa sigue pidiendo la palabra hasta que el usuario escriba la correcta, 
    entonces imprime "Puedes pasar".
"""

while True:
    palabra_magica = input("Ingrese la palabra magica para entrar: ").strip().lower()
    
    if palabra_magica != "por favor":
        print("Palabra magica incorrecta. Por favor intentelo de nuevo.")
    else:
        break

print("Puedes pasar.")    


