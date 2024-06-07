import math
a = float(input('digite: '))
b = float(input('digite: '))
hipo = (a**2) + (b**2) 
raiz = math.sqrt(hipo)
print(f'A hipotenusa dos catetos {a} e {b} é: {raiz}')

# outra maneira de fazer é utilizando a função do modulo math.hypot (para calcular a hipotenusa)
# hipo = math.hypot(a, b)
