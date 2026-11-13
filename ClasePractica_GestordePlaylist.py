import GestordePlaylist_funciones

while True:
    GestordePlaylist_funciones.menu()
    opcion = int(input("Opción: "))
    if opcion == 1:
        GestordePlaylist_funciones.agregar_musica()
    
    elif opcion == 2:
        GestordePlaylist_funciones.ver_playlist()

    elif opcion == 3:
        GestordePlaylist_funciones.buscar_en_playlist()

    elif opcion == 4:
        GestordePlaylist_funciones.eliminar_en_playlist()

    elif opcion == 5:
        print("Cerrando gestor.")
        break