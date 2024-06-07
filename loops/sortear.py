from random import choice
lista = []
nome = (input('Digite alguns nomes: '))
conti = input('Quer contiuar? [S/N]: ').upper()
cont = 1
lista.append(nome)
while True:
    if conti == 'S':
        nome = input('Digite alguns nomes: ')
        conti = input('Quer contiuar? [S/N]: ').upper()
        lista.append(nome)
        cont += 1
    else:
        break
lista.append(nome)
sorteado = choice(lista)
print(f'O escolhido dos {cont} participantes é o: {sorteado} ')