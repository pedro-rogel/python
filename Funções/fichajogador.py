def ficha(n='<desconhecidos>', g=0):
    print(f'O jogador {n} fez {g} gols no campeonato!')


n = input('Nome jogadoe: ')
gols = input('Numeros de Gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if n.strip() == '':
    ficha(g=gols)
else:
    ficha(n, gols)