nome = input('Digite seu nome completo: ').strip().split()
print(f'O seu primeiro nome é {nome[0]}')
print(f'O seu ultimo nome é {(nome[len(nome)-1])}')
print(len(nome))