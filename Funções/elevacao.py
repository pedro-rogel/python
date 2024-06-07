def elevacao (x,y):
    ele = x **y
    return ele
entrada = int(input('Digite aqui: '))
for ler in range(1, entrada + 1):
    if ler % 2 == 0:
        quadrado = elevacao(ler,2)
        print(f'{ler}^2 = {quadrado}')