"""
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
"""
#TIPOS DE DATO POR VALOR 
"""(es un elemento único incluso cuando lo enviamos a otra instancia o lo enviamos a otra variable. lo que estamos creando es un nuevo elemento no modifica el elemento original.
    Al modificar la variable original no va a afectar a otras variables a las que se les haya asignado la variable principal.
    Los siguientes, son tipos de datos por Valor: INT (3,6,9), FLOAT (1.24, 6.34), COMPLEX (1+2J), STR, BOOL ( True / False)
    Explicado para tontos: ++ Ei A! cuando vales ahora?
                           -- Pues ahora Valgo 10! Pero "User" me va a cambiar en el futuro y dos lineas mas abajo, valdré 30.
                           ++ Muy bien. pues yo me quedo con ese valor y me da igual lo que te pase a posteriori.
    Aunque sigamos modificando sus valores, no pasa absolutamente nada, ya que A y B estan en sus respectivos posiciones de memoria indendientes.
    )"""

my_int_a = 10
my_int_b = my_int_a #aquí le estamos diciendo que B coja el valor de A, en este caso, B vakdrá 10.
#my_int_b = 20
my_int_a = 30
print(my_int_a)
print(my_int_b)

#TIPOS DE DATO POR REFERENCIA.

"""
Son todos aquellos tipos de datos que no son primitivos, es decir: LISTAS, DICCIONARIOS, CONJUNTOS (SET's colecciones desordenadas de elementos únicos {1, 2, 3}),
También lo pueden ser OBJETOS PERSONALIZADOS: Instancias de clases definidas por el usuario.
 Al igual que en Tipo de dato por Valor, A y B estarán en sus respectivas posiciones de memoria, pero en cuanto le decimos que B = A, lo que sucde es que:
 Ei B ya que tú eres una Lista y actuas como referencia, no copias el valor de A y lo asigna a B, (como sí lo hace en Tipo de dato por valor), sino que lo que hace es:
 A apunta a la posicion de memoria M3
 B apunta a la posicion de memoria M4
 Mueve a B del M4 y lo mete dentro de M3 juntándolo con A. Así pues dejando libre la posición de memoria M4 para otro asunto.
 Lo que estemos tocando en la referencia, se va a modificar en TODAS LAS VARIABLES QUE ESTÉN LEYENDO ESE PUNTERO APUNTANDO HACIA ESA MISMA POSICIÓN DE MEMORIA QUE TIENEN ESOS DATOS.
 ASÍ QUE MUCHO OJO!!! LA PODEMOS LIAR MUY PARDA EN UN PROYECTO.
 """
my_list_a = [10, 20]
my_list_b = [30, 40]
my_list_b = my_list_a
my_list_b.append(30) #Queremos añadir 30 a la lista existente.
print(my_list_a)
print(my_list_b)
#Que va a pasar? que tanto A como B van a mostrar el mismo resultado aunque hayamos añadido el 30 solo a B.

#Funciones con datos por Valor.
my_int_c = 10

def my_int_func (my_int: int):
    my_int = 20
    print(my_int) #Aquí hemos modificado el valor a 20 asi que tras el print, My_int_c, ahora valdrá 20
my_int_func(my_int_c) #Pero aquí, sigue valiendo 10.
print(my_int_c)       #Lo cual imprimirá 10. porque my_int = 20, no ha modificado la variable exterior.

#Funciones con datos por Referencia.

def my_list_func (my_list: list):
    my_list.append(30)

    my_list_d = my_list
    my_list_d.append(40)

    print(my_list)
    print(my_list_d)

my_list_c = [10, 20]
my_list_func(my_list_c)
print(my_list_c)

###EXTRA

def value(value_a: int, value_b: int) -> tuple:  #retorna una tupla de un par de valores.
                                                # El ejercicio pide que se inviertan los valores de A a B y B a A.
    temp = value_a                              # Para ello, creamos una variable auxiliar con el valor de A.
    value_a = value_b                           # sin la var ausiliar, machacas el valor de A con el de B, y pierdes A. Pero con la var auxiliar, ésto no pasa y tienes el valor de B en A.
    value_b = temp                              # aquí invertimos los valores
    return value_a, value_b


my_int_d = 10
my_int_e = 20
my_int_f, my_int_g = value(my_int_d, my_int_e)

print(f"{my_int_d},{my_int_e}")
print(f"{my_int_f},{my_int_g}")

# Por referencia

def ref(value_a: list, value_b: list) -> tuple:  
    temp = value_a                              #Tenemos TEMP que guarda el puntero de A ( NO EL VALOR, COMO ANTES)                
    value_a = value_b                           #Aqui tenemos el puntero de A que pasa a tener el puntero de B              
    value_b = temp                              #Y ahora que el puntero B tiene la lista A
    return value_a, value_b


my_list_e = [10, 20]
my_int_f = [30, 40]
my_int_g, my_int_h = ref(my_list_e, my_int_f)

print(f"{my_list_e},{my_int_f}")
print(f"{my_int_g},{my_int_h}")