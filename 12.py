#  ¿Cuál de las siguientes declaraciones es inválida?

# a) abc = 1.000.000
abc = 1.000.000  # Esto es válido en Python(sólo con un punto, con dos peta), pero es una mala práctica. Python interpreta 1.000.000 como 1.0, ya que los puntos se usan como separadores de decimales en muchos lenguajes. En Python, debemos usar la notación científica o sin puntos, es decir, 1000000 o 1e6.
# b) a b b c = 1000 2000 3000
a b b c = 1000 2000 3000 # Esta declaración es inválida porque no se pueden usar espacios en los nombres de variables. En Python, un nombre de variable no puede contener espacios. Debería ser algo como 'a_b_b_c = 1000, 2000, 3000'.

# c) a,b,c = 1,000,000
a, b, c = 1,000,000  # Esto es válido pero confuso. La asignación de tuplas en Python no permite comas en los números como separadores de miles. La forma correcta sería usar 1_000_000 (que es una forma válida para números grandes en Python 3.6+). Por lo tanto, esto generará un error.

# d) a_b_c = 1,000,000
a_b_c = 1_000_000  # Esta declaración es válida. Python permite usar guiones bajos en los nombres de variables, y también se pueden usar guiones bajos para mejorar la legibilidad de los números, como en 1_000_000.
