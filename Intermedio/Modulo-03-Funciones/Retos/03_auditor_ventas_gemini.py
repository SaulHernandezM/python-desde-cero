def generar_reporte(lista_ventas, dict_precios):
    total_dinero = 0
    
    for articulo in lista_ventas:
        if articulo in dict_precios:
            total_dinero += dict_precios[articulo]
            
    # Creamos el diccionario resumen para el "jefe"
    resumen = {
        "total_dinero": total_dinero,
        "cantidad_articulos": len(lista_ventas)
    }
    return resumen

precios = {"Cafe": 30, "Galleta": 15, "Te": 25, "Pay": 60}
ventas_dia = ["Cafe", "Galleta", "Pay", "Cafe"] # Nota: El café se vendió dos veces

# Guardamos el resultado de la función en una variable
reporte_final = generar_reporte(ventas_dia, precios)

print(f"--- REPORTE DE CAJA ---")
print(f"Total recaudado: ${reporte_final['total_dinero']}")
print(f"Artículos vendidos: {reporte_final['cantidad_articulos']}")