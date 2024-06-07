from random import randint
from time import sleep
from operator import itemgetter
dados = {'jogador_1': randint(0, 10), 'jogador_2': randint(0, 10), 'jogador_3': randint(0, 10), 'jogador_4' : randint(0, 10)}
ranking = list()
for chave, valor in dados.items():
    print(f'O {chave} tirou {valor}')
    sleep(1.0)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True )
print()
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')

