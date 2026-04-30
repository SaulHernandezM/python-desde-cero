"""
Reto: El Detector de Suscriptores (Sets)
Este reto simula un análisis de marketing para dos plataformas de Streaming.
    Crea dos conjuntos: fans_netflix y fans_disney. Pon 5 nombres en cada uno 
    (asegúrate de que 2 nombres se repitan en ambos).
    Misión: El programa debe calcular y mostrar:
        Fieles de Netflix: Quiénes están en Netflix pero NO en Disney.
        Fans Premium: Quiénes están en ambas plataformas.
        Audiencia Total: Una lista única con todos los nombres de ambas plataformas sin repetir a nadie.
"""

fans_netflix = {"Saul", "Manuel", "Pepe", "Maria", "Samuel", "Alejandro", "Josue"}

fans_disney = {"Saul", "Manuel", "Carlos", "Ismael", "Samuel", "Axel", "Francisco"}

fieles_netflix = fans_netflix.difference(fans_disney)
fieles_disney = fans_disney.difference(fans_netflix)
print(f"Fieles Netflix: {fieles_netflix}.")
print(f"Fieles Disney: {fieles_disney}.")

fans_ambas = fans_netflix.intersection(fans_disney)
print(f"Fans Ambas Plataformas: {fans_ambas}.")

audiencia = fans_netflix.union(fans_disney)
fans = list(audiencia)

print(f"Audiencia total: {sorted(fans)}") 



