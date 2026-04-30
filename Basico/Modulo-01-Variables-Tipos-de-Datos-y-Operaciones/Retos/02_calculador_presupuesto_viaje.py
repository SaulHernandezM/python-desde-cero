"""
Reto: Calculadora de Presupuesto de Viaje
Para elevar el nivel de dificultad del reto de nómina, intenta este escenario:
Descripción:
Estás programando la lógica para una app de viajes. El programa debe:
    Pedir el presupuesto total del viaje.
    Pedir el número de días que durará el viaje.
    Calcular cuánto dinero puede gastar el usuario por día (promedio).
    Si el usuario gasta el 20% de su presupuesto total en el hotel, ¿cuánto dinero le queda disponible para el resto del viaje?
"""

print("### Calculadora de Presupuesto de Viaje ###")
# Varibles
presupuesto_viaje = float(input("Cual es el presupuesto del viaje?: "))
dias_duracion_viaje = int(input("Cuantos dias durara el viaje?: "))
 
# Calculos
presupuesto_hotel = presupuesto_viaje * 0.20
presupuesto_despues_hotel = presupuesto_viaje - presupuesto_hotel 
gasto_promedio_dia = (presupuesto_viaje - presupuesto_hotel) / dias_duracion_viaje

# Resultados
print("\n")
print("### Resumen del presupuesto del viaje ###")
print(f"El presupuesto del viaje es: {presupuesto_viaje}")
print(f"La duracion del viaje es de {dias_duracion_viaje} dias")
print(f"El costo del Hotel en base al 20% del presupuesto total del viaje es de: {presupuesto_hotel}")
print(f"El presupuesto restante es de {presupuesto_despues_hotel} despues del gasto del hotel")
print(f"El presupuesto diario resultante del viaje es: {gasto_promedio_dia}")


