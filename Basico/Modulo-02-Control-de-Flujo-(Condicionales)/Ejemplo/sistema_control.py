# Definición de criterios de seguridad
EDAD_MINIMA = 18
TIENE_INVITACION = True

# Entrada de datos del usuario
edad_usuario = int(input("Por favor, ingrese su edad: "))

# Lógica de decisión con operadores lógicos
# El uso de 'and' requiere que AMBAS condiciones sean verdaderas
if edad_usuario >= EDAD_MINIMA and TIENE_INVITACION:
    print("Acceso concedido. Bienvenido al sistema.")
elif edad_usuario < EDAD_MINIMA:
    print("Acceso denegado. Eres menor de edad.")
else:
    # Este bloque se ejecuta si es mayor de edad pero no tiene invitación
    print("Acceso denegado. Se requiere una invitación válida.")

# El programa continúa aquí después de cualquier bloque evaluado
print("Fin de la verificación de seguridad.")