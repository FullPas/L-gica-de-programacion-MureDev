"""
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
"""

from datetime import datetime

now = datetime.now()
print(now)

birth_date = datetime(1986, 2, 20, 7, 21, 0)
print(birth_date)

difference = now - birth_date

print (type(difference))
print(f"Tengo {difference.days // 365} años")                   #el // es para que te dé una división entera, porque solo con un / te da decimales.

#Extra

#Día, Mes y Año
print(birth_date.strftime("%d/%m/%y"))
print(birth_date.strftime("%d/%m/%Y"))
#Horas, minutos y segundos
print(birth_date.strftime("%H:%M:%S"))
#Día del año
print(birth_date.strftime("%j"))
#Día de la semana
print(birth_date.strftime("%A"))
#Nombre del mes
print(birth_date.strftime("%B"))
print(birth_date.strftime("%h"))
#Representacion por defecto del local
print(birth_date.strftime("%c"))
print(birth_date.strftime("%x"))
print(birth_date.strftime("%X"))

print(birth_date.strftime("%A %x %X")) 