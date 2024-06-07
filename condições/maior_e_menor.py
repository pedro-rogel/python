'''for ler in range(3):
    num = int(input('Digite aqui 3 valores:'))
    if num > num '''
a = int(input('Primeiro Valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro Valor: '))
if a<b and a<c:
    menor = a
elif b<a and b<c:
    menor = b
elif c<a and c<b:
    menor = c
if a>b and a>c:
    maior = a
elif b>a and b>c:
    maior = b
elif c>a and c>b:
    maior = c
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')