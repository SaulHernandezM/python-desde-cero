# Codigo generado por Gemini
print("### Sistema de Validación de Credenciales ###")

# 1. Datos Básicos
nombre = input("Nombre de usuario: ")
rol = input("Rol (admin, editor, guest): ").strip().lower()

# 2. Procesamiento por Roles (Filtros principales)
if rol == "admin":
    clave = input("Ingrese Clave Maestra: ")
    # Validación inmediata de Admin
    if clave == "clave1234":
        print(f"ACCESO CONCEDIDO. Bienvenido Administrador {nombre}.")
    else:
        print("ACCESO DENEGADO. Clave incorrecta.")

elif rol == "editor":
    codigo = input("Ingrese Código de Invitación: ")
    hora = float(input("Hora actual (0-23): "))
    
    # Validación doble para Editor
    if codigo != "invitacion1234":
        print("ACCESO DENEGADO. Código incorrecto.")
    elif not (8 <= hora <= 18):
        print("ACCESO DENEGADO. Fuera de horario (8-18h).")
    else:
        print(f"ACCESO CONCEDIDO. Bienvenido Editor {nombre}.")

elif rol == "guest":
    terminos = input("¿Acepta términos? (Si/No): ").strip().lower()
    acepta = terminos in ["si", "s", "yes", "y"]
    
    if acepta:
        hora = float(input("Hora actual (0-23): "))
        if 10 <= hora <= 16:
            print(f"ACCESO CONCEDIDO. Bienvenido Invitado {nombre}.")
        else:
            print("ACCESO DENEGADO. Fuera de horario para invitados (10-16h).")
    else:
        print("ACCESO DENEGADO. Debe aceptar los términos.")

else:
    print("ACCESO DENEGADO. Rol no reconocido.")