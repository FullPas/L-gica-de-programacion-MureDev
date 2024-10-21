"""
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han
 *   finalizado.
"""
import datetime
import time
import asyncio                      #Para ejecutar una función de forma asíncrona.

#Así aseguramos que ésta función se ejecute en segundo plano independiente del programa.
async def task(name: str, duration:int):
    print(
        f"Tarea: {name}. Diracion: {duration}s. Inicio: {datetime.datetime.now()}")
    #time.sleep(duration)           #Es para cuando no es de forma asíncrona. porque así bloquea el hilo porque no se está ejecutando como segundo plano real.
    await asyncio.sleep(duration)
    print(
        f"Tarea: {name}. Fin: {datetime.datetime.now()}")
asyncio.run(task("1",5))



#Antes de resolverlo como abajo, primero, segun lees el enunciado, escribes las 4 taresas/funciones..

#task("A", 1)
#task("B", 2)
#task("C", 3)
#task("D", 1)
#lUEGO YA PASAS A ESCRIBIR LA FUNCIÓN EN PARALELO, COMO PIDE EL ENUNCIADO Y MODIFICAS LO ANTERIOR PARA METERLO EN EL GATHER.
async def async_tasks():
    #Le apsamos las 3 funciones asíncronas para que se ejecuten a la vez.
    await asyncio.gather(task("C", 3),task("B", 2),task("A", 1)) #Con gather especificamos que una tarea va a acabar en el futuro.
    #El await se añadió despues de ejecutarsolo la linea de arriba. Dió un error diciendo que nunca se está esperando por la rutina.
    #Le tenemos que decir que "espere en este punto para que lo demás finalice"
    await task("D", 1),
asyncio.run(async_tasks())