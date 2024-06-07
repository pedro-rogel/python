primeiro = int(input(': '))
razao = int(input(': '))
termo = primeiro
cont = 1
while cont <= 10:
    print(termo, '-> ', end='')
    termo += razao
    cont += 1
print('FIM')