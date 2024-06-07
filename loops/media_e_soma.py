positivos = 0 
soma = 0 
for ler in range(6):
    entrada = float(input('Digite: '))
    if entrada > 0:
        positivos +=1
        soma = soma + entrada # ou soma += entrada
media = soma / positivos
print(f'{positivos} valores positivos')
print(f'{media:.1f}')