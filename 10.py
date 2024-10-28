# Escribir un programa en Python para comprobar si un número es capicúa. Es decir, si se lee igual de derecha a izquierda que de izquierda a derecha.

def es_capicua(n):
    # Convertimos el número a una cadena para facilitar la lectura de sus dígitos // GRACIAS A QUE PYTHON ES DEBILMENTE TIPADO!!!
    num_str = str(n)
    
    # Compara la representación en cadena del número con su reverso; si son iguales, el número es capicúa (se lee igual de izquierda a derecha que de derecha a izquierda).
    return num_str == num_str[::-1]

# Pruebas del programa
numeros = [121, 233, 1001, 9889, 12321,12322]

for num in numeros:
    print(f"{num} es capicúa: {es_capicua(num)}")
    