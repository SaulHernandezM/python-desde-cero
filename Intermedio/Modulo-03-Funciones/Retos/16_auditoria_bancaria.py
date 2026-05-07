"""
Reto: Sistema de Auditoría Bancaria
Este reto pondrá a prueba tu capacidad para procesar listas de transacciones anidadas en diccionarios.
    Crea un diccionario clientes donde la llave es el ID del cliente y el valor es un diccionario con 
    nombre y transacciones (una lista de números, positivos para depósitos y negativos para retiros).
        {"C001": {"nombre": "Ana", "transacciones": [100, -50, 200]}, "C002": {"nombre": "Luis", 
        "transacciones": [-10, -20]}}
    Crea una función llamada auditar_cuentas(diccionario_clientes).
    Misión: La función debe retornar un nuevo diccionario que contenga únicamente a los clientes cuyo 
    saldo final sea negativo (deuda). 
    El valor del nuevo diccionario debe ser el saldo calculado.
    Fórmula: Saldo = Sumatoria(Transacciones)
    Expectativa: Si el saldo de Luis es -30, el resultado debe ser {"C002": -30}.
"""

def auditar_cuentas(diccionario_clientes):
    usuarios_saldo_negativo = {}
    usuarios_saldo_positivo = {}
    
    saldo = 0
    for id, usuario in diccionario_clientes.items():
        saldo = sum(usuario["transacciones"])
        if saldo < 0:
            usuarios_saldo_negativo[id] = saldo
        else:
            usuarios_saldo_positivo[id] = saldo
        
    return usuarios_saldo_negativo, usuarios_saldo_positivo


clientes = {"C001": {"nombre": "Ana", "transacciones": [100, -50, 200]}, 
            "C002": {"nombre": "Luis", "transacciones": [-10, -20]},
            "C003": {"nombre": "Maria", "transacciones": [-140, -220]},
            "C004": {"nombre": "Saul", "transacciones": [-110, 300]},
            "C005": {"nombre": "Pepe", "transacciones": [310, -230, 230]}}



negativo, positivo = auditar_cuentas(clientes)

print(f"Usuarios saldo negativo: {negativo}")
print(f"Usuarios saldo positivo: {positivo}")