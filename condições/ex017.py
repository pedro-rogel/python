import random 
al1 = input('Nome: ')
al2 = input('Nome: ')
al3 = input('Nome: ')
al4 = input('Nome: ')
lista = [al1, al2, al3, al4]
random.shuffle(lista)
print(f'A ordem dos alunos que irão apresetar é: {lista}')
# shuffle é a função de embaralhar no modulo random 