# Dados dos números, escriba un código Python para encontrar el mínimo de estos dos números

def numero_minimo(num1, num2):

    # ternaria en python

    return num1 if num1 < num2 else num2 
    # usando la estructura if-else

    # if num1 < num2:
    #     return num1
    # else:
    #     return num2

num1 = -2
num2 = -5
print(f"El número mínimo de {num1} y {num2} es {numero_minimo(num1, num2)}")