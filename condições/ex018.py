nome = input('Digite seu nome completo: ').strip() # utilizado para tirar os espaços do começo e do final
maiuscula = nome.upper() # tudo em maiusculo
minuscula = nome.lower() # tudo em minusculo
carcteres = len(nome) - nome.count(' ') # utilizado para tirar TODOS os espaços, sem exceção (espaço do meio, como por exeplo) 
primero_nome = nome.split() # usei o split para separar ex: 'pedro'  'henrique'...
print(f'O Seu nome em maiusculas é: {maiuscula}')
print(f'O seu nome em minusculas é: {minuscula}')
print(f'A quantidade de letras sem contar espaços é: {carcteres}')
print(f'O seu primeiro nome há {primero_nome[0], len(primero_nome[0])} letras')