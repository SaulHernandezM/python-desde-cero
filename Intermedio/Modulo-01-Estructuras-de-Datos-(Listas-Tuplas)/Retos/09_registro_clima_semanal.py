"""
Reto: Registro de Clima Semanal (Tuplas)
Aquí usaremos tuplas para proteger los datos de cada día.
    Crea una lista llamada semana que contenga tuplas con el formato (dia, temperatura).
    Ejemplo: [("Lunes", 22), ("Martes", 25), ("Miercoles", 19) ...] (llénala con los 7 días).
    Misión: Recorre la lista y encuentra:
        El día con la temperatura más alta.
        El día con la temperatura más baja.
    Salida: Imprime un reporte: "El día más caluroso fue [dia] con [temp]° 
    y el más frío fue [dia] con [temp]°"
"""

semana = [("Lunes", 22), ("Martes", 25), ("Miercoles", 19), 
          ("Jueves", 20), ("Viernes", 15), ("Sabado", 29), ("Domingo", 18)]



for dia, temperatura in semana:
   if temperatura in semana:
      temp_alta = max(temperatura)
      temp_baja = min(temperatura) 
    
print(f"El dia mas caluroso fue {dia} con {temp_alta}°")
print(f"El dia mas frio fue {dia} con {temp_baja}°")
