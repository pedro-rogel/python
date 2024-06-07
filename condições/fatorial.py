# from math import factorial
# n = int(input('Digite seu numero: '))
# fatorial = factorial(n)
# print(f'O fatorial de {n} é {fatorial}')

# n = int(input('Digite seu numero: '))
# cont = n
# fatorial = 1
# while cont > 0:
#     print(cont, end='')
#     print(' x ' if cont > 1 else ' = ', end='')
#     fatorial *= cont
#     cont -= 1
# print(f'{fatorial}')

n = int(input('Digite aqui seu numero: '))
fatorial = 1
cont = n
for numero in range(1, n+1):
    fatorial *= numero
    print(cont, end='')
    print(' x ' if cont > 0 else ' = ', end='')
    cont -= 1
print(fatorial)
