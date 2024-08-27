"""
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
"""

s1 = "Hola"
s2 = "Python"

#Concatenación
print (s1 + "," + s2 + "!")

#Repetición
print(s1 * 3)

#Indexación
print(s1[0] + s1[1] + s1[2] + s1[3])

#Longitud
print(len(s2))

#Slicing (porción)
print(s2[2:6])
print(s2 [2:])
print(s2 [:2])

#Búsqueda
print("a" in s1)
print("i" in s1)

#Reemplazar
print(s1.replace ("o", "a"))

#División (corte, creando una estructura de datos o lista)
print(s2.split ("t"))

#Mayúsculas o Minúsculas y primera letra en mayúsculas
print(s1.upper())
print(s1.lower())
print("Brais moure".title())
print("Brais moure".capitalize())

#Eliminación de espacios al princio y al final
print(" Brais Moure ".strip())

#Búsqueda al principio y al final
print(s1.startswith("Ho")) #Le preguntas si empiezas por Ho = True
print(s1.startswith("Py")) #Dará false, porque no empieza por Py
print(s1.endswith("thon"))# Dará True.

#Búsqueda por posición
s3 = "Brais Moure @mouredev"
print(s3.find("moure"))
print(s3.find("Moure"))
print(s3.find("M"))
print(s3.lower().find("m"))

#Búsqueda de ocurrencias
print(s3.lower().count("m"))#Le preguntamoa cuantos caracteres "m" hay.

#Formateo
print("Saludo: {}, Lenguaje {}!".format(s1, s2))

#Interpolación
print(f"Saludo: {s1}, Lenguaje {s2}!")

#Transformación en lista de carácteres
print(list(s3))

#Transformación en lista de cadena.
l1 = [s1, ",",s2, "!"]
print("".join(l1)) #Con JOIN concatenamos resultados de una lista y pasamos de lista a cadena de texto.

#Transformación numéricos
s4 = "123456"
s4 = int (s4) #Transfórmame el string a entero y vuelvelo a guardar en la var s4.
print(type(s4))
print(s4)

s4 = "1234.66"
s4 = float (s4) #Transfórmame el string a entero y vuelvelo a guardar en la var s4.
print(type(s4))
print(s4)

#Comprobaciones varias
s4 = "123456"
print(s4.isalnum())# Es la cadena de texto numérica?
print(s1.isalpha())# Es la cadena de texto alfanumérica?

###DIFICULTAD EXTRA###

def check(word1: str, word2: str):
    #palíndromos (coges la 2ª palabra, le das la vuelta y la contrastas con la primera, siempre siendo la mísma palabra: por ej. radar)
        #print(f"¿{word1} es un palíndromo?: {word1 == word1[::-1]}")       #ANULADO POR EL ISOGRAMA, QUE NO AFECTE, PERO SI QUE FUNCIONA
        #print(f"¿{word2} es un palíndromo?: {word2 == word2[::-1]}")       #ANULADO POR EL ISOGRAMA, QUE NO AFECTE, PERO SI QUE FUNCIONA
    #Anagrama: (Contrasta entre dos palabras distintas.)
        #print (f"¿ es {word1} un anagrama de {word2}?: {sorted(word1) == sorted(word2)}")      #ANULADO POR EL ISOGRAMA, QUE NO AFECTE, PERO SI QUE FUNCIONA
    #Isograma


    def isogram(word: str) -> bool:
        word_dict = dict()                                      #Declaramos un diccionario
        for word in word2:
                word_dict[word] = word_dict.get(word, 0) + 1    #Con "[word]" le estamos diciendo al diccionario que intente guardar el número d eveces que se repite una letra de la palabra.
        print(word_dict)                                        #le hacemos un get al diccionario e intentamos acceder a la palabra word. Cada vez que acceda le sume 1, pero que por defecto, empiece en 0 a contar.
        isogram = True                                       
        values = list(word_dict.values())                       #Hay que trnsformarlo a una Lista porque sino, da error el campo values[0],
        isogram_len= values[0]                                  #Se accede  al primer elemento del diccionario. y se mete en la var isogram_len que refiere a la longitud del isograma.
        for word_count in values:                               #Aqui se mira (se revisa cual es el valor que tiene cada uno) cual es la longitud de cada una de las letras, cuantas ocurrencias hay de cada letra
            if word_count != isogram_len:                     #Aquí decimos que si la longitud del isgrama es distinto a la longitud del isograma (¿¿¿whaatt???)
                    isogram = False                             #Entonces, isogram es False.
                    break
        return isogram
    print(f"¿{word1} es un isograma?: {isogram(word1)}")
    print(f"¿{word2} es un isograma?: {isogram(word2)}")
    #print (f"¿ es {word2} un isograma?: {len (word2) == len(set(word2))}")
check("radar", "pythonpythonpythonpython")
#check("amor", "roma")  #Anulado por Isograma, valido solo para anagrama.


