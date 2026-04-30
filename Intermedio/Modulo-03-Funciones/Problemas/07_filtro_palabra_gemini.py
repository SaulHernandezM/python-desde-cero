def filtrar_cortas(lista_palabras, limite):
    lista_final = [] # 1. Creamos el contenedor
    for palabra in lista_palabras: # 'palabra' es un nombre más claro que 'nueva_lista'
        if len(palabra) > limite:
            lista_final.append(palabra) # 2. Guardamos sin salir de la función
    return lista_final # 3. Salimos entregando TODO al terminar el for

frutas = ["Fresa", "Mango", "Platano", "Pepino", "Sandia", "Melon", "Naranja", "Pera"]
limite = int(input("Ingrese un número: "))

resultado = filtrar_cortas(frutas, limite)
print(f"Frutas que superan el límite: {resultado}")