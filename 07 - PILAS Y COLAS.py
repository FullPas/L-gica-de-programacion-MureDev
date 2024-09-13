"""
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
"""

#Stack (LIFO) "El Último en entrar, el primero en salir"

stack  = []
#Elementos push
stack.append("1")                #Ésto es un String, pero puede ser un INT si se desea.
stack.append("2")
stack.append("3")

print (stack)

#Elementos pop
stack_items = stack[len(stack) -1]#usaremos LEN para acceder a la longitud de la lista. como nos dirá que hay 3 elementos en la lista, y queremos acceder al elemento 2, tendrermos que decirle, "accede a todos los elementos de la lista, -1"
                                  #Luego lo meteremos en una variable para usarla, he imprimirla.
del stack[len(stack) -1]          #Desapilamos el elmento índice que hemos apilado, en éste caso, el último elemento añadido.
print(stack_items)

print (stack.pop())               #Pop es un elemento nativo del lenguaje que hace de forma automática el desapilamiento del último elemento de la lista.
print(stack)

#Queue (FIFO) "El primero en entrar, el primero en salir"

queue = []

queue.append("1")
queue.append("2")
queue.append("3")
print(queue)

queue_items = queue[0]          #Accedemos al elemento 0 de la lista
del queue [0]                   #LE pedimos que elimine ese elemento
print(queue_items)

print(queue.pop(0))             #Le decimos que desencole accediendo al elemento 0 de la lista.
print(queue)

###EXTRA 1

#creamos una función
def web_navigator ():

    stack = []                  #Aquí se almacenará "las webs" por las que naveguemos, cada página que accedamos y luego retrocedamos.
    while True:                 #Entra en bucle infinito preguntando al usuario que añada o interaccione alante o atrás, hasta que le dé salir y se rompa el programa.
    
        action = input("Añade una url o interacciona con las palabras adelante/atrás: ")
                                #Ahora tenemos que exponer los diferentes casos que vamos a tener "introducir", "alante", "atrás", "salir" con una condición.
        if action == "salir":
            print("Saliendo . . .")
            break       
        elif action == "adelante":#Cómo una web funciona como una lista y NO como una pila, la fnción "adelante" purámente con Stack, no se puede hacer. habría que usar otro método ( que no especifica en el video)
            pass
        elif action == "atras":
            stack.pop()
        else:                   #Entrará en "ELSE" si el usuario no escribe ni salir, adelante, atrás.
            stack.append(action)
                                #Para poner un límite en la acción "atras" hay que añadir una condición extra:
        #Hemos pasado de:
            #print (stack[len(stack) -1])
        #a:
        if len(stack) > 0:
            print (f"Has navegado a: {stack[len(stack) -1]}")
        else:
            print("Estás en la página de inicio.")

                                ###CON ÉSTO CONSEGUIMOS QUE EL STACK AÑADA UN ELEMENTO Y PRINTEEMOS EL ÚLTIMO ELEMENTO AÑADIDO###

#llamamos a la función
web_navigator()

###EXTRA 2

def shared_printed():

    while True:               
        action = input("Añade un documento a imprimir: ")

        if action == "salir":
            print("Saliendo . . .")
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"imprimiento el archivo {queue.pop(0)}")
                print("La cola de impresión está vacía.")
        else:                                                   #Te muestra lo que has añadido
            queue.append(action)
        print(f"Cola de impresión: {queue}")


shared_printed()










"""
Buenas tardes:
Después de 1 y 5 meses de uso de un portatil que compré por medio de la empresa PC Componentes, en el que realmente tendrá menos de 
"""