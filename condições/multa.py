km = float(input('Digite a sua velocidade: '))
if km > 80:
    valor = 7.00
    multa = (km - 80) * 7
    print(f'você foi multado e terá que pagar {multa}')
else:
    print(f'Você não foi multado!')