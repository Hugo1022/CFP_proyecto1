peliculas = "peliculas.txt"
usuarios = "usuarios.txt"

def validarBusqueda(txt, valor):
    with open(f"{txt}", "r") as archivo:
        lineas = archivo.readlines()
        cont = 0
        for i in lineas:
            i2 = i.split(",")
            if i2[0] == str(valor):
                cont += 1
                return (True,i2,lineas.index(i))
        if cont == 0:
            return (False,0)

def alquilarPelicula():
    dni = int(input("ingrese su dni."))
    codigo = int(input("por favor ingrese el codigo de la pelicula"))
    validacion = validarBusqueda(peliculas, codigo)
    if validacion[0] == True:
        cont = 0
        for i in validacion[1]:
            if i == "L":
                index = validacion[1].index(i)
                validacion[1][index] = "A"
                validacion[1][index+1] = str(dni)
                cont += 1
                with open(f"{peliculas}", "r") as archivo:
                    lineas = archivo.readlines()
                    lineas[validacion[2]] = ",".join(validacion[1])
                    with open(f"{peliculas}", "w") as archivo2:
                        for i in lineas:
                            archivo2.write(i)
        if cont == 0:
            print("La pelicula ya esta alquilada")

def devolverPelicula():
    codigo = int(input("por favor ingrese el codigo de la pelicula"))
    validacion = validarBusqueda(peliculas, codigo)
    if validacion[0] == True:
        cont = 0
        for i in validacion[1]:
            if i == "A":
                index = validacion[1].index(i)
                validacion[1][index] = "L"
                validacion[1][index+1] = " "
                cont += 1
                with open(f"{peliculas}", "r") as archivo:
                    lineas = archivo.readlines()
                    lineas[validacion[2]] = ",".join(validacion[1])
                    with open(f"{peliculas}", "w") as archivo2:
                        for i in lineas:
                            archivo2.write(i)
        if cont == 0:
            print("La pelicula no esta alquilada")

def verDisponibles():
    with open(f"{peliculas}", "r") as archivo:
        lineas = archivo.readlines()
        for i in lineas:
            i2 = i.split(",")
            for j in i2:
                if j == "L":
                    print(i[0:-2])

def verTodas():
    with open(f"{peliculas}", "r") as archivo:
        lineas = archivo.readlines()
        for i in lineas:
            print(i[0:-2])

def crearUser():
    dni = int(input("ingrese su dni."))
    validacion = validarBusqueda(usuarios, dni)
    if validacion[0] == False:
        name = str(input("ingrese su nombre"))
        direc = input("ingrese su direccion")
        tel = int(input("ingrese su telefono"))
        usuario = f"{str(dni)},{name},{direc},{str(tel)},L, \n"
        with open(f"{usuarios}","r+") as archivo:
            lineas = archivo.readlines()
            archivo.write(usuario)
    else:
        print("el usuario ya existe")

def modificarUser():
    dni = int(input("ingrese su dni."))
    validacion = validarBusqueda(usuarios, dni)
    if validacion[0] == True:
        opcion = int(input("ingrese 1 para modificar su direc o 2 para modificar su tel"))
        if opcion == 1:
            validacion[1][2] = input("ingrese su nueva direccion")
        elif opcion == 2:
            validacion[1][3] = input("ingrese su nuevo telefono")
        else:
                    print("elija una opcion correcta")
        with open(f"{usuarios}", "r") as archivo:
            lineas = archivo.readlines()
            lineas[validacion[2]] = ",".join(validacion[1])
            with open(f"{usuarios}", "w") as archivo2:
                for i in lineas:
                    archivo2.write(i)
    else:
        print("el usuario no existe")

def eliminarUser():
    dni = int(input("ingrese su dni."))
    validacion = validarBusqueda(usuarios, dni)
    if validacion[0] == True:
        with open(f"{usuarios}","r") as archivo:
            lineas = archivo.readlines()
            lineas.pop(validacion[2])
            with open(f"{usuarios}", "w") as archivo2:
                for i in lineas:
                    archivo2.write(i)
    else:
        print("el usuario no existe")