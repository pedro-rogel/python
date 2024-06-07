soma = 0
cont = 0
for numeros in range(0, 6):
    n = int(input('Digite: '))
    if n % 2 == 0:
        soma += n
        cont +=1
print(f'Dos {cont} numeros pares, a soma foi {soma}')
