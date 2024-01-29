import functions as f
import messages as m

def menuPrincipal():
    m.saludar()
    on = 1
    while on == 1:
        on = 0
        opcion = m.imprimirMenu(m.menuPrincipal)
        if opcion == 1: 
            menuUser()
        elif opcion == 2:
            menuPelicula()
        elif opcion == 3:
            m.despedir()
            quit()
        else:
            print("ingrese una opcion correcta.")
            on = 1

def menuUser():
    on = 1
    while on == 1:
        on = 0
        opcion = m.imprimirMenu(m.menuUsuario)
        if opcion == 1:
            f.crearUser()
            menuUser()
        if opcion == 2: 
            f.modificarUser()
            menuUser()
        elif opcion == 3:
            f.eliminarUser()
            menuPrincipal()
        elif opcion == 4:
            menuPrincipal()
        else:
            print("ingrese una opcion correcta.")
            on = 1

def menuPelicula():
    on = 1
    while on == 1:
        on = 0
        opcion = m.imprimirMenu(m.menuPelicula)
        if opcion == 1: 
            f.verDisponibles()
            menuPelicula()
        elif opcion == 2:
            f.alquilarPelicula()
        elif opcion == 3:
            f.devolverPelicula()
        elif opcion == 4:
            menuPrincipal()
        else:
            print("ingrese una opcion correcta.")
            on = 1