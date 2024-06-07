num = int(input('Digite seu numero: '))
pg = input('Quer continuar? [S/N]: ').upper() .strip()
cont = 1 
tot = 1
maior = 1
menor = 1
while True:
    if pg == 'S':
        num = int(input('Digite seu numero: '))
        pg = input('Quer continuar? [S/N]: ').upper() .strip()
        cont += 1
        tot += num
    else:
        break
    if num > maior:
        maior = num 
    elif num < maior:
        menor = num
    media = tot / cont
print(f'A média dos {cont} numeros digitados, é: {media}')
print(f'O maior numero é {maior} e o menor é {menor}')