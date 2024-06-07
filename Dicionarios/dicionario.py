dados = dict()
dados['nome'] = input('Seu nome: ')
dados['media'] = float(input('Digite sua média: '))
if dados['media'] < 6:
    dados['situação'] = 'Reprovado'
else:
    dados['situação'] = 'Aprovado'
# print(f'Nome: {dados["nome"]}')
# print(f'Média de {dados["nome"]}: {dados["media"]}')
# print(f'Situação: {dados["situação"]}')
for chave, valor in dados.items():
    print(f'{chave} recebe {valor}')