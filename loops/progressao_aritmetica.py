primeiro = int(input(': '))
razao = int(input(': '))
decimo = primeiro + (10 - 1) * razao
for numero in range(primeiro, decimo + razao, razao):
    print(f'{numero}', end=' ')
print('| Acabou')