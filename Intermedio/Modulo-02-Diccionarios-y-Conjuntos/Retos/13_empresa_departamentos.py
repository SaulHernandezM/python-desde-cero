"""
Reto: La Empresa y sus Departamentos (Anidación + Listas)
Aquí vamos a mezclar diccionarios con listas para simular una base de datos real.
    Crea un diccionario empresa. Las llaves son departamentos ("Ventas", "IT"). El valor es una lista 
    de diccionarios (cada diccionario es un empleado con nombre y puesto).
        empresa = {"IT": [{"nombre": "Ana", "puesto": "Dev"}, {"nombre": "Luis", "puesto": "Soporte"}]}
    Misión:
        Pide al usuario el nombre de un departamento.
        Si existe, recorre la lista de ese departamento con un for.
        Por cada empleado, imprime: "Empleado: [nombre] | Cargo: [puesto]".
        Extra: Al final, muestra cuántas personas trabajan en ese departamento usando len().
"""

empresa = {"Ventas": [{"nombre": "Pablo", "puesto": "Marketing"}, {"nombre": "Karen", "puesto": "Analista Ventas"}],
           "IT": [{"nombre": "Ana", "puesto": "Dev"}, {"nombre": "Luis", "puesto": "Soporte"}]}

nombre_depa = input("Departamento (Ventas, IT): ")

if nombre_depa in empresa:
    for empleado, puesto in empresa.items():
        print(f"Empleado: {empresa[empleado]} | Cargo: {empresa[puesto]}.")
        print(f"Personas trabajando en {nombre_depa}: {len(nombre_depa)}.")
        
else:
    print("Empresa no encontrada.")


"""
El error del for: Escribiste for empleado, puesto in empresa.items():.
Esto recorre toda la empresa (Ventas e IT). Si el usuario eligió "IT", no deberías recorrer "Ventas".
Lo correcto es entrar directamente a la lista del departamento elegido: 
for empleado_info in empresa[nombre_depa]:.

Acceso a los datos: Una vez dentro de la lista, cada empleado_info es un pequeño diccionario. 
Para sacar el nombre, usas empleado_info["nombre"].

El conteo: Usaste len(nombre_depa). Como nombre_depa es un texto (ej. "IT"), el resultado era 2. 
Lo que queremos es el largo de la lista de empleados: len(empresa[nombre_depa]).
"""
