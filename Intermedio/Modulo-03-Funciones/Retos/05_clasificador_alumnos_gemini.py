"""
Reto: El Clasificador de Alumnos (Creación de Diccionarios Complejos)
Aquí transformaremos una estructura en otra totalmente distinta.
Crea un diccionario de clase donde la llave es el nombre y el valor es la calificación 
(ej: {"Ana": 90, "Luis": 65, "Pepe": 80, "Sonia": 40}).
Crea una función llamada clasificar_estudiantes(diccionario_alumnos).
Misión:
La función debe crear un nuevo diccionario con dos llaves: "Aprobados" y "Reprobados".
Los valores de estas llaves deben ser listas con los nombres de los alumnos correspondientes.
Uso: Imprime el diccionario resultante para ver cómo quedó organizada la clase.
"""

def clasificar_estudiantes(diccionario_alumnos):
    # 1. Preparamos la "caja" con sus divisiones vacías
    resultado = {
        "Aprobados": [], 
        "Reprobados": []
    }
    
    # 2. Recorremos el diccionario original
    for nombre, nota in diccionario_alumnos.items():
        # 3. Aplicamos la lógica de clasificación
        if nota >= 70:
            # Agregamos el nombre a la lista correspondiente dentro de 'resultado'
            resultado["Aprobados"].append(nombre)
        else:
            resultado["Reprobados"].append(nombre)
            
    return resultado

# --- PRUEBA ---
clase = {"Ana": 90, "Luis": 65, "Pepe": 80, "Sonia": 40, "Carla": 72}
reporte = clasificar_estudiantes(clase)

print(f"Diccionario clasificado: {reporte}")
print(f"Total aprobados: {len(reporte['Aprobados'])}")
