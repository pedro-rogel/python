"""x = int(input('Dgite um numero para saber os 6 numeros impares sucessores: '))
if x % 2 == 0:
    x1 = x+1 
    print(x1)
    x2 = x+3
    print(x2)
    x3 = x+5
    print(x3)
    x4 = x+7
    print(x4)
    x5 = x+9
    print(x5)
    x6 = x+11
    print(x6)
elif x % 2 ==1: 
    x1 = x+2 
    print(x1)
    x2 = x+4
    print(x2)
    x3 = x+6
    print(x3)
    x4 = x+8
    print(x4)
    x5 = x+10
    print(x5)
    x6 = x+12
    print(x6)"""

"""x = int(input('Dgite um numero para saber os 6 numeros impares sucessores: '))
if x % 2 == 0:
   x+=1
   print(x)
   x+=2
   print(x)
   x+=2
   print(x)
   x+=2
   print(x)
   x+=2
   print(x)
   x+=2
   print(x)
elif x % 2 ==1: 
    x +=2
    print(x)
    x+=2
    print(x)
    x+=2
    print(x)
    x+=2
    print(x)
    x+=2
    print(x)
    x+=2
    print(x) """


'''x = int(input('Digite um número para saber os 6 números ímpares sucessores: '))

if x % 2 == 0:  # Se o número fornecido for par
    for _ in range(6):  # Loop para imprimir os próximos 6 números ímpares
        x += 1  # Incrementa para o próximo número ímpar
        print(x)

elif x % 2 == 1:  # Se o número fornecido for ímpar
    for _ in range(6):  # Loop para imprimir os próximos 6 números ímpares
        print(x)
        x += 2  # Incrementa para o próximo número ímpar'''

'''x = int(input())
if x % 2 == 0:
   x+=1
   print(x)
   x+=2
   print(x)
   x+=2
   print(x)
   x+=2
   print(x)
   x+=2
   print(x)
   x+=2
   print(x)
elif x % 2 ==1: 
    for ler in range(6):
        x+=2
        print(x)'''
x= int(input("Digite um número inteiro positivo: "))

# Se x é par, incrementamos para o próximo ímpar
if x % 2 == 0:
    x += 1

# Imprimimos os próximos 6 números ímpares
for _ in range(6):
    print(x)
    x += 2
