# SEQUENCIA DE FIBONACCI
n = int(input('Quantos termos você quer mostrar?: ')) #primeiro ira pergintar quantos termos o usuario quer ver
t1 = 0 # na sequencia de fibonacci, ja começa com o termo zero e comm o termo um
t2 = 1 # na sequencia de fibonacci, ja começa com o termo zero e comm o termo um
cont = 3 #começando o contador com o termo 3 pois ja vimos que o termo 1 é o 0 e o termo 2 é o 1
while cont <= n: # Enquanto o contador for menor ou igual ao numero inserido pelo usuario:
    sequencia = t1 + t2 # a sequencia mostrara a soma do primeiro termo com o segundo para formar o terceiro
    t1 = t2 # para continuar a sequencia, vamos passar o valor dos termos para 'frente' t1 recebe t2 e t2 recebe sequencia. Assim seguira até o cont ficar maior do que o n
    t2 = sequencia
    print(sequencia, '-> ', end='')
    cont += 1 # o cont vai aumentando até chegar no numero do usuario 
print('FIM', end='')