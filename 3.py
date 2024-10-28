# Realizar una suma de los elementos de una tupla
def sum_tuple(tuple):
    return sum(tuple)

# Tupla de prueba
t = (1, 2, 3, 4, 5)

# Llamada a la función y muestra del resultado
print(f"La suma de los elementos de la tupla {t} es: {sum_tuple(t)}")


# Diferencias entre Tuplas y Arrays en Python

# 1. Definición
# Tupla: Colección inmutable de elementos. Se define con ().
# Array: Estructura mutable que almacena elementos del mismo tipo. Se puede usar 'array'.

# 2. Mutabilidad
# Tuplas: Inmutables. No se pueden modificar.
# Arrays: Mutables. Se pueden cambiar y manipular.

# 3. Tipos de Elementos
# Tuplas: Pueden tener diferentes tipos de elementos.
# Arrays: Generalmente solo del mismo tipo.

# 4. Rendimiento
# Tuplas: Más ligeras y rápidas para operaciones simples.
# Arrays: Eficientes para cálculos y manipulación de datos.

# 5. Métodos
# Tuplas: Métodos limitados (count(), index()).
# Arrays: Más métodos disponibles, especialmente con NumPy.
