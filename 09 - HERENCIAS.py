"""
* EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
"""

#Hablamos de herencias, cuando se trata de crear una gerarquía de clases. Haber una clase padre, unas clases hijas, éstas heredando atributos y funciones de la Super clase o clase padre.
#Con ésto ganamos reutilizar el código  sin tener que reescribir continuamente lo mísmo.

#CLASE PRINCIPAL, SUPERCLASS O PADRE
class Animal:
    def __init__ (self, name:str):
        self.name = name

    def sound(self):
        print("Este animal emite un sonido no determinado")
        pass

#SUBCLASES O CLASES HIJAS
class Dog(Animal):                                              # Hacemos que las subclases, hereden de su clase principal. Hemos hecho que animal, sea polimórfico, si es un perro, suene de una manera, si es un gato, suene de otra.
    def sound(self):
         print("Guau!")

class Cat (Animal):
    def sound(self):
         print("Miau!")

def print_sound (animal : Animal):                                # Le pasamos animal, que és un Animal(class). FUNCIÓN EXTERNA fuera de perro... de gato... de todo.
    animal.sound()
#Ahora implementamos...

my_animal = Animal("Animal")                                      # Creamos el objeto Animal genérico.
print_sound(my_animal)
#my_animal.sound()                                                # Se comenta por la creación de la función externa print_sound, si se borra esa función, volver a descomentar.
my_dog = Dog("perro")
print_sound(my_dog)
#my_cat.sound()                                                   # Se comenta por la creación de la función externa print_sound, si se borra esa función, volver a descomentar.
my_cat = Cat("gato")
print_sound(my_cat)
#my_cat.sound()                                                   # Se comenta por la creación de la función externa print_sound, si se borra esa función, volver a descomentar.

#POLIFORMISMO

#El polimorfismo es la capacidad d eun objeto d epoder adquirir muchas formas. Es que sin que la clase lo sepa lo que és, pueda comportarse de una manera distinta.
# En programación,Es la capacidad que tiene una clase para ser tratadas como instancias de una clase padre pero desde el punto de vista de lo que llamamos interfaces sin saber que el pueda comportarse de una manera distinta

#En el ejemplo anterior, veos como se dota d epolimorfismo no solo en tiempo de sobrecarga de métodos, como en el caso de sobre cargar SOUND, sino que en tiempo de ejecución.
#Cómo la clase, adopta distintas formas en el sonido de animal.
#Polimorfismo permite: Reutilizar, acotar código y evitar errores.

###EXTRA
"""Acontinuación crearemos 3 clases, siendo Employee la clase padre y las demás clases hijas que heredan de la padre.
La clase padre, contendrá el inicializador con los atributos en comun de todas las clases.
Cada clase hija, tendrá su función, a excepción del programador que a parte de tener su función ( programar) hay que añadirle un atributo personalizado. El lenguaje en el que trabaja.
Para no repetir código en programador al tener que crearle un atributo nuevo, se usará la función "super" para llamar al inicializador ( que ya contiene los 2 atributos principales)
"""
#Super Clase
class Employee:
    def __init__(self, id: int, name: str):                                                             #Creamos el inicializador

        self.id = id                                                                                    #Añadimos dos atributos principales que luego las clases hijas, heredarán.
        self.name = name
        self.employees = []
    
    def add(self, employee):                                                                            #Ahora las clases hijas, van a poder añadir empleados, ya que heredan. (**Pero no queremos que programador tenga nadie a su cargo)
        self.employees.append(employee)                                                                 #Para inicializarlo, hay que crear una lista y meterla en la variable employee
    #SI QUEREMOS QUE IMPRIMA TODOS LOS EMPLEADOS...
    def print_employees(self):
        for employee in self.employees:
            print(employee.name)    #(Ahora ve a la parte de ejecución y pruebalo.)

class Manager(Employee):
    def coordinate_projects(self):
        print(f"{self.name} El coordinador, está controlando todos los proyectos de la empresa")


class ProjectManager(Employee):

    def __init__(self, id: int, name: str, project: str ):
        super().__init__(id,name)
        self.project = project

    def coordinate_project(self):
        print(f"{self.name} Está coordinando su proyecto.")

class Programmer(Employee):

    def __init__(self, id: int, name: str, lenguage: str ):
        super().__init__(id,name)
        self.lenguaje = lenguage

    def code (self):
        print(f"{self.name} Está programando en {self.lenguaje} ")

    def add(self, employee:Employee):                                                                              #**Así que hay que sobrecargar la función.
        print (f"un programador no tiene empleados a su cargo. {employee.name} no se añadirá.")

##A trabajar con ellos, vamos a ver como montamos una gerarquía, basándonos en una superclase empezamos a modificar su comportamiendo basandonos en la clase especializada que vayamos a crear. basandonos nuevamente en la herencia y por otro lado en el polimorfismo
#PARTE DE EJECUCIÓN#
my_manager = Manager(1, "Francisco")
my_project_manager = ProjectManager(2, "Juan", "Proyect1")
my_project_manager_2 = ProjectManager(3, "Pedro", "Proyect2")
my_programmer = Programmer(4, "Pedro", "Swift")
my_programmer2 = Programmer(5, "Alberto", "Cobol")
my_programmer3 = Programmer(6, "Sandra", "Java")
my_programmer4 = Programmer(7, "Maite", "Python")

my_manager.add(my_project_manager)
my_manager.add(my_project_manager_2)
my_project_manager.add(my_programmer)
my_project_manager.add(my_programmer2)
my_project_manager_2.add(my_programmer3)
my_project_manager_2.add(my_programmer4)

my_programmer.add(my_programmer2)                                                                       #Le decimos que programador principal, manda sobre programador 2

my_programmer3.code()
my_project_manager.coordinate_project()
my_manager.coordinate_projects()

#Ejecución de la función print_employees
my_manager.print_employees()
my_project_manager.print_employees()
my_programmer.print_employees()