"""
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 * 
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
"""
import xml.etree.ElementTree as xml
import os
import json
# Lo más lógico, será crear un diccionado con claves y valores, con los que la función pueda trabajar
data = {
    "name" : "Brais Moure",
    "age" : 36,
    "birth_date" : "29-04-1987",
    "programming_languages" : ["Python", "Kotlin", "Swift"]
}
xml_file = "mouredev.xml"
json_file = "mouredev.json"
#XML
def create_xml():
    root = xml.Element("data")                              # Invocamos el elemento "Element" de la libreria para que podamos escribir un elemento y de darle un nombre al elemento (podria ser un programador, una persona, pero le llamamos DATA)
                                                            # Para que el XML vaya anidando los datos, lo meteremos en una variable que llamamos ROOT
                                                            # Ahora que ya tenemos los datos en el elemento principal ( ROOT), ya podemos ir añadiendo cada uno de los datos, creando hijos de ROOT, (CHILD's)
                                                            # Ahora se crea el bucle para que recorra el diccionario en búsqueda de cada item
    for key, value in data.items():                         # Con for, le decimos que recorra TODOS los ITEMS de clave y valor que están en DATA ( el diccionario)
        child = xml.SubElement(root, key)                   # Creamos un Subelemento en base a ROOT, ( elemento principal)
        if isinstance(value, list):                         # Le estamos diciendo que si hay subelementos que tengan una instancia, (en éste caso una lista), haz "algo", sino, haz otra cosa
                                                            # Para ello, debemos saber como debe guardar esos diferentes datos, con un bucle, que recorra dicha lista por valor, si la hay (El valor, es el listado)
            for item in value: #listado
                                                            # Ahora deberemos guardar los elementos en un nuevo subelemento, en este caso ya no dependerá de ROOT, sino de CHILD que es "padre"  de éste nuevo subelemento
                xml.SubElement(child, "item").text = item   # Los guardamos en child y lo llamamos ITEM ( podriamos llamarlo cualquier otra cosa, relacionada con el dato). También accedemos a su propiedad "text"y meterle el item, mejor que crear un sub elemento de nuevo.
        else:                                               #Y ahora cual es el texto? pues el texto en este caso seria "Brais moure" que se lo pasamos como valor
            child.text = str(value)
                                                            # Cuando ya tenemos todos los Elementos en el ROOT, nos queda crear el arbol de gerarquía para el XML
    tree = xml.ElementTree(root)                            # Accedemos al elemento de la librería ElementTree y le decimos que meta a ROOT ( que contiende todos los datos, clave/Valor de DATA)
    tree.write("mouredev.xml")                              # Por último le decimos que ya escriba todos esos elementos en un archivo .xml ( que creará autamáticamente)
create_xml()

with open (xml_file, "r") as xml_data:
    print(xml_data.read())

os.remove(xml_file)

#json
def create_json():
    with open (json_file, "w") as json_data:
        json.dump(data, json_data)                              #DUMP nos da la posibilidad de pasarle un objeto (el diccionario DATA) y que lo transcriba directamente a json donde lo guaradaremos en el json_data
create_json()
with open (json_file, "r") as json_data:
    print(json_data.read())

#EXTRA
#Antes hemos cogido datos nativos y los hemos metido en archivos creados en XML y JSON, ahora lo haremos al revés. Cogeremos los datos de esos archivos y los transformaremos para que la Clase que vamos a crear acontinuación, pueda trabajar con ellos.

create_xml()

create_json()
class Data:
    def __init__(self, name, age, birth_date, programming_languages) -> None:
        #uNA VEZ ESCRITO LOS PARÁMETROS, LOS VAMOS GUARDANDO.
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_languages = programming_languages

#Como soy capaz de leer los datos de un archivo y de transformarlos aquí
with open (xml_file, "r") as xml_data:                          #vamos a leerlo
                                                                #Ahora vamos a intentar crear una Class Data con éstos datos ( los que a leido del archivo XML)
    root = xml.fromstring(xml_data.read())                             #Ahora hacemos la operación a la inversa (con respecto a ejercicios anteriores). Recuperamos los datos del XML, pero para ello, recuperaremos cada uno de los datos.
    #Tenemos que recuperar cada uno de los datos. donde lo tienes? en el texto.
    name = root.find("name").text
    age = root.find("age").text
    birth_date = root.find("birth_date").text
    #Éste no puede ser igual que los anteriores, porque contiene una lista, así que para acceder a la lista, hay que hacerlo con un FOR
    #programming_janguages = root.find("programming_janguages").text
    #Primero crearemos un listado en vacio para guardar los elementos.
    programming_languages = []
    for item in root.find("programming_languages"):             #Por cada uno de los items busca en root lo que contenga.
        programming_languages.append(item.text)                 #Aquí vamos añadiendo (con append) los diferentes elementos accediendo a su texto (de cada item) para obtenerlos.
    
    xml_class = Data(name, age, birth_date, programming_languages)
    print(xml_class.__dict__)                                   #Le pedimos que nos lo imprima y que lo trnscriba como diccionario

#Ahora trabajemos con json

with open (json_file, "r") as json_data:
#como tenemos que hacer para leer el diccionario....
#creamos una clase y accedemos a cada uno de los elementos
        #json_dict = json_data.read()                            #Éste read será capaz de crear un diccionario, el problema es que si hacemos un print type, nos dice que es un diccionario STR, lo cual luego, no lo entenderá, para ello:     
        #print(type(json_dict))
    json_dict = json.load(json_data)
    #print(type(json_dict))
#accedamos a los elementos
        #En vez de hacerlo, como se representa abajo, accedemos a ellos directamente para transformarlos en la class de más abajo
            #name = json_dict["name"]
            #age = json_dict["age"]
            #birth_date = json_dict["birth_date"]
            #programming_languages = json_dict["programming_languages"]
    json_class = Data(
        json_dict["name"],
        json_dict["age"], 
        json_dict["birth_date"],
        json_dict["programming_languages"])   #Por la parte de la lista, JSON ya lo entiende automáticamente. no es como XML que hay que especificárselo.
    print(json_class.__dict__)  

    os.remove(xml_file)
    os.remove(json_file)