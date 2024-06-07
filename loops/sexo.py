sexo = input('Digite seu sexo: ').upper()
while True :
    if sexo == 'M' or sexo == 'F':
        break
    else:
        sexo = input('Dados inválidos! Digite seu sexo: ').upper()
print(f'Seu sexo é :{sexo}')