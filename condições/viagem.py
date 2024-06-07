distancia = float(input('Digite a distnacia da sua viagem: '))
if distancia <= 200:
    viagem = distancia * 0.5
else:
    viagem = distancia * 0.45
print(f'De acordo com a sua disntancia de {distancia} Km, você pagará R$ {viagem:.2f} reaisl')