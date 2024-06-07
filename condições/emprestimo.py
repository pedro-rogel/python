nome = input('Digite o seu nome: ')
idade = int(input('Digite sua Idade: '))
renda_mensal = float(input('Digite sua renda mensal: '))

if idade <= 25:
    emprestimo = renda_mensal * 0.5
    print(f'{emprestimo:.2f}')
elif idade <= 35:
    emprestimo = renda_mensal * 0.75
    print(f'{emprestimo:.2f}')
elif idade <= 45:
    emprestimo = renda_mensal
    print(f'{emprestimo:.2f}')
else:
    print(f'Por favor {nome}, peço que entre em contato com o gerente')    