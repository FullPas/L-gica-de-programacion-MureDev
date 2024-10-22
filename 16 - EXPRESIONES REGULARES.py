"""
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
"""
#Es un estandar que nos permite analizar cadenas de texto, con una sintaxis muy concreta para encontrar algo, validar la cadena...
import re       #Nos permite usar la expresión regular.

regex = r"[0-9]+"      #Aquí ponemos la expresión regular que queramos usar. Faltará aplicarla (más abajo) con una función
                       #Para ser un poco más finos, en vez de 0-9, para expresar "todos los nºs,  existe: [\d] "
text = "Este es el ejercicio 16 publicado el 15/04/2024"

def find_numbers(text: str) -> list:
    return re.findall (regex, text) #Encuentrame todo y retornamelo.
print (find_numbers(text))

#Extra
def validate_email(email:str) -> bool:
    return bool(re.match(r"^[\w.+-]+@[\w]+\.[a-zA-Z]+$", email))
print(validate_email("mouredev@gmail.com"))
      
def validate_phone(phone:str) -> bool:
    return bool(re.match(r"^\+?[\d\s]{3,}$",phone))      #Validamos que: el + sea opcional con el "?", un rango de todos los números "\d" y espacios intercalados "\s" y que sea mínimo de 3 dígitos a infinito ( ya que hay centralitas con 9 o más números)
print(validate_phone("+34 901 92 34 22"))

def validate_url(url:str) -> bool:
    return bool(re.match(r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]+$",url))   #Validamos que: contenga el http con la opcional de la "s". que las "www." sean opcionales. El dominio sea de uno a cualquier carácter seguido de un punto y cualquier letra.
print(validate_url("https://www.moure.dev"))