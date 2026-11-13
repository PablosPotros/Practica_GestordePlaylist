def menu():
    print("1: Agregar musica")
    print("2: Ver playlist")
    print("3: Buscar en la playlist")
    print("4: Eliminar de la playlist")
    print("5- Salir")

def agregar_musica():
    with open("playlist.txt", "w") as archivo:
        cantidadcanciones = int(input("¿Cuantas canciones?: "))
        for i in range(cantidadcanciones):
            nombre = input("Nombre de la canción: ")
            artista = input("Compositor: ")
            archivo.write(f"{nombre},{artista}\n")
            print("Agregada.\n")

def ver_playlist():
    with open("playlist.txt", "r") as archivo:
        print("\nCanciones registradas:")
        print(archivo.read())
        archivo.close()
        print("")

def buscar_en_playlist():
    busqueda = input("Musica buscada: ")
    encontrado = False
    with open("playlist.txt", "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            nombre = datos[0]
            artista = datos[1]
            
            if busqueda.lower() == nombre.lower():
                print("\n-Canción encontrada-")
                print("Nombre:", nombre, " | Artista: ", artista)
                print("")
                encontrado = True
                
            if encontrado == False:
                    print("No se encontro.\n")

def eliminar_en_playlist():
    elimencontrado = False
    elimbusqueda = input("Musica que quiere eliminar: ")
    canciones = []

    with open("playlist.txt", "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            nombre = datos[0]
            artista = datos[1]

            if elimbusqueda.lower() == nombre.lower():
                print("\n-Se quito de la playlist-")
                print("Nombre:", nombre, " | Artista: ", artista)
                print("")
                elimencontrado = True
            else:
                canciones.append(linea)

    if elimencontrado == False:
        print("No se encontro.\n")
    else:
        with open("playlist.txt", "w") as archivo:
            archivo.writelines(canciones)