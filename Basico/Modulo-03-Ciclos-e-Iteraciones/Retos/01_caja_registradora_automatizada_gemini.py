print("### CAJA REGISTRADORA ###")

# 1. Inicializamos los "contenedores" de datos
total_cuenta = 0.0
cantidad_productos = 0

while True:
    precio = float(input("Ingrese precio del producto (o 0 para finalizar): "))
    
    # 2. Condición de salida (Centinela)
    if precio == 0:
        break 
    
    # 3. Validación básica: no aceptar precios negativos
    if precio < 0:
        print("Precio inválido, intente de nuevo.")
        continue # Salta al inicio del bucle sin sumar nada
    
    # 4. Actualización de datos
    total_cuenta += precio       # Acumulador (Suma valores)
    cantidad_productos += 1      # Contador (Suma de 1 en 1)

# 5. Cálculos finales y salida
if cantidad_productos > 0:
    promedio = total_cuenta / cantidad_productos
    print("-" * 20)
    print(f"Total de la compra: ${total_cuenta:.2f}")
    print(f"Productos comprados: {cantidad_productos}")
    print(f"Precio promedio: ${promedio:.2f}")
else:
    print("No se registraron productos.")