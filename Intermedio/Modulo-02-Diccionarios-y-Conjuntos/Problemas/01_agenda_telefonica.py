"""
Problema: La Agenda Telefónica.
Crea un diccionario vacío llamado agenda.
    Pide al usuario que ingrese 3 contactos (Nombre y Teléfono).
    Agregalos al diccionario.
    Pide un nombre para buscar. Si el nombre está en la agenda (if nombre in agenda:), 
    muestra su teléfono. Si no, avisa que no existe.
    Muestra todos los nombres registrados usando el método .keys().
"""

agenda = {
}

print("Ingresa 3 contactos")

for x in range(1, 4):  
    nombre = input("Nombre: ")
    telefono = int(input("Telefono: "))
    
    agenda[nombre] = telefono
    
print("#### Buscar contacto ####")
buscar = input("Nombre: ")

if buscar in agenda:
    print(f"Telefono: {agenda[buscar]}")
else:
    print("El usuario no existe.")
    print(agenda.keys())