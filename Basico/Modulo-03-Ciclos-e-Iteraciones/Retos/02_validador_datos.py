"""
Reto: El Validador de Datos (Bucle de Control)
Un sistema profesional nunca confía en el usuario.
    Misión: Crea un programa que pida una calificación al usuario.
    Regla: La calificación debe estar entre 0 y 10.
    Lógica: Si el usuario ingresa un número fuera de ese rango (ej: 15 o -5), 
    el programa debe decir "Error: Nota inválida" y volver a pedirla infinitamente hasta 
    que el usuario ingrese un número correcto.
    Al final: Cuando por fin sea válida, imprime "Nota registrada exitosamente: [nota]".
"""

while True:
    
    calificacion = int(input("Ingrese una calificacion en un rango de 0 - 10: "))
    
    if calificacion >= 0 or calificacion <= 10:
        print(f"Calificacion registrada exitosamente: {calificacion}")
        break
    
    elif calificacion < 0 or calificacion > 10:
        print("Error: Nota inválida")
        
   


