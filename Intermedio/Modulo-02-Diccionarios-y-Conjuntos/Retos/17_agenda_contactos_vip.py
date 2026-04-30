"""
Reto: Agenda de Contactos VIP (Diccionario -> Diccionario -> Diccionario)
Aquí la anidación es profunda para guardar datos muy específicos.
    Crea un diccionario contactos. La llave es el nombre. El valor es un diccionario con email 
    y direccion. A su vez, direccion es otro diccionario con ciudad y calle.
        {"Luis": {"email": "l@mail.com", "direccion": {"ciudad": "CDMX", "calle": "Reforma"}}}
    Misión:
        Pide el nombre de un contacto.
        Si existe, muestra su email.
        Entra a la dirección y muestra solo la ciudad.
        Reto Pro: Permite al usuario cambiar la calle del contacto ingresando una nueva.
"""

contactos = {"Luis": {"email": "luis@mail.com", "direccion": {"ciudad": "CDMX", "calle": "Reforma"}},
             "Pepe": {"email": "pepe@mail.com", "direccion": {"ciudad": "Puebla", "calle": "Constitullentes"}},
             "Saul": {"email": "saul@mail.com", "direccion": {"ciudad": "Toluca", "calle": "Emiliano Zapata"}},
             "Zara": {"email": "zara@mail.com", "direccion": {"ciudad": "Acapulco", "calle": "Las Cruces"}}}

nombre_contacto = input("Nombre contacto: ")

if nombre_contacto in contactos:
    print(f"{nombre_contacto} email: {contactos[nombre_contacto]['email']}")
    print(f"Direccion - Ciudad: {contactos[nombre_contacto]['direccion']['ciudad']} | Calle: {contactos[nombre_contacto]['direccion']['calle']}")
    
    cambiar_calle = input("Ingrese la nueva calle: ")
    
    contactos[nombre_contacto]['direccion']['calle'] = cambiar_calle
    
    print(f"Nueva direccion - Ciudad: {contactos[nombre_contacto]['direccion']['ciudad']} | Calle: {contactos[nombre_contacto]['direccion']['calle']}")
    
else:
    print("Contacto no encontrado.")
    
