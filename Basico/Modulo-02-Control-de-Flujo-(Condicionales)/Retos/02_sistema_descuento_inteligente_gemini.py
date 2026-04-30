"""
¿Qué mejoras aplicamos aquí?
    Normalización de datos: Con .lower(), no importa si el usuario escribe "SI", "si" o "Si", siempre lo entenderemos.
    Operador in: Es mucho más limpio que usar muchos or.
    Cálculo Único: Solo calculamos el descuento al final, basándonos en la variable porcentaje_descuento.
    Formato de moneda: :.2f asegura que siempre veamos dos decimales.
"""

print("### Sistema de Descuento Profesional ###")

# 1. Entrada y Normalización
# .strip() quita espacios y .lower() pasa todo a minúsculas
respuesta = input("¿Tiene membresía? (Si/No): ").strip().lower()

# Convertimos la respuesta a un Booleano real
# Verificamos si la respuesta está dentro de una lista de opciones válidas
tiene_membresia = respuesta in ["si", "s", "yes", "y"]

monto = float(input("Ingrese el monto de la compra: "))

# 2. Definición de variables de estado
porcentaje_descuento = 0

# 3. Lógica de Negocio (Evaluación de arriba hacia abajo)
if monto > 1000:
    if tiene_membresia:
        porcentaje_descuento = 0.20  # 20%
    else:
        porcentaje_descuento = 0.10  # 10%
elif 500 <= monto <= 1000:
    porcentaje_descuento = 0.05      # 5%
else:
    porcentaje_descuento = 0.00      # 0%

# 4. Cálculos finales (Solo una vez)
monto_descuento = monto * porcentaje_descuento
total_pagar = monto - monto_descuento

# 5. Salida limpia usando f-strings
print("-" * 30)
print(f"Monto Original: ${monto:,.2f}")
print(f"Descuento ({porcentaje_descuento*100}%): -${monto_descuento:,.2f}")
print(f"TOTAL A PAGAR: ${total_pagar:,.2f}")
print("-" * 30)