def promedio_alumno(nombre, diccionario):
    # No usamos for, vamos directo al grano
    if nombre in diccionario:
        notas = diccionario[nombre]
        # Calculamos el promedio
        return sum(notas) / len(notas)
    else:
        return "Alumno no encontrado"

estudiantes = {"Ana": [90, 80, 100], "Luis": [70, 60, 80], "Pepe": [79, 80, 90]}
nombre_buscado = input("Nombre del alumno: ")
resultado = promedio_alumno(nombre_buscado, estudiantes)

print(f"Resultado para {nombre_buscado}: {resultado}")