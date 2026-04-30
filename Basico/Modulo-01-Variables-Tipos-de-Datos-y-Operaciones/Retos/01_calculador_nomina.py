"""
Reto: El Calculador de Nómina Simple.
Imagina que estás diseñando un módulo para un sistema de recursos humanos. Debes solicitar al usuario:
    El nombre del empleado.
    Las horas trabajadas en la semana.
    El pago por hora.
    El programa debe calcular el salario bruto, restarle un 12% 
    en concepto de impuestos (retención legal) y mostrar un "recibo de pago" 
    en la terminal que incluya el nombre, el salario bruto, el monto del impuesto y el salario neto final.
"""

print("### Calculador de nomina ###")

# Datos a obtener
nombre_empleado = input("Ingrese el nombre del empleado: ")
horas_trabajadas = int(input("Ingrese las horas trabajadas en la semana por el empleado: "))
pago_hora = float(input("Ingrese el pago por hora al empleado: "))

# Operaciones
salario_bruto = horas_trabajadas * pago_hora
monto_impuesto = salario_bruto * 0.12
salario_neto = salario_bruto - monto_impuesto

print("\n")

# Recibo de pago
print("Recibo de pago")
print(f"Nombre del empleado: {nombre_empleado}")
print(f"Salario bruto: {salario_bruto}")
print(f"Monto del impuesto: {monto_impuesto}")
print(f"Salario neto: {salario_neto}")