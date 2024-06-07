altura = float(input('Digite a altura em metros: '))
largura = float(input('Digite a largura em metros: '))
area = altura * largura
volume = area * altura
pintar = volume / 2**2
print(f'A area da parede é de {area} e é preciso de {pintar} litros para pintar a parede toda.')
