maior = 0
menor = 0
posição = 0 
for pesoa in range(1, 6):
    pesos = float(input(f'Peso da {pesoa} pessoa: '))
    if pesoa == 1:
        maior == pesos
        menor == pesos
    else:
        if pesos > maior:
            maior = pesos

        if pesos < maior:
            menor = pesos
print(f'O maior peso pesa {maior} Kg') 
print(f'O menor peso pesa{menor}') 