agenda_trabajo = {"Saul": "saul@gmail.com", "Samuel": "samuel@gmail.com", "Said": "said@gmail.com",
                "Sara": "sara@gmail.com", "Sasha": "sasha@gmail.com", "Sam": "sam@gmail.com"}


agenda_personal = {"Saul": "saul@gmail.com", "Samanta": "samanta@gmail.com", "Said": "said@gmail.com",
                "Sabrina": "sabrina@gmail.com", "Sasha": "sasha@gmail.com", "Sam": "sam@gmail.com"}

# Convertimos las llaves directamente a conjuntos (sets)
nombres_trabajo = set(agenda_trabajo.keys())
nombres_personal = set(agenda_personal.keys())

# Ahora sí podemos usar operaciones de conjuntos
todos_los_contactos = nombres_trabajo.union(nombres_personal)
comunes = nombres_trabajo.intersection(nombres_personal)

print(f"Tienes {len(todos_los_contactos)} contactos únicos en total.")
print(f"Contactos repetidos en ambas agendas: {comunes}")