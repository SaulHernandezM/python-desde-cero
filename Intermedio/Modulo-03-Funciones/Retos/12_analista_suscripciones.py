"""
Reto: El Analista de suscripciones (Sets + Dics)
Imagina que tienes dos servicios de streaming y quieres saber qué usuarios están desperdiciando 
dinero en ambos.
    Crea un diccionario servicios donde las llaves sean "Netflix" y "Disney", y los valores sean 
    Sets con los nombres de los suscriptores.
    Crea una función llamada analizar_usuarios(dicc_servicios).
    Misión: La función debe devolver un nuevo diccionario con tres llaves:
        "ambos": Un set con los nombres de quienes están en los dos.
        "solo_netflix": Quienes están en Netflix pero no en Disney.
        "total_unicos": La cantidad total (entero) de personas únicas en la plataforma.
    Pista: Repasa las operaciones de conjuntos: intersection, difference y union.
"""

def  analizar_usuarios(dicc_servicios):
    nuevo_dicc = {"ambos": [],
                  "solo_netflix": [],
                  "total_unicos": []}
    
    
    ambos = dicc_servicios["Netflix"].intersection(dicc_servicios["Disney"])
    nuevo_dicc["ambos"].append(ambos)
    
    solo_netflix = dicc_servicios["Netflix"].difference(dicc_servicios["Disney"])
    nuevo_dicc["solo_netflix"].append(solo_netflix)
    
    total_unicos = len(solo_netflix)
    nuevo_dicc["total_unicos"].append(total_unicos)
    
    return nuevo_dicc 
        
    

servicios = {"Netflix": {"Saul", "Samuel", "Said", "Jose", "Manuel", "Maria"},
             "Disney": {"Saul", "Maria", "Samuel"}}


print(f"Usuarios en ambos servicios: {analizar_usuarios(servicios)["ambos"]}")
print(f"Usuarios solo en Netflix: {analizar_usuarios(servicios)["solo_netflix"]}")
print(f"Total de usuarios: {analizar_usuarios(servicios)["total_unicos"]}")



"""
Notas
Acierto: El uso de .intersection() y .difference() es correcto.

Error de lógica (Total únicos): Calculaste total_unicos basándote solo en solo_netflix. La definición 
de "total de personas únicas" en ambas plataformas requiere la unión (.union()).

Error de estructura: Inicializaste nuevo_dicc con listas vacías y luego hiciste .append(set). Esto crea 
una lista que contiene un conjunto adentro [{'User1'}], en lugar de que el valor sea directamente el 
conjunto o la cantidad.

Eficiencia: Llamaste a la función 3 veces en los print. En producción, esto multiplicaría el tiempo de 
ejecución innecesariamente. Es mejor guardar el resultado en una variable.
"""