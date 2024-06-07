from datetime import date
sexo = input('Qual é o eu sexo? M ou F?: ').strip()
if sexo == 'M' or 'm': 
    nascimento = int(input('Ano de nascimento: '))
    atual = date.today().year
    idade = (atual - nascimento)
    print(f'Você tem {idade} anos')
    if idade < 18:
        print(f'Ainda falta {18 - idade} ano(s) para você se alistar')
        ano = atual + (18 - idade)
        print(f'Seu alistamento será em {ano}')
    elif idade == 18:
        print(f'Parabens! Esse é o seu ano de alistamento!')
    elif idade > 18: 
        ano = atual - (idade - 18)
        print(f'É preciso se alistar, meu caro! Já se passaram {idade - 18} ')
        print(f'Erá para você ter se alistado em {ano}')
else: 
    print('Vai lavar louça kkk')