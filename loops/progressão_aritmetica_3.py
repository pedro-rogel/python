primeiro = int(input(': '))
razao = int(input(': '))
termo = primeiro
cont = 1
tot = 0 
mais = 10
while mais != 0:
    tot += mais
    while cont <= tot:
        print(termo, '-> ', end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {tot} termos mostrados')
