# Escriba un código que pueda contar todas las palabras mayúsculas de un archivo.

def count_uppercase_words(file_path):
    # Leer el contenido del archivo y contar las palabras mayúsculas
    with open(file_path, 'r') as file:
        return sum(1 for word in file.read().split() if word.isupper())

# Prueba del código
file_path = '6.txt'
uppercase_count = count_uppercase_words(file_path)
print(f"El archivo '{file_path}' tiene {uppercase_count} palabras mayúsculas.")

# Nota: Este código requiere que el archivo exista en el mismo directorio que el script.
