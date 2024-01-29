menuPrincipal = "Por favor ingrese una opcion:\n1.Menu Usuario.\n2.Menu Pelicula/Video.\n3.Salir.\n"
menuUsuario = "Ingrese una opcion:\n1.Crear usuario.\n2.Modificar datos.\n3.Eliminar usuario.\n4.Atras.\n"
menuPelicula = "Ingrese una opcion:\n1.Ver pelis disponibles.\n2.Alquilar peli.\n3.Devolver peli.\n4.Atras.\n"

def saludar():
    print("Bienvenido a la app de peliculas/videos")

def despedir():
    print("Gracias por utilizar la app de peliculas/videos")

def imprimirMenu(texto):
    opcion = int(input(f"{texto}"))
    return opcion