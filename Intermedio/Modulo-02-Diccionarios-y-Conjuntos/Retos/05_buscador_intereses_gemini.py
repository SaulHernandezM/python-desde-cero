intereses_usuarios = [["musica", "cine"], ["cine", "deporte", "arte"], ["arte", "musica", "viajes"]]
todos_los_intereses = set() # Creamos el conjunto vacío

for sublista in intereses_usuarios:
    # .update agrega todos los elementos de la sublista de golpe y elimina duplicados solo
    todos_los_intereses.update(sublista) 

print(f"Intereses únicos: {sorted(todos_los_intereses)}")
print(f"Total de intereses únicos: {len(todos_los_intereses)}")