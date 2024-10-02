"""
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 * 
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
"""

#Lo primero que deberemos hacer es IMPORTAR la librería OS que nos descarga operaciones que nos permitan interactuar con el sistema operativo.

import os

file_name = "noredev.txt"

with open(file_name, "w") as file:# Con With  le decimos que nos habra el fichero y lo asocie a una variable que hemos llamado "file"con permisos de escritura
    file.write("Brais Moure\n")
    file.write("36\n")
    file.write("Python\n")

with open(file_name, "r") as file:
    print(file.read())

# os.remove(file_name)    #Elimina el fichero.

#Extra
open(file_name, "w")
file_name = "noredev_shop.txt"

while True:
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actuañizar producto")
    print("4. Borrar producto")
    print("5. Mostrar productos")
    print("6. Calcular venta total")
    print("7. Calcular venta por producto")
    print("8. Salir")

    option = input("Selecciona una opción")

    if option == "1":
        name = input("Nombre: ")
        quantity = input ("Cantidad: ")
        price = input ("Precio: ")
        with open(file_name, "a") as file:
            file.write(f"{name}, {quantity}, {price}\n")
            
    elif option == "2":
        name = input ("Nombre: ")
        with open(file_name, "r") as file:  #Abrimos fichero
            for line in file.readlines():
                #Si el primer elemento del producto es = al nombre que yo estoy buscando "name", entonces:
                if line.split(", ")[0] == name:                                                             #Split es para hacer una subdivision. Al hacer el split por comas, nos quedamos con el elemento "0"
                    #Imprimimos la linea completa.
                    print(line)
                    break
                    # Si se encuentra el nombre, lo guardamos
    elif option == "3": #Que queremos actualizar? una linea en concreto, para ello:
        name = input("Nombre: ")
        quantity = input ("Cantidad: ")
        price = input ("Precio: ")
                        # tenemos que buscar en el fichero la linea a actualizar
        with open(file_name, "r") as file:  #Abrimos fichero en modo lectura
            lines = file.readlines()        #Leemos todas las lineas y las guardamos en una variable que luego usaremos abajo.
        #OJO PORQUE ESCRITO ASÍ LAS LINEAS SIGUIENTES, LO QUE HACES ES CARGARTE EL ARCHIVO CON "w", HAY QUE ABRIR ANTES EL FICHERO EN MODO LECTURA Y GUARDARLO EN UNA VARIABLE
        with open(file_name, "w") as file:  #Abrimos fichero en modo escritura
            #Cual es la linea que coincide con el nombre que yo quiero actualizar?
            for line in lines:
                if line.split(", ")[0] == name:                                             # Si existe, meto mis nuevos datos ( con la siguiente linea)
                    file.write(f"{name}, {quantity}, {price}\n")                            # Si se encuentra el nombre, lo guardamos
                else:                                                                       # Si no existe...
                    file.write(line)
    
    elif option == "4":
        name = input ("Nombre: ")           #Preguntamos el nombre del producto que queremos borrar
        with open(file_name, "r") as file:  #Abrimos fichero en modo lectura
            lines = file.readlines()        #Leemos todas las lineas y las guardamos en una variable que luego usaremos abajo.
        #OJO PORQUE ESCRITO ASÍ LAS LINEAS SIGUIENTES, LO QUE HACES ES CARGARTE EL ARCHIVO CON "w", HAY QUE ABRIR ANTES EL FICHERO EN MODO LECTURA Y GUARDARLO EN UNA VARIABLE
        with open(file_name, "w") as file:  #Abrimos fichero en modo escritura
            #Cual es la linea que coincide con el nombre que yo quiero actualizar?
            for line in lines:
                if line.split(", ")[0] != name:                                             # Si no coincide con el nombre, lo queremos mantener
                    file.write(line)
    elif option == "5":
      with open(file_name, "r") as file: 
          print(file.read()) 
    elif option == "6":
        total = 0                                                                           #Inicializamos "Ventas totales" a 0.
        with open(file_name, "r") as file:
            for line in file.readlines():              #En cada una de éstas lineas hay que quedarse con la cantidad y con el precio.
                #Como accedemos a la canidad y al precio? accediendo primero al nombre con SPLIT
                components = line.split(", ")           #Queremos generar el array de componentes.
                quantity =  int (components[1])
                price =     float (components[2])
                total += quantity * price
        print(total)

    elif option == "7":
        name = input ("Nombre: ")
        total = 0                                                                           #Inicializamos "Ventas totales" a 0.
        with open(file_name, "r") as file:
            for line in file.readlines():              #En cada una de éstas lineas hay que quedarse con la cantidad y con el precio.
                #Como accedemos a la canidad y al precio? accediendo primero al nombre con SPLIT
                components = line.split(", ")          #Queremos generar el array de componentes.
                if components[0] == name:
                    quantity =  int (components[1])
                    price =     float (components[2])
                    total += quantity * price
                    break
        print(total)
    elif option == "8":
        os.remove(file_name)
        break
    else:
        print ("Introduce una opción correcta de las disponibles.")
