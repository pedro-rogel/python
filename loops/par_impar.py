from random import randint
while True:
    pg = input('Você quer ser par ou impar? [P/I]: ').upper()
    jogador = int(input('Digite um numero: '))
    computador = randint(0, 10)
    total = jogador + computador
    if pg == 'P':
        if total % 2 == 0:
            print(f'Jogador Ganhou! Ele escolheu {jogador} e o computador escolheu {computador} ')
            print(f'A soma é {total}')
        else:
            print(f'Computador ganhou! Jogador escolheu {jogador} e o computador escolheu {computador}')
            print(f'A soma é {total}')
    if pg == 'I':
        if total % 2 == 1:
            print(f'Jogador Ganhou! Ele escolheu {jogador} e o computador escolheu {computador} ')
        else:
            print(f'Computador ganhou! Jogador escolheu {jogador} e o computador escolheu {computador}')
            print(f'A soma é {total}')
    pg2 = input('Quer continuar? [S/N]: ').upper()
    if pg2 == 'N':
        break
