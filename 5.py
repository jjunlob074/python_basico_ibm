# Escriba un código que desordene al azar una lista.

import random

def desordenar_lista(lista):
    # Solución 1: Utilizando la función random.shuffle() / Esta solución usa la misma lista
    random.shuffle(lista)
    return lista

    # Solución 2: Utilizando random.sample() para crear una nueva lista desordenada / Son dos listas diferentes, es una copia desordenada de la lista original
    #lista_desordenada = random.sample(lista, len(lista))
    #return lista_desordenada

    # Solución alternativa: Utilizando la función sorted() y el parámetro key=lambda x: random.random()
    #lista_desordenada = sorted(lista, key=lambda x: random.random())
    #return lista_desordenada
    


# Prueba de la función
lista_prueba = [1, 2, 3, 4, 5, 6]
print(f"La lista antes de desordenar: {lista_prueba}")
print(f"La lista después de desordenar: {desordenar_lista(lista_prueba)}")
