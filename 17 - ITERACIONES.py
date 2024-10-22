"""
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
"""

# Recorrer un conjunto de elementos (Iterar valores, estructuras, listados...)

for i in range(1, 11):
    print(i)

i = 1
while i <= 10:
    print(i)
    i += 1
#Función recursiva ( que ya lo vimos en el ejercicio 6)
def count_ten(i=1):
    if i <= 10:
        print(i)
        count_ten(i + 1)
count_ten()

#Extra

for e in [1, 2, 3, 4]:  #Iteramos una lista
    print(e)

for e in {1, 2, 3, 4}:  #Iteramos SETS
    print(e)

for e in (1, 2, 3, 4): #Iteramos una Tupla
    print(e)

for e in {1: "a", 2: "b", 3: "c", 4: "d"}:  #Iteramos un mapa con clave:valor
    print(e)

for e in {1: "a", 2: "b", 3: "c", 4: "d"}.values(): #Itermaos los valores, en vez de las claves, que e slo que sale por defecto ( arriba)
    print(e)

#Compresion list
print(*[i for i in range(1, 11)], sep="\n")     #Básicamente es la capacidad de crear listas d euna manera concisa.
#^^^^ Iteramos "i" en un rango que generaremos una lista que con el resultado nos quedaremos con el primer "i"
#El * es para decirle a la compresion list, como quieres terminar creándolo. El "sep", es un separador que le decimos que es un salto de linea

for c in "Python":  #Iteramos una cadena de texto.
    print(c)

for e in reversed([1, 2, 3, 4]):    #Iteramods una lista de forma reversa.
    print(e)

for e in sorted(["m", "o", "u", "r", "e"]): #Iteramos carácteres de forma ordenada ascendente.
    print(e)

for i, e in enumerate(sorted(["m", "o", "u", "r", "e"])): #Iteramos de forma que queremos conocer el índice de una estructura.
#"i"(indice), "e" (Elemento)
    print(f"Índice: {i}, valor: {e}")