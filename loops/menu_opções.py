import os
x = float(input('Digite um numero: '))
y = float(input('Digute outro numero: '))
escolher = 0

while True:
    print('''
       [ 1 ] somar
       [ 2 ] multiplicar
       [ 3 ] maior
       [ 4 ] novos números
       [ 5 ] sair do programa''')
    escolher = int(input('Escolha uma opção: '))
    if escolher == 1:
        soma = x + y
        print(f'{x} + {y} = {soma}')
    elif escolher == 2:
        mult = x * y 
        print(f'O Produto de {x} x {y} = {mult}')
    elif escolher == 3:
        maior = 0 
        if x > y:
            maior += x
            print(maior)
        elif y > x:
            maior += y
            print(maior)
        else:
            print('Os dois numeros são iguais, não há maior e menor')
    elif escolher == 4:
        x = float(input('Digite um numero: '))
        y = float(input('Digute outro numero: '))
    elif escolher == 5:
        os.system('cls')
        print('FIM, VOLTE SEMPRE!')
        break

