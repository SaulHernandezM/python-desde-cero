"""
Reto: El Analizador de Contactos Duplicados (Sets + Dics)
Imagina que estás uniendo las agendas de dos teléfonos y quieres limpiar el desorden.
    Crea un diccionario llamado agenda_trabajo con 3 nombres y sus correos.
    Crea otro llamado agenda_personal con 3 nombres y sus correos (asegúrate de que un nombre
    y correo se repita en ambos).
    Misión:
        Obtén todos los nombres de ambas agendas.
        Usa un Conjunto (Set) para crear una lista única de nombres sin duplicados.
        Muestra cuántos contactos únicos tienes en total.
"""

agenda_trabajo = {"Saul": "saul@gmail.com", "Samuel": "samuel@gmail.com", "Said": "said@gmail.com",
                "Sara": "sara@gmail.com", "Sasha": "sasha@gmail.com", "Sam": "sam@gmail.com"}


agenda_personal = {"Saul": "saul@gmail.com", "Samanta": "samanta@gmail.com", "Said": "said@gmail.com",
                "Sabrina": "sabrina@gmail.com", "Sasha": "sasha@gmail.com", "Sam": "sam@gmail.com"}


agenda_trabajo_key = agenda_trabajo.keys()
agenda_personal_key = agenda_personal.keys()

agend_trabajo_list = list(agenda_trabajo_key)
agenda_personal_list = list(agenda_personal_key)

"""
Hiciste bien en extraer las llaves con .keys(). El problema es que las llaves por sí solas no son "Sets" 
automáticos (son objetos dict_keys).
La solución: Debes envolverlos en la función set() para poder usar union o intersection.
Pro-tip: En Python, puedes usar el símbolo | para unir conjuntos de forma más rápida.
"""
