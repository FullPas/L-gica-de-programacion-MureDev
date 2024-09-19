"""
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
"""
#### El concepto de clase, es un pilar basicamente. lOS OBJETOS SON ENTIDADES CON UNAS CARACTERÍSTICAS

class Programador:

    surname_2: str = None                                                           # OTRA FORMA DE AÑADIR UN ATRIBUTO DE FORMA EXTERNA. Le añadimos un valor ( aunque sea None {ninguno} porque sino, no detecta que hay atributo inicializado y dará error)

    def __init__(self, name: str, surname: str, age: int, lenguage: list):          # Init es una función inicializadora que define los valores iniciales de nuestra clase, nuestro objeto, que recibe SELF (funcion reservada del sistema) que es el propio objeto
        self.name = name
        self.surname = surname
        self.age = age
        self.lenguage = lenguage
        
                                                                    # Funcion que imprime los parámetros anteriores
    def print(self):
        print(f"Nombre: {self.name} |Apellido_1: {self.surname} |Apellido_2: {self.surname_2}  | Edad: {self.age} | Lenguaje {self.lenguage}")

                                                                    # Ahora como interactuamos con Programador? Instanciando la clase (crear el objeto)

                                                                    # Creamos programador con los datos que nos pide la función
mi_programador = Programador("brais","March", 36, ["Python", "Kolin", "Swift"])
                                                                    # Ahora podemos acceder a programador y podemos llamar a la función print.
mi_programador.print()                                              # Con print, llamamos a la funcion PRINT
mi_programador.age = 38
mi_programador.print()
mi_programador.surname_2 = "Meri"
mi_programador.print()

### EXTRA

# LIFO
class stack:                                # Al crear una clase, no nos tenemos que preocupar que va a hacer un atributo "push por ejemplo". Nosotros sabemos cual es la lógica, dejamos que sea la clase que se encargue de aplicarla ( LIFO, FIFO....)

    def __init__(self):
        self.stack = []
                                            # Todas las funciones deben llamarse a sí mísmas para interactuar con la clase.
    def push(self, item):                   # Le añadimos "item" porque queremos que nos añada elementos... con implementación abierta. no le vamos a decir si es STR, ni INT, ni ningún tipo de dato. en el caso de especificarle un tipo, sería "item: str"           
        self.stack.append(item)         # Accedemos a append y le pasamos "item"
    def pop(self):
        if self.count() == 0:           # Aquí reaprovechamos código, ya que podríamos escribir: if len(self.stack) == 0, pero no tiene sentido. Ya llamamos directamente a Count.
            return None                 # Con ésta condición, le decimos que si la lista está vacía, nos devuelva que no hay nada.
        return self.stack.pop()         # Aquí ya le explicamos que elimine el elemento de la lísta según la lógica que deba la clase aplicar.
        
    def count(self):                        # Si queremos que nos retorne la lista, deberemos hacer lo siguiente:
        return len(self.stack)          # Nos devuelve la longitud d ela lista, que inicialmente, será 0.
    def print(self):                        # Para imprimir, la mejor opción es que recorra todos los elementos de la lista. Así que lo haremos con un FOR.
        for item in self.stack:         # Por cada elemento d ela lista.....
            print(item)                 # Imprimeme el item que corresponda.
                                            # HASTA AQUÍ HEMOS DEFINIDO STACK (pila). AHORA, SI QUEREMOS USAR LA CLASE....
my_stack = stack()
                                            # LE DAMOS DATOS CON LOS QUE TRABAJAR:
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
my_stack.push("D")
                                            # Ahora quiero contar los elementos.
print (my_stack.count())                    # Print nos dejará ver que vale ese Count.
my_stack.print()
my_stack.pop()                              #Ahora desapilemos...
print (my_stack.count())
my_stack.pop()                              #print (my_stack.pop()) Veríamos como desapila C
my_stack.pop()                              #print (my_stack.pop()) Veríamos como desapila B
my_stack.pop()                              #print (my_stack.pop()) Veríamos como desapila A
my_stack.pop()                              #print (my_stack.pop()) Nos dirá que ya no tiene elementos que desapilar "None"
print (my_stack.count())                    #Nos da valor 0

#FIFO

class Queue:

    def __init__(self):
        self.queue = []
    def equeue(self, item ):
        self.queue.append(item)
    def dequeue(self):
        if self.count() == 0:           # Aquí reaprovechamos código, ya que podríamos escribir: if len(self.stack) == 0, pero no tiene sentido. Ya llamamos directamente a Count.
            return None                 # Con ésta condición, le decimos que si la lista está vacía, nos devuelva que no hay nada.
        return self.queue.pop()
    def count(self):                        # Si queremos que nos retorne la lista, deberemos hacer lo siguiente:
        return len(self.queue)          # Nos devuelve la longitud d ela lista, que inicialmente, será 0.
    def print(self):                        # Para imprimir, la mejor opción es que recorra todos los elementos de la lista. Así que lo haremos con un FOR.
        for item in self.queue:         # Por cada elemento d ela lista.....
            print(item)

my_queue = Queue()
my_queue.equeue("A")
my_queue.equeue("B")
my_queue.equeue("C")
print (my_queue.count())
my_queue.print()

my_queue.dequeue()
print  (my_queue.count())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue()) 
print(my_queue.dequeue())                              
print  (my_queue.count())