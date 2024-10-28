# ¿Cuál es el resultado de ejecutar el siguiente código?
try:
    if '1' != 1:
        raise "algún error"
    else:
        print("no se ha producido ningun error")
except "algún error":
    print(f"Se ha producido un error")
    

# En este código, se producen errores debido a que se intenta lanzar y capturar 
# una excepción usando una cadena de texto, lo cual no es válido en Python. 
# Las excepciones deben ser instancias de clases que heredan de BaseException.
# 
# 1. En la línea `raise "algún error"`, se intenta lanzar una cadena como si 
#    fuera una excepción. Esto provoca un TypeError porque las excepciones 
#    deben ser instancias de clases que heredan de BaseException, como 
#    ValueError o Exception.
# 
# 2. En la línea `except "algún error":`, se intenta capturar una excepción 
#    usando una cadena de texto. Al igual que con `raise`, esto causa un 
#    TypeError porque `except` solo puede capturar instancias de excepciones, 
#    no cadenas.
# 
# Para corregir el código, se deben usar excepciones adecuadas como 
# ValueError o Exception para lanzar y capturar errores correctamente.
