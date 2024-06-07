import random
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
alunos = random.choice(lista)
print(f'O Aluno(a) escolhido a apagar a lousa é o(a): {alunos} ')
# A choice é a função de escolher um na lista. Utilizado no modulo random