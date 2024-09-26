"""
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado. 
"""

try:
    print(10/1)
    print([1, 2, 3, 4[4]])
except Exception as e:
    print(f"Se ha producido un error: {e}")

#EXTRA                                                          #Se va a generar de forma abrupta un Index Error, en la consulta d eun tercer elemento de una lista ( que no existe)


class StrTypeError(Exception):                                  #Error personalizado
    pass                                                        #Sin más pasa.                                                                

def process_params(parameters: list):
    if len(parameters) < 3:
        raise IndexError()                                      #Raise es una palabra reservada para controlar y lanzar el tipo de error, en este caso por consola.
    elif parameters[1] == 0:                                    #Aquí vamos a provocar un erorr que hará que se detenga el programa.
        raise ZeroDivisionError()                               #Con ésto lo capturamos para controlarlo.
    
    elif type(parameters[2]) == str:
        raise StrTypeError ("El tercer elemento de la lista no puede ser una cadena de texto")
        
    print(parameters[2])                                                #Nosotros aquí buscamos acceder al parámetro de la posición 2 de la lista, pero... y su dividimos 0, en tre 1? nos dará error?
    print(parameters[0]/parameters[1])                                  #El aprámetro 0 , lo dividimos entre el parámetro 1
    print(parameters[2] +5)
#Ahora, capturemos el error...

#----------------------------------------------------------------------------------------------------------------------------------------------
# 2 Errores del sistema
try:
    process_params([1, 2, 3])                                           #si añadimos un 0 en la 2ª posicion (dará ZeroDivisionError), Si sustituimos el 3 por "brais" (dará error inesperado)
except IndexError as e:
    print("El número de la lista debe ser mayor que dos")
except ZeroDivisionError as e:
    print("El segundo elemento de la lista no puede ser un cero")       #Pues quí estamos capturando el error que generaría el programa al intentar dividir el elemento 2 de la lista.
#------------------------------------------------------------------------------------------------------------------------------------------------
# 1 Error personalizado
except StrTypeError as e:
    print(f"{e}")

#Captura de cualquier otro error como buena práctica.

except Exception as e:                                                   #Como buena práctica, si no entra en ningun bloque anterior, que pueda salir por el siguiente:
    print(f"Se ha producido un error inesperado {e}")
else:                                                                    # En Try/Except existe también ( al igual qu en el condicional IF) Else, donde, si no se cumplen ninguna de las anteriores excepciones, podemos indicar, por ejemplo, que no hubo ningún error.
    print("No se ha producido ningún error.")
finally:
    print("El programa finaliza  sin detenerse.")


