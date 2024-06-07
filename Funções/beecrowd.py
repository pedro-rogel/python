def soma_impares(x,y):
    menor = min(x, y)
    maior = max(x,y)
    soma = 0
    for numero in range(menor, maior+1):
        if numero % 2 != 0:
            soma += numero
    return soma
    
x = int(input('Digite: ')) 
y = int(input('Digite: ')) 
resultado = soma_impares(x,y)
print(resultado)
