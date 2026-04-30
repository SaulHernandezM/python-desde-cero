# Imagina un sistema que gestiona una fila de espera en un banco.

# Creamos una lista inicial (mutable)
clientes = ["Ana", "Pedro", "Luis"]

# Llega un nuevo cliente
clientes.append("Marta") 

# Atendemos al primero (índice 0)
atendido = clientes.pop(0)

print(f"Se atendió a: {atendido}")
print(f"Quedan en espera: {clientes}")
print(f"El próximo es: {clientes[0]}") # Acceso por índice

# Ejemplo de Tupla (datos que no deberían cambiar, como coordenadas)
posicion_sucursal = (19.4326, -99.1332)
# posicion_sucursal[0] = 20.0  # <-- Esto daría ERROR porque es inmutable