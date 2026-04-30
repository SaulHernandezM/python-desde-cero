"""
Reto: El Organizador de Gastos (Agrupación)
Imagina que tienes una lista de gastos, pero quieres saber cuánto gastaste en total por cada categoría.
    Crea una lista de diccionarios llamada gastos.
        [{"item": "Cine", "monto": 150, "cat": "Ocio"}, {"item": "Tacos", "monto": 80, "cat": "Comida"}, 
        {"item": "Netflix", "monto": 200, "cat": "Ocio"}]
    Crea una función resumen_gastos(lista).
    Misión: La función debe retornar un diccionario donde las llaves sean las categorías y el valor sea 
    la suma total de dinero de esa categoría.
        Resultado esperado: {"Ocio": 350, "Comida": 80}.
    Pista: Si la categoría aún no existe en tu diccionario de resultados, agrégala con el monto. Si ya 
    existe, súmale el nuevo monto.
"""

def resumen_gastos(lista):
    totales = {}
    
    for gasto in lista:
        categoria = gasto["cat"]
        monto = gasto["monto"]
        
        # LÓGICA DE AGRUPACIÓN:
        if categoria in totales:
            # Si ya existe la categoría, le sumamos el nuevo monto
            totales[categoria] += monto
        else:
            # Si es la primera vez que la vemos, la creamos con ese monto
            totales[categoria] = monto
            
    return totales

# Prueba
gastos_mes = [
    {"item": "Cine", "monto": 150, "cat": "Ocio"},
    {"item": "Tacos", "monto": 80, "cat": "Comida"},
    {"item": "Netflix", "monto": 200, "cat": "Ocio"}
]

print(f"Resumen de gastos: {resumen_gastos(gastos_mes)}")