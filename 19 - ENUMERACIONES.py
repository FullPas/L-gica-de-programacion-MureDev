"""
* EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un pequeño sistema de gestión del estado de pedidos.
 * Implementa una clase que defina un pedido con las siguientes características:
 * - El pedido tiene un identificador y un estado.
 * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 * - Implementa las funciones que sirvan para modificar el estado:
 *   - Pedido enviado
 *   - Pedido cancelado
 *   - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 * - Implementa una función para mostrar un texto descriptivo según el estado actual.
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
"""
"""Enumeraciones o ENUM, es un tipo de dato que consiste en un conjunto de constantes nombradas. Es una estructura que nos sirve, 
mediante ese conjunto (que está limitado de valores, los podemos identificar por nombres) va ha hacer que nuestro 
código va a ser más legible, más seguro ( ya que esa estructura nos va a delimitar cuales cson los vales con los 
que podemos trabajar). Es muchísimo más facil creando código seguro acotando el rango de actuacion de nuestro programa."""

#Como creamos un _ENUM en Python? hay que crear una clase.

"""
Supongamos que tenemos una empresa que trabajamos 4 días de la semana y queremos dejar a un usuario que escoja 
su día libre de L a V en un desplegable de la app.
Podríamos crear una lista para ello. Pero y que pasa si; ¿Queremos trabajar a lo largo d ela aplicación con un
dato tipado, acotado? Pues que se podrían perder esos valores a lo largo d ela app, alguien podría no saber que 
és...
Entonces... si le decimos al programa que si tiene que trabajar con días d ela semana, no trabajes con ID's, con 
Nombres.. Trabaja con dato de tipo Weekday. De ésta forma, nos restamos asegurando que si trabajamos con un dato de tipo Wekkday
eso solo va a poder tener los días de la  semana, que solo van a tener estos identificadores.
De ésta forma lo tenemos como más "cerrado" / "encapsulado" y una forma más segura de trabajar con éstos datos.
"""

from enum import Enum

class Weekday(Enum):         #Le estamos diciendo que está heredando del comportamiento de ENUM.
#Ahora hay que definir cuales son los valores que tiene este enumerado. En éste caso, creando los días de la semana
# y definir una constante (Weekday) que va a tener los valores de los días de la semana y a parte le tenemos que asiciar
# a cada día de la semana, un identificador.

    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
#Ahora mostramos el día (nombre) según el número entero utilizado para su identificador

def get_day(number: int):
    #para mostrar el nombre, de alguna manera, tendremos que hacer un print.
    #Y, en base al identificador que me pasen, ¿cómo voy a ser capaz de convertirlo en un dato de tipo Weekday, con el identificador que le pasremos "number?
    print(Weekday(number).name) #Con .name recuperamos solo el nombre, sin él, saldrá "Weekday.MONDAY". Con .Value, recuperaremos el valor.
    #Vamos a lanzar nuestro programa  y le pasamos un identificador...
get_day(1)

#Extra

 # Crea un pequeño sistema de gestión del estado de pedidos.
 # Implementa una clase que defina un pedido con las siguientes características:
class OrderStatus(Enum):
    # El pedido tiene un identificador y un estado.
    # El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELLED = 4

class Order: #Implemento una clase que defina el pedido... y como tiene que tener, un ientificador y un estado, 
             #creamos un constructor de clase, que va a tener que recibir un ID (identificador) y un estado.
    """ Si tuvieramos que crear un pedido por primera vez, podríamos pensar. ¿igual puedo definir el estado 
    inicial del pedido? podría ser así, porque al igual mi sistema, por lo que sea, quiero crear un pedido 
    en enviados. Igual quiero crear un pedido desde 0, este pedido tendría que tener el primer estado "Pending".
    Que el usuario le meta el estado que le de la gana! Pues tendrá que pasarle el ID y Status al crear el 
    pedido. Así que para que eso ocurra, se lo tenemos que asodiar (linea 84)"""
    #Vamos a definir un constructor para que el usuario no pueda usar otro estado que el Pending a la hora de crear un pedido.
    #Porque no tiene ningún sentido, el crear un pedido en estado "Cancelado, Enviado..."
    status = OrderStatus.PENDING
    def __init__(self, id) -> None: #Con ésto tendríamos la función que es necesario ID y Status para crear el pedido.
        self.id = id
    # Implementa las funciones que sirvan para modificar el estado:
        # - Pedido enviado
    def ship(self):
        if self.status == OrderStatus.PENDING:
            self.status = OrderStatus.SHIPPED
            self.display_status()
        else:
            print("El pedido ya ha sido enviado o cancelado")
        # - Pedido cancelado
    def cancel(self):
        if self.status == OrderStatus.PENDING:
            self.status = OrderStatus.CANCELLED
            self.display_status()
        else:
            print("El pedido no se puede cancelar  ya que se ha entregado")
        # - Pedido entregado
    def deliver(self):
        if self.status == OrderStatus.SHIPPED:
            self.status = OrderStatus.DELIVERED
            self.display_status()
        else:
            print("El pedido necesita ser enviado antes de entregarse")
        # (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
    def display_status(self):
        print(f"El estado del pedido {self.id} es: {self.status.name}")
 #Implementa una función para mostrar un texto descriptivo según el estado actual.
 #Crea diferentes pedidos y muestra cómo se interactúa con ellos. 

order_1 = Order(1)
order_1.ship()
order_1.deliver()
order_1.cancel()

