pessoa = dict()
lista = list()
soma = 0; media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    pessoa['idade'] = int(input('Idade: '))
    while True:
        pessoa['sexo'] = input('Sexo [M/F]: ').upper()
        if pessoa['sexo'] in 'MF':
            break
    soma += pessoa['idade']
    lista.append(pessoa.copy())
    pergunta = input('Quer Continuar? [S/N]: ').upper()
    if pergunta in 'N':
        break
media = soma / len(lista)
print(lista)
print(f'Ao todo, temos {len(lista)} pessoas cadastradas!')
print(f'A média das idades é {media:.2f}')
print(f'As mulheres cadasradas são: ')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='|')
print()
print(f'As pessoas que estão com a idade acima da média são: ')
for p in lista:
    if p['idade'] >= media:
        print(f'{p["nome"]} ', end='|')
