"""
Reto: Agrupación de Inventario por Categoría
Aquí trabajarás con la transformación de una lista de objetos en un mapa categorizado.
    Crea una lista de diccionarios llamada productos. Cada diccionario tiene: nombre, precio y categoria.
        [{"nombre": "Teclado", "precio": 25, "categoria": "IT"}, {"nombre": "Monitor", "precio": 200, 
        "categoria": "IT"}, {"nombre": "Silla", "precio": 150, "categoria": "Muebles"}]
    Crea una función llamada agrupar_por_categoria(lista_productos).
    Misión: La función debe devolver un diccionario donde las llaves sean las categorías y el valor 
    sea una lista de nombres de los productos pertenecientes a esa categoría.
        Resultado esperado: {"IT": ["Teclado", "Monitor"], "Muebles": ["Silla"]}.
"""

def  agrupar_por_categoria(lista_productos):
    productos_cat = {}
    
    for producto in lista_productos:
        productos_cat[producto]["categoria"] = "nombre"
       
        if producto["categoria"] not in productos_cat:
            productos_cat["categoria"].append("categoria")
            
        
    return productos_cat    
        
productos = [{"nombre": "Teclado", "precio": 25, "categoria": "IT"}, 
             {"nombre": "Monitor", "precio": 200, "categoria": "IT"}, 
             {"nombre": "Silla", "precio": 150, "categoria": "Muebles"},
             {"nombre": "Mesa", "precio": 250, "categoria": "Muebles"},
             {"nombre": "Mouse", "precio": 10, "categoria": "IT"}]

nuevo_dicc = agrupar_por_categoria(productos)

print(nuevo_dicc)


"""
Nota
El Error: Escribiste productos_cat[producto]["categoria"] = "nombre". Aquí hay dos problemas:

    producto es un diccionario completo, y los diccionarios no pueden ser llaves de otros diccionarios 
    (porque son mutables).

    Intentaste acceder a una llave dentro de algo que aún no habías definido como diccionario.

La Lógica Correcta: Debes extraer el nombre de la categoría (que será tu llave) y el nombre del producto 
(que irá a la lista).
"""


