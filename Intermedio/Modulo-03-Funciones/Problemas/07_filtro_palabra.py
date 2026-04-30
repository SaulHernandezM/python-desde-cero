"""
Problema: El Filtro de Palabras (Lógica con Listas)
Este reto requiere que la función tome decisiones sobre una colección.
    Crea una función llamada filtrar_cortas(lista_palabras, limite).
        Debe recorrer la lista y crear una nueva lista que solo contenga las palabras que 
        tengan más caracteres que el limite.
        Retorna la nueva lista.
    Misión: Crea una lista de 5 frutas. Pide al usuario un número (el límite) y usa la función 
    para mostrarle qué frutas tienen un nombre más largo que ese número.
"""

def filtrar_cortas(lista_palabras, limite):
    for nueva_lista in lista_palabras:
        if len(nueva_lista) > limite:
            return nueva_lista

frutas = ["Fresa", "Mango", "Platano", "Pepino", "Sandia", "Melon", "Naranja", "Pera"]

print(f"Frutas: {frutas}.")

limite = int(input("Ingrese un numero: "))

frutas_limite = filtrar_cortas(frutas, limite)
print(f"Frutas: {frutas_limite}.")

"""
Me comentaste que solo te devuelve "Fresa". Esto sucede por cómo funciona la palabra clave return.
El concepto: Imagina que una función es una habitación. El return es la puerta de salida. En el momento 
en que el código llega a un return, la función se detiene por completo, sale de la habitación
y entrega el valor.
Tu código: En la primera vuelta del bucle, encontró que "Fresa" (5 letras) era mayor al límite
(si pusiste 3, por ejemplo) y ejecutó el return. Ahí se acabó todo; el programa ya no siguió 
con "Mango", "Platano", etc.
La solución: Debes crear una lista vacía antes del bucle, usar .append() para llenarla y poner 
el return fuera del bucle para que entregue la lista completa al final.
"""
