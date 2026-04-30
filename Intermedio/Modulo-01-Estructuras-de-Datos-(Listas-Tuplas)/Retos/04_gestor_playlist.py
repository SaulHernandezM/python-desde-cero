"""
Reto: El Gestor de Playlist (Listas)
Este reto simula una aplicación de música como Spotify.
    Crea una lista llamada playlist con 4 canciones.
    Requerimientos:
        El usuario puede elegir "Eliminar canción". El programa debe pedir el nombre. 
        Si está, la elimina; si no, avisa del error.
        El usuario puede elegir "Mover canción". Debe pedir el nombre de la canción y 
        la nueva posición (índice) donde la quiere poner.
        Pista: Para mover, primero la eliminas con .remove() y luego la insertas con 
        .insert(indice, valor).
    Muestra la playlist numerada al final (puedes usar un contador en el for).
"""

playlist = ["Panda", "Rockstar", "Baila", "Ella baila sola", "Pieces", "Doomsday"]
contador = 0


while True:
    print("#### Playlist ####")
    print("Elije una opcion: ")
    print("1. Eliminar cancion.")
    print("2. Mover cancion.")
    print("3. Mostrar playlist.")
    print("4. Salir.")
    opcion = int(input("Opcion: "))
    
    if opcion == 1:
        cancion_nombre = input("Nombre de la cancion: ").strip()
        
        for cancion in playlist:
            if cancion_nombre in playlist:
                playlist.remove(cancion_nombre)
                print(f"Cancion: {cancion_nombre} eliminada de la playlist.")
                break
            else:
                print("Cancion no encontrada en la playlist.")
                break

    if opcion == 2:
        cancion_nombre = input("Nombre de la cancion: ").strip()
        posicion_cancion = int(input("Posicion (1 - n): "))
        posicion_cancion -= 1
        
        for cancion in playlist:
            if cancion_nombre in playlist:
                playlist.remove(cancion_nombre)
                playlist.insert(posicion_cancion, cancion_nombre)
                print(f"Cancion {cancion_nombre} movida a la posicion {posicion_cancion + 1}.")
                break
            else:
                print("Cancion no encontrada en la playlist.")
                break  
    
    if opcion == 3:
        for cancion in playlist:      
            contador += 1
            print(f"{contador}. {cancion} ")
    
    if opcion == 4:
        print("Adios.")
        break
