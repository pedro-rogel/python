from datetime import date
def votar(n):
    atual = date.today().year
    idade = atual - n
    if 18 <= idade <= 65:
        print(f' Você tem {idade} anos, entao o seu voto é Obrigatorio!!')
    elif 16 <= idade < 18 or idade >= 65:
        print(f' Você tem {idade} anos, então o seu voto é Opcional!!')
    else:
        print(f' Você tem {idade} anos, então o seu voto está Negado!')

n = int(input('Digite o ano no seu nascimento: '))
votar(n)