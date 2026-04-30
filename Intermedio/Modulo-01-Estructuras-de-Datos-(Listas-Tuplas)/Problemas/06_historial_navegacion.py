"""
Problema: El Historial de Navegación (Listas)
Este ejercicio simula el comportamiento del botón "Atrás" de un navegador.
    Crea una lista llamada historial que empiece con: ["google.com", "youtube.com", "github.com"].
    Lógica:
        El usuario visita una nueva página: "stackoverflow.com". Agrégala al final.
        El usuario presiona el botón "Atrás". Esto significa que debes eliminar el 
        último elemento de la lista y guardarlo en una variable llamada pagina_eliminada 
        (Investiga el método .pop() sin pasarle índice).
        Muestra un mensaje: "Saliste de [pagina_eliminada]. 
        Ahora estás en [ultimo_elemento_de_la_lista]".
    Muestra cuántas páginas quedan en el historial
"""

historial = ["google.com", "youtube.com", "github.com"]
historial.append("stackoverflow.com")
print(historial)


# Elimina el último y lo guarda en la variable al mismo tiempo
#pagina_eliminada = historial.pop()

pagina_eliminada = historial[-1]
print(f"Salieste de la pagina {pagina_eliminada}.")
historial.pop()

ultimo_elemento_lista = historial[-1]
print(f"Ahora estas en {ultimo_elemento_lista}.")

print("Quedan", len(historial), "paginas en el historial.")


