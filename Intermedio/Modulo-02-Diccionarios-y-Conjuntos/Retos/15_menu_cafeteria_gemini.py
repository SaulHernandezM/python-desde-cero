menu = {
    "Cafe": [{"item": "Espresso", "precio": 2.5}, {"item": "Latte", "precio": 3.5}],
    "Postre": [{"item": "Pastel", "precio": 10.5}, {"item": "Pay", "precio": 5.5}]
}

cat = input("Categoría: ")
if cat in menu:
    suma_precios = 0
    print(f"\n--- Menú de {cat} ---")
    
    for producto in menu[cat]:
        print(f"* {producto['item']}: ${producto['precio']}")
        suma_precios += producto['precio']
    
    promedio = suma_precios / len(menu[cat])
    print(f"\nEl precio promedio de esta sección es: ${promedio:.2f}")