# Ejercico resuelto por Gemini

print("### Clasificador de números mejorado ###")
numero = int(input("Ingresa un número: "))

if numero == 0:
    print("El número es cero")
else:
    # Determinamos primero si es positivo o negativo
    if numero > 0:
        referencia = "positivo"
    else:
        referencia = "negativo"
    
    # Determinamos si es par o impar usando SIEMPRE el módulo 2
    if numero % 2 == 0:
        print(f"El número es {referencia} y es par")
    else:
        print(f"El número es {referencia} y es impar")