"""
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""

#Operadores aritméticos:
print (f"Suma: 10 + 3 = {10 + 3}") # con la "f" interpolamos valores dentro de una cadena de texto mediante llaves.
print (f"Resta: 10 - 3 = {10 - 3}")
print (f"Multiplicación: 10 * 3 = {10 * 3}")
print (f"División: 10 / 3 = {10 / 3}")
print (f"Módulo de: 10 % 3 = {10 % 3}")
print (f"Exponente: 10 ** 3 = {10 ** 3}")
print (f"División entera: 10 // 3 = {10 // 3}")

#Operadores de comparación:
print (f"igualdad: 10 == 3 es {10 == 3}")
print (f"desigualdad: 10 != 3 es {10 != 3}")
print (f"Mayor que: 10 > 3 es {10 > 3}")
print (f"Menor que: 10 < 3 es {10 < 3}")
print (f"Mayor igual que: 10 >= 3 es {10 >= 3}")
print (f"Menor igual que: 10 <= 3 es {10 <= 3}")

#Operadores lógicos:
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es: {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 es: {10 + 3 == 13 or 5 - 1 == 4}")
print(f"NOT !: not 10 + 3 == 14 es: {not 10 + 3 == 14}")

#Operaciones de asignación:
my_number = 11 #el = es el operador de asignación. Asignamos 11 a my_number.
print(my_number)
my_number += 1 #suma y asignación. Suma 1 al valor que ya tiene my_number
print(my_number)
my_number -= 1 #
print(my_number)
my_number *= 2 #
print(my_number)
my_number /= 2 #
print(my_number)
my_number %= 2 #
print(my_number)
my_number **= 2 #
print(my_number)
my_number //= 2 #
print(my_number)

#Operadores de identidad: (sirven para comparar el valor de la posición de la memoria, es decir, que nos puede servir en algún momento para comparar si de verdad dos objetos, son iguales.)
my_new_number = my_number #(si ponemos como valor 1.0, nos dará FLASE porque aunque sea igual al resultado anterior, ambos están en posiciones distintas de memoria)
print(f"my_number is my_new_number es:{my_number is my_new_number}")
print(f"my_number is not my_new_number es:{my_number is not my_new_number}")

#Operadores de pertenencia: ( es si ALGO pertenece a ALGO)
    #Imaginemos que quiero comprobar si la letra L está en mi nombre:
print(f"'l' in Pascual = {'l' in 'Pascual'}")


#Operadores de bit ( básicamente trabaja a nivel de bit para hacer comparación)
a = 10  #En bits hablariamos que 10 es 1010
b = 3   #En bits hablariamos que 3  es 0011
print(f"AND 10 & 3 = {10 & 3}") # el resultado dará 2.
                                #Lo que hace es coger los bits de 10 y 3 y de derecha a izquierda los compara: 
                                # 0 y 1 = 0; 
                                # 1 y 1 = 1; 
                                # 0 y 0 = 0; 
                                # 1 y 0 = 0. Qué da todo ésto? 0010, que en decimal es: 2. Sigamos con el siguiente.
print(f"OR 10 | 3 = {10 | 3}")  # A diferencia del anterior, con que solo haya un "1" en uno de las opciones, el resultado será "1". En éste caso: 1011, que es: 11 en decimal.
print(f"XOR 10 & 3 = {10 ^ 3}") # En éste caso si el resultado son diferentes: es "1". Si son iguales: es "0". 1001, que és 9.
print(f"NOT ~10 = {~10}")       #Intercambia el valor bit a bit de cualquiera de los elementos. dará -11.
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") #10 es 1010 en binario, si ahora desplazamons un bit a la derecha quedaría: 0101. con 2 bits sería 0010 (el segundo 1 desaparece)
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") #pues lo mismo pero a la inversa. de 1010, quedaría: 101000 que es 40.


#ESTRUCTURAS DE CONTROL
#Condicionales:

my_string = "Brais"

if my_string == "Mouredev":
    print ("my_string es 'Mouredev'")
elif my_string == "Brais":
    print ("my_string es 'Brais'")
else:
    print("my_string no es 'Mouredev'")

#Iterativas

for i in range (11):
    print(i)

#Planteas que el bucle se ejecute mientras esa condición sea verdadera. por ejemplo si creamos una variable en la que:
i = 0

# Ejecuta el bucle infinitamente mientras esta condición se dé.
while i <= 10:
    print(i) #Con ésto se ejecutaría indefinidamente
    i += 1 # Se le iría sumando 1 al resultado anterior hasta llegar al 10, lo cual se detendría.

#Manejo de excepciones.
#Útil para evitar que el programa, no se rompa, que aunque esa parte del código no se ejecute, mande un mensaje al usuario y podamos continuar. Apaliar el error.

#Si lo lanzamos así tal cual, nos lanzará un "ZeroDivisionError y el programa se detendrá"
    #print (10 / 0)

#Entonces para apaliarlo...:
try:
    print (10 / 0)
except: #cath
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepción")

for i in range (10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
