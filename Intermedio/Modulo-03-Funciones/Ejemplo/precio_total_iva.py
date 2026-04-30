def calcular_total(precio_base):
    iva = precio_base * 0.16
    total = precio_base + iva
    return total # La función "suelta" el resultado

# Así se usa:
pago_final = calcular_total(100)
print(f"El total a pagar es: {pago_final}") # Resultado: 116.0