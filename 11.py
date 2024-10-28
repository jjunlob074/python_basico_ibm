# Escribir un algoritmo de ordenación para un conjunto de datos numéricos en Python.

lista = [5, "8", 4, "1"]
print("Valores originales y sus tipos:")
for num in range(len(lista)):
    print(f" - Valor: {lista[num]}, Tipo: {type(lista[num])}")  # Muestra el valor y su tipo

    lista[num] = int(lista[num])  # Convierte cada elemento a entero

    print(f" - Valor convertido: {lista[num]}, Tipo: {type(lista[num])}")  # Muestra el valor convertido y su tipo

# Ordena la lista
lista.sort()  
print("\nLista ordenada:")
print(lista)  # Imprime la lista ordenada
