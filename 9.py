def es_primo(n):
    """
    Comprueba si un número es primo.

    Un número primo es mayor que 1 y solo es divisible por 1 y por sí mismo.

    Parámetros:
    n (int): El número a comprobar.

    Retorna:
    bool: True si n es primo, False de lo contrario.
    """
    # Si el número es menor que 2, no puede ser primo
    if n < 2:
        return False
    
    # Itera desde 2 hasta la raíz cuadrada de n (inclusive) porque cualquier divisor de n debe ser menor o igual a su raíz cuadrada; esto optimiza la búsqueda de divisores.
    for i in range(2, int(n**0.5) + 1):
        # Si n es divisible por i, entonces no es primo
        if n % i == 0:
            return False
    
    # Si no se encontró ningún divisor, n es primo
    return True

# Pruebas del código
numeros_a_probar = [17, 18, 1, 2, 3, 4]
for num in numeros_a_probar:
    resultado = es_primo(num)
    print(f"¿Es {num} primo? {'Sí' if resultado else 'No'}")
