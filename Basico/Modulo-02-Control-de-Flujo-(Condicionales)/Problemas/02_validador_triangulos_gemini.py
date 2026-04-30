print("### Validador de Triángulos Profesional ###")

# 1. Entrada de datos
a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

# 2. Lógica de existencia (Se deben cumplir las 3 condiciones)
# Usamos paréntesis para agrupar visualmente la condición lógica
es_valido = (a + b > c) and (a + c > b) and (b + c > a)

if es_valido:
    print("La figura es un triángulo válido.")
    
    # 3. Clasificación (Solo entramos aquí si es válido)
    if a == b == c:
        print("Tipo: Equilátero")
    elif a == b or a == c or b == c:
        print("Tipo: Isósceles")
    else:
        print("Tipo: Escaleno")
        
else:
    print("Error: Los lados ingresados no pueden formar un triángulo.")