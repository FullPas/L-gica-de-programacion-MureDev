"""
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
"""
import unittest
from datetime import datetime, date
#Operaciones de ASSET: Son operaciones que se encargan de validar datos.

def sum (a, b):
    #PAra controlar el flujo de información, acotarlo a que solo sean INT o FLOAT...
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los argumentos deben ser enteros o decimales")            #raise para controlar una excepción.
    return a + b

#Para ejecutar un test, hay que hacerlo dentro de una clase
class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(5, 7), 12) #Funcion que busca ver si algo es igual a algo. En este caso le pasamos lo que queremos ejecutar, que és la función SUM que le pasamos el 5 y el 7 y le decimos que esperamos que nos de 12.
        self.assertEqual(sum(5, -7), -2)
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(2.5, 2.1), 4.6)
        self.assertEqual(sum(2, 2.1), 4.1)
        self.assertEqual(sum(2.5, 2.5), 5)
    
    def test_sum_type (self):

       # with self.assertRaises(ValueError):
       #    sum(5,7)
        with self.assertRaises(ValueError):
            sum("5",7)
        with self.assertRaises(ValueError):
            sum("a",7)
        with self.assertRaises(ValueError):
            sum(None,7)
#La siguiente libreria (que hemos importado arriba) va a buscar todos los test que empiecen por "test_" y los va a ejecutar


# unittest.main()   ( lo comento para que no entre en conflicto con el ejercicio extra.)



class TestData (unittest.TestCase):
# Si tenemos que comprobar cada campo del diccionario, como menciona el enunciado...
# En la propia clase donde estoy estableciendo todos los requisitos de Testing, tenemos una función especial que nos 
# permite preparar el contexto, es decir, podemos meterle datos (En éste caso el diccionario, que se encontraba fuera 
# de la clase), con los que va a trabajar el propio test. En Python es una función que se llama setUp.
    def setUp(self) -> None:
        self.data = {
            "name":"Brais Moure",
            "age" : 36,
            "birth_date": datetime.strptime("29-04-87", "%d-%m-%y").date(),
            "programming_languages": ["Python", "Kotlin", "Swift"]
        }
    #Vamos a comprobar si existen los campos.
    def test_fields_exist(self): #Ahora SELF tiene acceso al diccionario, poruqe está dentro del contexto de setUp.
        self.assertIn("name", self.data) #Queremos que compruebe si existe el campo NAME den el diccionario.
        self.assertIn("age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("programming_languages", self.data)
    
    def test_data_is_correct(self):
        self.assertIsInstance(self.data["name"], str)
        self.assertIsInstance(self.data["age"], int)
        self.assertIsInstance(self.data["birth_date"], date)
        self.assertIsInstance(self.data["programming_languages"], list)
unittest.main() 
