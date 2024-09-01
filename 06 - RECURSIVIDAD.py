"""
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
"""
###RECURSIVIDAD: FUNCIÓN QUE SE LLAMA A SÍ MISMA. SE SUELE USAR EN PROBLEMAS EN LOS QUE HAY QUE SUBDIVIDIRLOS EN CACHITOS O ESTRUCTURAS EN ARBOL PARA PROFUNDIZAR A DISTINTOS IVELES(((ÉSTE EJERCICIO SIRVE PARA ENTENDER CUANDO ENTENDER UNA FUNCION RECURSIVA Y CUANDO USAR UN BUCLE FOR. NO ES UNA BUENA PRÁCTICA)))

def countdown(number:int):
    if number >= 0:             # Ésto es para que no pase de -1 y continue restando infinitamente.
        print(number)
        countdown(number - 1)   # Se llama así misma.

    countdown(100)              # Aquí le decimos desde donde debe partir.

###COMO SE DIJO ANTES, ÉSTA NO ES LA MEJOR PRÁCTICA, PARA ELLO TENEMOS LOS BUCLES FOR.

#EXTRA

def factorial (number:int) -> int:
    if number < 0:
        print("Los números negativos no son válidos.")
        return 0
    elif number == 0:
        return 1
    else:
        return number * factorial(number - 1)
print(factorial(5))


#Buscando la serie de fibonacci en google, se entiende el ejercicio.
def fibonacci(number:int) -> int:
    if number <= 0:
        print("Los números negativos no son válidos.")
        return 0
    elif number == 1: # se refiere a la primera posición, ya que en la serie de fib. no se puede sumar por ninguno anterior
        return 0
    elif number == 2: # se refiere a la segunda posición, ya que en la serie de fib. no se puede sumar por ninguno anterior
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2) # a partir de la 3ª posición ya sí puede calcular las dos anteriores.
    
print(fibonacci(5)) #Por ejemplo, 5ª posicion, puede calcular la 3ª y 4ª posicion que corresponden a 2 + 1 = 3.

