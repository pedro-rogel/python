from datetime import date
nasc = int(input('Qual foi o ano que você nasceu?: '))
atual = date.today().year
idade = atual - nasc
if idade <= 9:
    print(f'Nadador mirim')
elif idade <= 14:
    print(f'Nadador infantil')
elif idade <= 19:
    print(f'Nadador Júnior')
elif idade <= 25:
    print(f'Nadador Sênior')
else: 
    print(f'Nadador Master')
print(f'Você tem {idade} anos')