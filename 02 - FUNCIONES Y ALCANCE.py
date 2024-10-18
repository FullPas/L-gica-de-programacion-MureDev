"""
* EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""
#DEFINICIÓN:
"""
Bloque de código que lo reutilizamos para hacer una acción específica, es una forma lógica de reutilizar, sea más legible, 
hacer que no se cometan tantus bugs, que sea más facil de escalar, de mantener...
"""
###FUNCIONES DEFINIDAS POR EL USUARIO###

#FUNCIÓN SIMPLE:

def greet(): #saludo
    print ("Hola Python") #--> Usamos siempre la plabra reservada "def" para crear una función, en éste caso, sin atributos.
greet()                   # Luego con greet, llamamos a la función para que nos dé el resultado de print.

#FUNCIÓN CON RETORNO:

def return_greet():
    return "Hola python"  #Le pedimos que nos devuelva un valor, en éste caso un String.
#Si no quieres guardarte el retorno en ninguna variable, puedes directamente improbirlo. Sino...
    #print(return_greet())
greet = return_greet()    #Metemos el return en una variable, para luego, con print (en éste caso), imprimirla.
print(greet)

#Hasta aquí la lógica dependía de lo que había en el bloque del código ( print, return...)

#FUNCIÓN CON ARGUMENTO: (Si queremos que la función opere con "ese algo", le podemos pasar parámetros)

def arg_greet(name):
        print (f"hola, {name}!")
#Ahora llamamos a la función y en ésta le pasamos un argumento, algo con lo que pueda trabajar.
arg_greet("Pascual")

#FUNCIÓN CON ARGUMENTOS:
def arg_greet(greet, name):
        print (f"{greet}, {name}!") #Ahora el "hola" lo hemos parametrizado con un atributo al inicio d ela función
arg_greet("Hi", "Pascual") #Debemos pasarle dos argumentos, uno por cada atributo.

#FUNCIÓN CON ARGUMENTO PREDETERMINADO: (Hablamos que aunque siempre hay que pasar un argumento al final, en el caso de que no se pase ninguno, que el/los atributo/s tengan un valor por defecto.)

def default_arg_greet(name="python"):
        print (f"hola, {name}!")
default_arg_greet()

#FUNCIÓN CON ARGUMENTOS Y RETORNO:
def return_arg_greet(greet, name):
        return (f"{greet}, {name}!")
print (return_arg_greet("Hi", "Pascual"))

#FUNCIÓN CON RETORNO DE VARIOS VALORES: ( Lo que se conoce como una tupla de valores, más de 1)
def multiple_return_greet():
       return "Hola", "Python" #Ya estamos retornando dos valores, dos cadenas de texto. ¿Cómo hacemos para recuperar estos dos valores?
#Creamos dos variables separadas por una coma ( una para cada valor) y llamamos a la función
greet, name = multiple_return_greet()
#Y ahora imprimimos cada valor por separado para por ejemplo ( no es el caso) poder trabajar con cada valor por independiente en un proyecto mayor.
print(greet)
print(name)

#FUNCIÓN CON UN NÚMERO VARIABLE DE PARÁMETROS (ARGUMENTOS). LE PODEMOS PASAR UN NÚMERO INDEFINIDO DE ARGUMENTOS:

def variable_arg_greet(*names):
    for name in names:
          print(f"Hola, {name}!")
#Ahora llamamos a la función...
variable_arg_greet("Python", "Pascual", "Comunidad")

#FUNCIÓN CON UN NÚMERO VARIABLE DE PARÁMETROS (ARGUMENTOS) CON PALABRA CLAVE: (LE PODEMOS INDICAR UNA PALABRA CLAVE A CADA ARGUMENTO. ÉSTO LO AHCEOS INDICÁNDOLO CON 2 ASTERISCOS{**})
#Cada argumento estará formado por "CLAVE:VALOR"

def variable_key_arg_greet(**names):
    for key, value in names.items(): #Creamos las variables para la clave y el valor. La función ITEMS descompone cada argumento en clave y valor.
          print(f"{value}({key})") #Imprimimos también el parámetro que le pasamos a name.
#Le vamos a dar una clave a cada argumento.
variable_key_arg_greet(
      lenguaje="Python", 
      nombre="Pascual", 
      alias="likarus", 
      edad=38)

#FUNCIONES DENTRO DE FUNCIONES ( ANIDADAS):
def outer_function():
      def inner_function():
            print("Funcion interna: Hola python!")
      inner_function() # <<<----- si ésto no está, no funka!
outer_function()

#Para que el PRINT de la función interna, se ejecute, hay que llamar a ambas funciones. Es decir: outer_function() llamará a inner_function() y éste ejecutará el print.
# Si no está el llamamiento de la función interna, nunca se ejecutará ésta.
#Éste tipo de funciones se suele utilizar cuando quieres estructurar mucho el código, dividir las funciones del código... etc.
#OJO!!! Python soporta éste tipo de estructura. no todos los lenguajes lo soportan.


###HASTA AHORA HEMOS VISTO FUNCIONES CREADAS POR EL USUARIO. AHORA VEREMOS FUNCIONES QUE ESTÁN PREDETERMINADAS ( YA CONSTRUIDAS) POR EL LENGUAJE.

#FUNCIONES DEL LENGUAJE ( built-in):
#Son funciones que se usan día a día en el bloque de código: print, len, type, upper... hay cientos de ellas.
#Por ejemplo:

print()                     # Que ya es una función en sí misma.
print(len("Pascual"))       # LEN es una función que nos retorna un entero. 
                            # Si le pasamos una estructura d edatos, nos contará cuantos elementos tiene esa estructura. La función en sí nos imprime numero de carácteres que le hemos pasado en el String
print(type(38))             # Nos dice el tipo de dato que le pasamos.
print("pascual".upper())    # Nos modifica el string, pasandolo a mayúsculas

#########################################################################################################################################################################
###VARIABLES GLOBALES Y LOCALES###
#########################################################################################################################################################################
#ÁMBITO o SCOPE: Es Cuándo tenemos acceso a segun qué de nuestro código

var_global = "Python"

def hola_python():
    print(f"Hola, {var_global}!")

hola_python()
#¿Qué estamos haciendo aquí? Estamos llamando a la función  para que utilice una var externa a la función. Lo que se conoce como variable global. (su ámbito es superior a lo que queremos ejecutar)

var_global = "Pascual"

def hola_python():
    var_local = "Holaa"
    print(f"{var_local} {var_global}!")
hola_python()

#¿Qué estamos haciendo aquí? Que aparte de tener acceso a la var global, tabién tenemos acceso a la var local.
# Pero... y que pasa si llamamos a la var local desde fuera? que nunca accederá. ya que la var local, solo se puede acceder a ella, desde dentro de la misma función.
var_global = "Pascual"
def hola_python():
    var_local = "Holaa"
    print(f"{var_local} {var_global}!")

hola_python()
print(var_global)
#print (var_local)

###TAMBIÉN EXISTEN FUNCIONES LAMBDA Y FUNCIONES RECURSIVAS QUE SON MAS DE APLICAR UNA LÓGICA MUY CONCRETA PARA SU EJECUCIÓN. YA SE VERÁN MÁS ADELANTE.###

###EJERCICIO EXTRA!!!

def print_numbers(text1, text2) -> int:
      count = 0 
      for number in range(1, 101):
          if number % 3 == 0 and number % 5 == 0:
              print(text1 + text2)
          elif number % 3 == 0:
              print(text1)
          elif number % 5 == 0:
              print(text2)
          else:
               print(number)
               count += 1
      return count
print(print_numbers("Fizz", "Buzz"))