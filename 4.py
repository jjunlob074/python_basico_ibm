# Escriba un código que calcule la suma una lista de números proporcionados.
def sum_numbers(numbers):
    # Solución 1: Utilizando la función built-in sum()
    return sum(numbers)

    # Solución 2: Utilizando un bucle for
    # total = 0
    # for num in numbers:
    #     total += num
    # return total

    # Solución 3: Utilizando comprensión de listas
    # return sum([num for num in numbers])

    # Solución 4: Usando la función reduce() de functools
    # from functools import reduce
    # return reduce(lambda x, y: x + y, numbers)

    # Solución 5: Usando recursión
    # if not numbers:  # Caso base
    #     return 0
    # return numbers[0] + sum_numbers(numbers[1:])  # Llamada recursiva

    # Solución 6: Usando un generador
    # def generator():
    #     for num in numbers:
    #         yield num
    # return sum(generator())

    # Solución 7: Usando NumPy (si tienes la biblioteca instalada)
    # import numpy as np
    # return np.sum(numbers)
    
# Prueba de la función
lista_numeros = [3, 5, 8, 9, 9]
print(f"La suma de los números en la lista {lista_numeros} es: {sum_numbers(lista_numeros)}")