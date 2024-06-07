def maior(*n):
    cont = 0
    maior = 0
    for valor in n:
        if cont == 0:
            maior = valor
        elif valor > maior:
            maior = valor
        cont += 1
    print(f'foram informados {cont} valores e o maior valor é {maior}')


maior(1,7,85)