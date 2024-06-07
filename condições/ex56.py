'''soma_idade = 0  
media_idade = 0
maior_homem = 0
nome_maior ='' 
totmulher20 = 0
for pessoas in range(1, 5):
    print(f'{'-'*10}{pessoas} PESSOA {'-' * 10}')
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite o seu sexo [M/F]: ').strip()
    if pessoas == 1 and sexo in 'Mm':
        maior_homem = idade
        nome_maior = nome
    if sexo in 'Mn' and idade > maior_homem:
        maior_homem = idade
        nome_maior = nome
        soma_idade += idade
    if sexo in 'Fm' and idade < 20:
        totmulher20 +=1
media_idade = soma_idade /4
print(f'A média das idades é: {media_idade}')
print(f'O homem mais velho se chama {nome_maior} e ele tem {maior_homem} anos')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')'''

pessoas =[]
homem_velho = {'nome': '', 'idade': 0}
totmulheres_menor20 = 0
for pessoa in range(4):
    x = '=' * 10
    print(x,'pessoa',x)
    nome = input('Nome: ').capitalize() #estava errando aqui
    idade = int(input('Idade '))
    sexo = input('M/F: ').upper()
    if sexo == 'M' and idade > homem_velho['idade']:
        homem_velho['nome'] = nome
        homem_velho['idade'] = idade
    if sexo == 'F' and idade < 20:
        totmulheres_menor20 += 1
    pessoas.append({'nome' : nome, 'idade': idade, 'sexo': sexo})

soma_idades = sum(pessoa['idade'] for pessoa in pessoas)
media_idade = soma_idades/len(pessoas)
print(f'A média das idades são: {media_idade:.2f}')
print(f'Nome do homem mais velho é {homem_velho['nome']} e ele tem {homem_velho['idade']} anos')
print(f'O total de mulheres com menos de 20: {totmulheres_menor20}')

# # Lista para armazenar as informações das pessoas
# pessoas = []
# homem_mais_velho = {'nome': '', 'idade': 0}
# total_mulheres_menos_20 = 0

# # Loop para coletar informações das 4 pessoas
# for i in range(4):
#     print(f"Digite as informações da {i+1}ª pessoa:")
#     nome = input("Nome: ")
#     idade = int(input("Idade: "))
#     sexo = input("Sexo (M/F): ").upper()

#     # Verificar se é o homem mais velho
#     if sexo == 'M' and idade > homem_mais_velho['idade']:
#         homem_mais_velho['nome'] = nome
#         homem_mais_velho['idade'] = idade

#     # Contar mulheres com menos de 20 anos
#     if sexo == 'F' and idade < 20:
#         total_mulheres_menos_20 += 1

#     # Adicionar informações à lista de pessoas
#     pessoas.append({'nome': nome, 'idade': idade, 'sexo': sexo})

# # Calcular média de idade do grupo
# soma_idades = sum(pessoa['idade'] for pessoa in pessoas)
# media_idade = soma_idades / len(pessoas)

# # Exibir resultados
# print("\nResultados:")
# print(f"Média de idade do grupo: {media_idade:.2f} anos")
# print(f"Nome do homem mais velho: {homem_mais_velho['nome']} (idade: {homem_mais_velho['idade']} anos)")
# print(f"Total de mulheres com menos de 20 anos: {total_mulheres_menos_20}")
