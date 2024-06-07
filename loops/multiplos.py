from random import randint
soma = 0
cont = 0
for  numero in range(1, 500+1, 2):
    if numero % 3 == 0:
        cont += 1
        soma += numero
print(f'A soma dos {cont} numeros é {soma}')

