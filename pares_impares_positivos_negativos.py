positivo = 0
par = 0 
impar = 0
negativo = 0
for ler in range(5):
    valor = float(input('Digite aqui quaisquer numeros distintos: '))
    if valor % 2 == 0: 
        par += 1
    else:
        impar +=1
    if valor > 0:
        positivo += 1
    else:
        negativo += 1
    
print(f'{par} valor(res) par(res)')
print(f'{impar} valor(res) impar(es)')
print(f'{positivo} valor(res) positivo(s)')
print(f'{negativo} valor(res) negativo(s)')