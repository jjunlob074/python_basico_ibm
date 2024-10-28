# Escriba un programa para producir la serie Fibonacci en Python.


def fibonacci(n):
    # RECURSIVIDAD
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci(n-1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence


# Prueba del código
print(fibonacci(10))  # Debería imprimir [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(fibonacci(20))  # Debería imprimir [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

# # 2. Función Iterativa
# def fibonacci_iterativo(n):
#     # Función iterativa para generar la secuencia de Fibonacci.
#     fib_sequence = []  # Inicializa la lista para almacenar la secuencia.
#     # Itera desde 0 hasta n.
#     for i in range(n):
#         # Verifica si el índice es 0.
#         if i == 0:
#             fib_sequence.append(0)  # Agrega el primer número.
#         # Verifica si el índice es 1.
#         elif i == 1:
#             fib_sequence.append(1)  # Agrega el segundo número.
#         else:
#             # Suma los dos últimos números de la secuencia para generar el siguiente.
#             next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
#             # Agrega el nuevo número a la lista.
#             fib_sequence.append(next_fib)
#     return fib_sequence  # Devuelve la secuencia generada.

# # Pruebas del código iterativo
# print("\nFibonacci Iterativo:")
# # Imprime la secuencia de Fibonacci para n = 10.
# print(fibonacci_iterativo(10))  # Debería imprimir [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# # Imprime la secuencia de Fibonacci para n = 20.
# print(fibonacci_iterativo(20))  # Debería imprimir los primeros 20 términos.

# # 3. Función usando Programación Dinámica
# def fibonacci_dp(n):
#     # Función que usa programación dinámica para generar la secuencia de Fibonacci.
#     # Verifica si n es 0.
#     if n == 0:
#         return []  # Devuelve una lista vacía si n es 0.
#     # Verifica si n es 1.
#     elif n == 1:
#         return [0]  # Devuelve solo el primer número de la secuencia.
#     # Verifica si n es 2.
#     elif n == 2:
#         return [0, 1]  # Devuelve los dos primeros números de la secuencia.
    
#     fib_sequence = [0, 1]  # Inicializa la lista con los dos primeros números.
    
#     # Itera desde 2 hasta n-1.
#     for i in range(2, n):
#         # Cada nuevo número es la suma de los dos anteriores.
#         next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
#         # Agrega el nuevo número a la lista.
#         fib_sequence.append(next_fib)
        
#     return fib_sequence  # Devuelve la secuencia generada.

# # Pruebas del código de programación dinámica
# print("\nFibonacci Programación Dinámica:")
# # Imprime la secuencia de Fibonacci para n = 10.
# print(fibonacci_dp(10))  # Debería imprimir [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# # Imprime la secuencia de Fibonacci para n = 20.
# print(fibonacci_dp(20))  # Debería imprimir los primeros 20 términos.

# # 4. Generador
# def fibonacci_generador(n):
#     # Generador para producir la secuencia de Fibonacci.
#     a, b = 0, 1  # Inicializa los dos primeros números.
#     # Itera desde 0 hasta n.
#     for _ in range(n):
#         yield a  # Devuelve el número actual.
#         # Actualiza los valores de a y b.
#         a, b = b, a + b

# # Uso del generador
# print("\nFibonacci Generador:")
# # Itera sobre los números generados y los imprime.
# for num in fibonacci_generador(10):
#     print(num, end=' ')  # Imprime: 0 1 1 2 3 5 8 13 21 34
# print()  # Nueva línea.