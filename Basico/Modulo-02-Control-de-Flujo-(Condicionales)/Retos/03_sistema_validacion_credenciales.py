"""
Reto: El Sistema de Validación de Credenciales (Simulador de Login)
Requisitos del programa:
    Capa 1: Usuario y Rol.
        Pregunta el nombre de usuario.
        Pregunta el rol del usuario (las opciones válidas son: admin, editor, guest).
    Capa 2: Código de Acceso.
        Si el rol es admin, debe pedir una "Clave Maestra" (elige tú la palabra secreta).
        Si el rol es editor, debe pedir un "Código de Invitación".
        Si el rol es guest, no pide clave pero debe preguntar si acepta los "Términos y Condiciones" (Si/No).
    Capa 3: Evaluación de Horario (Lógica Numérica).
        Pregunta la hora actual (usa formato de 24 horas, del 0 al 23).
        Regla de Negocio: * Los admin pueden entrar a cualquier hora (0-23).
            Los editor solo pueden entrar si la hora está entre las 8 y las 18 (inclusive).
            Los guest solo pueden entrar entre las 10 y las 16 (inclusive).
Lo que se espera:
    El programa debe imprimir un mensaje de "ACCESO CONCEDIDO" solo si se cumplen los requisitos de rol, clave y horario.
    Debe imprimir "ACCESO DENEGADO" y la razón específica (ej: "Código incorrecto" o "Fuera de horario") si falla alguna validación.
    Importante: Debes usar la técnica de normalización que vimos antes (.lower(), .strip()) para que el programa no falle si escriben 
    "Admin" en lugar de "admin".
"""

# Variables donde se guardan el usuario y rol
nombre_usuario = input("Cual es tu nombre de usuario?: ")
rol_usuario = input("Cual es tu rol de usuario(admin, editor, guest)?: ").strip().lower()

# Variables para el tipo de rol
admin = "admin"
editor = "editor"
guest = "guest"

# Codigos de acceso
if rol_usuario == admin:
    clave = input("Ingrese la clave maestra: ")
if rol_usuario == editor:
    codigo_invitacion = input("Ingrese el codigo de invitacion: ")
if rol_usuario == guest:
    terminos_condiciones = input("Acepta los terminos y condiciones(Si/No): ").strip().lower()
    terminos_si = terminos_condiciones in ["SI", "Si", "si", "s", "S"]


# Variable para el horario
hora = float(input("Cual es la hora actual (usa formato de 24 horas, del 0.00 al 23.59): "))
clave_correcta = "clave1234"
codigo_invitacion_correcto = "invitacion1234"

# Comprobar clave y hora
if clave == clave_correcta:
    print("Acceso concedido. Bienvenido Administrador.")
elif clave != clave_correcta:
        print("Acceso denegado.")
if codigo_invitacion == codigo_invitacion_correcto and hora >= 8. and hora <= 18.59:
    print("Acceso concedido. Bienvenido Editor.")
elif codigo_invitacion != codigo_invitacion_correcto:
        print("Codigo de invitacion incorrecto.")
elif hora != 8. and hora != 18.59:
        print("Horario de entrada incorrecto.")
if guest >= 10. and guest <= 16:
    print("Acceso concedido. Bienvenido Guest.")
else:
    print("Horario de entrada incorrecto.")
    


    

    


    
    