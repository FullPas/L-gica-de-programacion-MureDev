"""
* EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
"""

"""
#ESTRUCTURAS: Nos sirven para organizar datos.
####LISTAS### (Estructura para guardar varios elementos de forma ordenada. Que en Python no es lo mismo que las Array.)

my_list = ["Pascual", "Julián", "Sergio", "Damian"]
print(my_list)
#Para añadir
my_list.append("Juan")
print(my_list)
#Para actualizar
my_list[0] = "Pascu"
#Para borrar
my_list.remove("Juan")
print(my_list)
#Para ordenar
my_list.sort()
print(my_list)

###TUPLAS### (Es un tipo de estructura inmutable, es decir, una vez está creda, no se puede modificar, actualizar, eliminar...solo tienes  operación de acceso.)

my_tuple: tuple = ("Maria", "Olga", "Sandra", "Marina", "38")
print(my_tuple[2]) 

#Función "SORTED" nos devuelve una lista. no funciona con distintos tipos de datos, por eje: un INT con STR.

my_tuple = sorted(my_tuple) #Reconviertes una tupla en una lista ordenada
my_tuple = tuple(sorted(my_tuple))# Y con ésto lo volvemos a reconvertir a Tupla.
print(my_tuple) #Print de la primera linea con sorted
print(type(my_tuple))

###SETS### (Estructura desordenada. no te puedes fiar en la posición en la que guarda un elemento. Muy util para guardar (insertar), recorrer muchos datos, eliminar, pero no sirve para buscarlos)
my_set = {"Maria", "Olga", "Sandra", "Marina", "38"}
print (my_set) #El resultado te lo da completamente aleatorio.
my_set.add("correo@hotmail.com")
print (my_set)

        ####APUNTE ------------------------------------------------------------------------------------------------------------------------------------------------------
            #Así como en las listas puedes meter datos duplicados ( por ejemplo dos veces el mismo nombre) en los SET, no. no permite que los datos se dupliquen.
            #Se puede actualizar un SET, pero no es como la lista. En la lista, actualizas un elemento concreto. aquí eso no se puede. directamente actualizas todo el SET.

###DICCIONARIOS###
my_dict = {"nombre":"Pascual", "apellido1":"March", "edad":"38"}

print(my_dict["nombre"])            #acceso
my_dict["email"] = "correo@msn.com" #Inserción
my_dict["edad"] = "37"              #actualización
del my_dict["apellido1"]            @Borrar
print(my_dict)
"""
#EJERCICIO EXTRA:


def programa ():

    agenda = {}

    def insertar_contacto():
        telefono = input ("Introduce el telefono del contacto nuevo o a actualizar: ")
        if telefono.isdigit() and len(telefono) > 0 and len(telefono) <=11:
            agenda[nombre] = telefono
        else:
            print("Lo siento. No reconozco la entrada que has escrito. Debes introducir solo numeros con un máximo de 11 dígitos. Prueba otra vez")

    #Como queremos que tras elegir una opción, el programa no se salga, sino que vuelva aotra vez a preguntarte que opción quieres, meteremos toda la lógica dentro de un While.
    #Le decimos que es "TRUE" porque siempre va a ser verdadera. Para romper el programa, en el Caso 5, introducimos un Break.
    while True:

        print ("")
        print ("1) Insertar")
        print ("2) Buscar")
        print ("3) Actualizar")
        print ("4) Eliminar")
        print ("5) Listar toda la agenda")
        print ("6) Salir")

        opcion = input("\nIntroduce una opción: ")
        #Como solo queremos revisar las opciones de UNA SOLA VARIABLE, usaremos MATCH (swich en otros lenguajes.) 
        #Si tuvieramos condiciones complejas procesando valores de diferentes variables, usaríamos "IF, ELIF, ELSE"
        match opcion:
            case "1":
                nombre = input ("Introduce el nombre del contacto.")
                insertar_contacto()
                print (f"Perfecto, gracias. {nombre} se ha añadido correctamente.")
                print ("Que quieres hacer ahora?")
                pass
            
            case "2":
                nombre = input("Introduce el nombre del contacto a buscar: ")
                if nombre in agenda:
                    print (f"El número de teléfono de {nombre} es: {agenda[nombre]}")
                else:
                    print(f"El contacto con nombre: {nombre}, no existe, por favor vuelve a introducir un nombre válido.")
                pass
            
            case "3":
                nombre = input("Introduce el nombre del contacto a actualizar: ")
                if nombre in agenda:
                    insertar_contacto()
                    print (f"Perfecto, gracias. {nombre} se ha actualizado correctamente.")
                    print ("Que quieres hacer ahora?")
                else:
                    print(f"El contacto con nombre: {nombre}, no existe, por favor vuelve a introducir un nombre válido.")
                pass

            case "4":
                nombre = input("Introduce el nombre del contacto a eliminar: ")
                if nombre in agenda:
                    del agenda[nombre]
                    print ("El numero de teléfono de {nombre} se ha eliminado")
                else:
                    print(f"El contacto con nombre: {nombre}, no existe, por favor vuelve a introducir un nombre válido.")
                pass
            case "5":
                for i in agenda:
                    print(i)
                pass
            case "6":
                print("Has salido del programa. ¡HASTA LA PRÓXIMA!")
                break
            case _:#Caso por defecto. Si el usuario introduce cualquier otro valor, que le salte éste mensaje.
                print("El valor introducido no es válido, por favor, elige una opción del 1 al 5.")
programa()



