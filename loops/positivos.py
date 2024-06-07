positivos = 0
negativo = 0  
for mais in range(6):
    valor = float(input('Digite um numero: '))
    if valor > 0:
        positivos +=1 
    elif valor < 0:
        negativo +=1
print(f'Há {positivos} valores positivos.')
print(f'Há{negativo} valores negativos.')




"""positivos = 0

for _ in range(6):  # Loop para ler 6 valores
    valor = float(input('Digite um valor: '))  # Leitura do valor como um número de ponto flutuante
    if valor > 0:  # Verifica se o valor é positivo
        positivos += 1  # Incrementa o contador de valores positivos

print(positivos, "valores positivos")  # Imprime a quantidade de valores positivos lidos"""
