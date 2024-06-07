from random import randint
from time import sleep
itens =('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas Opções:
    [0] Pedra
    [1] Papel
    [2] Tesoura''')
jogador = int(input('Qual é a sua jogada?: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔÔ')
print('---'*10)
print(f'Computador Jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('---'*10)
if computador == 0 and jogador == 0:
    print('Empate')
elif computador == 0 and jogador == 1:
    print('Jogador Ganhou')
elif computador == 0 and jogador == 2:
    print('Computador Ganhou')
elif computador == 1 and jogador == 0:
    print('Computador Ganhou')
elif computador == 1 and jogador == 1:
    print('Empate')
elif computador == 1 and jogador == 2:
    print('Jogador Ganhou')
elif computador ==2 and jogador == 0:
    print('Jogador Ganhou')
elif computador ==2 and jogador == 1:
    print('Computador Ganhou')
elif computador == 2 and jogador ==2:
    print('Empate')