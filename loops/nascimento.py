from datetime import date 
contmaior = 0
contmenor = 0
atual = date.today().year
for contar in range(1, 8):
    data = int(input('Digite o ano do seu nacimento:  '))
    idade = atual - data
    if idade >= 18:
        contmaior +=1
    else:
        contmenor +=1
print(f'Há {contmaior} pessoas maiores de 18')
print(f'Há {contmenor} pessoas menores de 18')



