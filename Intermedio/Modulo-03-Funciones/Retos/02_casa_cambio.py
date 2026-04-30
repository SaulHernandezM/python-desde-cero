"""
Reto: La Casa de Cambio (Diccionarios Anidados + Matemáticas)
Imagina que trabajas en una app de finanzas.
    Crea un diccionario llamado tasas_cambio donde las llaves sean la moneda (ej: "USD", "EUR") 
    y el valor sea el tipo de cambio respecto al Peso (ej: {"USD": 17.5, "EUR": 19.2}).
    Crea una función llamada convertir_a_pesos(moneda, cantidad, diccionario).
    Misión: La función debe:
        Buscar la moneda en el diccionario.
        Si existe, retornar la cantidad multiplicada por la tasa. (totalmx = cantidad * moneda)
        Si no existe, retornar el texto "Moneda no soportada".
Uso: Pide al usuario la moneda y la cantidad, y muestra cuánto dinero tiene en pesos.
"""

def convertir_a_pesos(moneda, cantidad, diccionario):
    if moneda in diccionario:
        total_mx = cantidad * diccionario[moneda]
        return total_mx
    else:
        return "Moneda no soportada"


tasas_cambio = {"USD": 17.3, "EUR": 19.2, "GBP": 23.9, "CAD": 13.1, "CHF": 22.6, "AUD": 12.3}

user_moneda = input("Moneda (USD, EUR,.., AUD): ")
user_cantidad = float(input("Cantidad: "))

user_convertir = convertir_a_pesos(user_moneda, user_cantidad, tasas_cambio)

print(f"Dinero en pesos: {user_convertir}.")
