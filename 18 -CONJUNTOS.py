"""
 * EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
"""
#Estructura de datos que nos sirve para almacenar, pues eso, datos.

data = [1, 2, 3, 4, 5]
print(f"Estructura inicial: {data}")

data.append(6)
print(f"Añadiendo elemento al final: {data}")

data.insert(0, 0)
print(f"Añadiendo elemento al principio: {data}")

data.extend([7, 8, 9])
print(f"Añadiendo elementos al final: {data}")  #Extend nos permite añadir elementos en bloque con una lista y evitamos tener que hacer múltiples INSERT.

data[3:3] = [-1, -2, -3]                        #El [3:3] es una manera de añadir elementos en una posición específica en una lista. Aquí, [3:3] significa que estás insertando elementos en la posición 3 sin eliminar nada. Es como decir: “inserta estos elementos justo antes del índice 3”.
print(f"Añadiendo elementos en una posición: {data}")

del data[3]
print(f"Eliminando un elemento concreto: {data}")

data[4] = -1
print(f"Actualizando un elemento concreto: {data}")

print(f"Comprobar si un elemento existe: {-1 in data}")

print(f"Eliminar el contenido: {data.clear()}") #del.data se cargaría directamente el objeto.

"""
Extra
"""
#Lista
#elements_1 = [1,2,3,4,5]
#elements_2 = [1,2,3,4,6,7]
"""
¿Qué sucede?
Que no se pueden trabajar con listas, para añadir elementos de dos tuplas distintas porque con "extens" nos lo añade todo.
Como no queremos eso, porque estamos trabajando con TEORÍA DE CONJUNTOS MATEMÁTICA, no nos sirven las LISTAS. 
Tenemos que usar otra estructura, que en Python, es un SET.
Teniendo las listas, podríamos probar con el atributo UNION, ya que EXTENS no nos funciona, pero pasa que las LISTAS, no trbajan
con el atributo UNION. ¿Que sí trabajao con el atributo UNION? Los SETS: name = {dato1, dato2, dato,3 ... }
"""

#Conjuntos
set_1 = {1, 2, 3, 4, 5}
set_2 = {1, 2, 3, 4, 6, 7}

print(f"Unión: {set_1.union(set_2)}")   
print(f"Intersección: {set_1.intersection(set_2)}")

print(f"Diferencia: {set_1.difference(set_2)}")
print(f"Diferencia: {set_2.difference(set_1)}")

print(f"Diferencia simétrica: {set_1.symmetric_difference(set_2)}") #Todo lo que tienen en común ambas a  la vez