jogador = dict()
lista = []
time = []
while True:
    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ')
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou?:  '))
    lista.clear()
    for partidas in range(0, jogador['partidas']):
        lista.append(int(input(f'Quantos gols na {partidas + 1} partida? ')))
    jogador['gols'] = lista[:]
    jogador['total'] = sum(lista)
    time.append(jogador.copy())
    while True:
        r = input('Quer Continuar?[S/N]: ').upper()[0]
        if r in 'SN':
            break
        print('Responda apenas com S ou N!')
    if r == 'N':
        break
print()
print('cod ' , end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for chave, valor in enumerate(time):
    print(f'{chave:>3} ', end='')
    for d in valor.values():
        print(f'{str(d):<15}', end='')
    print()
print()
while True:
    busca = int(input('Mostrar dados de qual jogador?[999 para parar]: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe nenhum jogador com o codigo {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for indice, gols in enumerate(time[busca]['gols']):
            print(f'No jogo {indice + 1} fez {gols} gols')
        print()
print(f'Volte sempre!!!')