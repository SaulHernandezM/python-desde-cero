"""
Reto: El Algoritmo de Triaje Médico (Sistema de Emergencias)
Vas a programar la lógica de un sistema de entrada para un hospital. 
El programa debe recibir los datos de un paciente y determinar a qué área debe ser enviado y con qué prioridad.
1. Entrada de Datos:
    Nombre del paciente.
    Edad (número).
    Saturación de oxígeno (número de 0 a 100).
    Temperatura (número en Celsius, ej: 38.5).
    ¿Tiene dificultad para respirar? (Si/No).
2. Reglas de Negocio (Lógica de Prioridad):
El sistema debe clasificar según estos criterios jerárquicos:
    PRIORIDAD 1 (CRÍTICO): * Si la saturación de oxígeno es menor a 90 O si el paciente dice SI a la dificultad para respirar.
        Acción: Imprimir "Enviar inmediatamente a REANIMACIÓN".
    PRIORIDAD 2 (URGENCIA): * Si no es crítico, pero tiene fiebre alta (temperatura mayor o igual a 39) O si es un paciente de riesgo 
    (edad mayor a 65 o menor a 5).
        Acción: Imprimir "Enviar a EVALUACIÓN URGENTE".
    PRIORIDAD 3 (ESTABLE): * Si no cumple ninguna de las anteriores.
        Acción: Imprimir "Enviar a SALA DE ESPERA GENERAL".
3. Requisitos Técnicos:
    Validación de rangos: Si el usuario ingresa una saturación mayor a 100 o menor a 0, debe mostrar un error de "Dato de oxígeno inválido".
    Normalización: La respuesta de "dificultad para respirar" debe aceptar "si", "SI", "s", etc.
    Salida Profesional: El programa debe mostrar un resumen con el nombre del paciente, sus signos vitales y la decisión final del sistema.
"""

print("##### SISTEMA DE EMERGENCIAS ####")
# Datos del paciente
nombre_paciente = input("Ingresa el nombre del paciente: ")
edad_paciente = int(input("Ingresa la edad del paciente: "))
saturacion_oxigeno = int(input("Ingrese la saturacion de oxigeno del paciente (0 - 100): "))
temperatura_paciente = float(input("Ingrese la temperatura del paciente: "))
dificultad_respirar = input("¿Tiene dificultad para respirar? (Si/No): ").strip().lower()
dificultad_respirar_si = dificultad_respirar in ["si", "s", "yes", "y"]
dificultad_respirar_no = dificultad_respirar in ["no", "n"]

print("\n###################################################\n")

# Resumen datos del paciente
print(f"El paciente {nombre_paciente} con edad de {edad_paciente}.")
print(f"Tienen una saturacion de oxigeno de {saturacion_oxigeno} y una temperatura corporal de {temperatura_paciente}.")
if dificultad_respirar_si:
    print("Presenta dificulta para respirar.")
else:
    print("No presenta dificultad para respirar.")
print(f"Por lo tanto se ha tomado la decision de enviar al paciente {nombre_paciente} a: ")

# Procesamiento de prioridad
if 0 < saturacion_oxigeno or saturacion_oxigeno> 100:
    print("Dato de oxigeno invalido.")    
    
    if 90 < saturacion_oxigeno or dificultad_respirar_si:
        print("Enviar inmediatamente a REANIMACIÓN")

elif 39. >= temperatura_paciente or 5 <= edad_paciente or edad_paciente >= 65:
    print("Enviar a EVALUACIÓN URGENTE")
    
else:
    print("Enviar a SALA DE ESPERA GENERAL")