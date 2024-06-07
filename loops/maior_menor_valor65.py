continuar = 'S'
cont = 0  
maior = 0
menor = 0 
lista = []
while continuar == 'S':
    num = int(input('Digite: '))
    continuar = input('Quer continuar?[S/N]: ').upper()
    cont += 1
    lista.append(num)
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    
media = sum(lista) / cont # sum é utilizado para somar todos os numero dentro de uma lista
print(lista)
print(media)
print(cont)
print(f'Maior numero da lista: {maior}')
print(f'Menor numero da lista: {menor}')


# para fazer sem a função sum 
# soma = 0 
# for numero in lista:
#     soma += numero
# print(soma)   