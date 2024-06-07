from datetime import datetime
pessoa = dict()
pessoa['nome'] = input('Nome: ')
nascimento = int(input('Ano de nascimento: '))
pessoa['idade'] = datetime.now().year - nascimento
pessoa['ctps'] = int(input('Carteira de trbalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contrato'] = int(input('Ano de contração: '))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contrato'] + 35) - datetime.now().year)
    pessoa['salario'] = int(input('Salário: R$'))
    for chave, valor in pessoa.items():
        print(f'{chave} tem valor {valor}')

else:
    for chave, valor in pessoa.items():
        print(f'{chave} tem valor {valor}')

