"""
Reto: El Validador de Permisos (Sets + Dics)
Imagina que gestionas los accesos de una empresa.
    Crea un diccionario roles_permisos donde las llaves son roles ("Admin", "Editor", "Invitado") y 
    los valores son Sets con sus permisos.
        {"Admin": {"borrar", "editar", "ver"}, "Editor": {"editar", "ver"}}
    Misión:
        Pide al usuario que ingrese dos roles para comparar.
        Muestra qué permisos tienen en común esos dos roles.
        Muestra qué permisos tiene el primer rol que el segundo no tiene (diferencia).
"""

roles_permisos = {"Admin": {"borrar", "editar", "ver"}, "Editor": {"editar", "ver"}, "Invitado": {"ver"}}

comparar_rol1 = input("Rol a comparar 1 (Admin, Editor, Invitado): ")
comparar_rol2 = input("Rol a comparar 2 (Admin, Editor, Invitado): ")

if comparar_rol1 and comparar_rol2 in roles_permisos:
    roles_comun = roles_permisos[comparar_rol1].intersection(roles_permisos[comparar_rol2])
    roles_diferente = roles_permisos[comparar_rol1].difference(roles_permisos[comparar_rol2])
    print(f"Permisos en comun de {comparar_rol1} y {comparar_rol2}: {roles_comun}.")
    print(f"Permisos que tiene {comparar_rol1} que no tiene {comparar_rol2}: {roles_diferente}.")
else:
    print("Roles no encontrados.")
    
    

"""
Tu lógica fue: if comparar_rol1 and comparar_rol2 in roles_permisos:.
    El error: En Python, esto se lee como: "¿Existe comparar_rol1? (Sí) Y ¿Está comparar_rol2 en el 
    diccionario?". No verifica que ambos estén dentro. Si escribes un rol que no existe en el primero, 
    el programa intentará operar y lanzará un error.
    Corrección: if comparar_rol1 in roles_permisos and comparar_rol2 in roles_permisos:
"""

