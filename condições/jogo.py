from random import randint
from time import sleep
computador = randint(0, 5) # comando para escolher um numro inteiro aleatorio entre 0 and 5
entrada = int(input('Descubra o numero que a maquina está pensando entre 0 e 5: '))
print('Processando...')
sleep(2)
if entrada == computador:
    print(f'Você Venceu!\nA maquina pensou em {computador} e você digitou {entrada}')
else:
    print(f'A maquina te venceu!\nEla pensou em {computador} e você digitou {entrada}')
