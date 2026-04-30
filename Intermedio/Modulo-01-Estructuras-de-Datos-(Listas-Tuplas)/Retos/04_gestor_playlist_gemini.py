playlist = ["Panda", "Rockstar", "Baila", "Ella baila sola", "Pieces", "Doomsday"]

while True:
    print("\n#### MENU PLAYLIST ####")
    print("1. Eliminar | 2. Mover | 3. Mostrar | 4. Salir")
    opcion = int(input("Opcion: "))

    if opcion == 1:
        nombre = input("Cancion a eliminar: ").strip()
        if nombre in playlist:
            playlist.remove(nombre)
            print(f"Eliminada: {nombre}")
        else:
            print("No se encontro la cancion.")

    elif opcion == 2:
        nombre = input("Cancion a mover: ").strip()
        if nombre in playlist:
            nueva_pos = int(input("Nueva posicion (1-n): ")) - 1
            playlist.remove(nombre)
            playlist.insert(nueva_pos, nombre)
            print("Movimiento exitoso.")
        else:
            print("No se encontro la cancion.")

    elif opcion == 3:
        # REINICIAMOS EL CONTADOR AQUÍ
        contador = 0 
        print("\n--- Tu Playlist ---")
        for cancion in playlist:
            contador += 1
            print(f"{contador}. {cancion}")
    
    elif opcion == 4:
        break