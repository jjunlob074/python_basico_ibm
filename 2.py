#  Invertir palabras de una cadena dada.
def invert_words(frase):
    print(frase.split()) # crea un array de las palabras
    print(reversed(frase.split())) # Es necesario convertirlo en una lista porque es un objeto iterador 
    print(list(reversed(frase.split()))) # y le invierte el orden iterando sobre él
    words_reversed = reversed(frase.split())  
    return ' '.join(words_reversed) # une de nuevo las palabras en una cadena

# Frase original
frase = 'geeks de prueba de practica de codigo'

resultado = invert_words(frase)
print(f"\nFrase original: {frase}")
print(f"Frase invertida: {resultado}")