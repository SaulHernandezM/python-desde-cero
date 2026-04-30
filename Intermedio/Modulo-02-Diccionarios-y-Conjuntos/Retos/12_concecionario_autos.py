"""
Reto: El Concesionario de Autos (Anidación de Características)
Este reto te obligará a buscar datos específicos dentro de categorías.
    Crea un diccionario autos. Las llaves son marcas ("Toyota", "Ford"). El valor es otro diccionario 
    donde las llaves son modelos ("Corolla", "Mustang") y el valor es el año.
        autos = {"Toyota": {"Corolla": 2022, "Hilux": 2021}, "Ford": {"Mustang": 2023}}
    Misión:
        Pide al usuario una Marca.
        Si existe, muestra todos los modelos disponibles en esa marca.
        Luego, pide al usuario un Modelo específico de esa marca y muestra su año de fabricación.
"""

autos = {"Toyota": {"Corolla": 2022, "Hilux": 2021}, "Ford": {"Mustang": 2023}}

marca_auto = input("Marca de auto: ")

if marca_auto in autos:
    marca = autos[marca_auto]
    
    for modelo, año in marca.items():
        print(f"Modelos: {modelo}.")
    
else:
    print("Marca de auto no encontrada.")
    
    
modelo_especifico = input("Modelo Especifico: ")
    
if modelo_especifico in marca:
    
    for modelo, año in marca.items():
        print(f"Año: {año}.")
    
else:
    print("Modelo de auto no encontrado.")
        

        
        
    




