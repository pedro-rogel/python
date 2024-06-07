numeros = list(map(int,input('Digite aqui três valores: ') .split()))
numeros_ordem = sorted(numeros)
for numero in numeros_ordem:
    print(numero)
    
print()

for numero in numeros:
    print(numero)