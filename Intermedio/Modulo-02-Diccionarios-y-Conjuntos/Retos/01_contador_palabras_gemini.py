frase = input("Frase: ").lower()
palabras = frase.split() # Esto crea una lista: ["hola", "mundo", "hola"]

frecuencias = {}

for p in palabras:
    if p in frecuencias:
        frecuencias[p] += 1 # Si ya existe, sumamos 1 al valor
    else:
        frecuencias[p] = 1  # Si no existe, lo creamos con valor 1

print("Frecuencia de palabras:", frecuencias)