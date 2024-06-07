num = 0
cont = 0
soma = 0
num = int(input('Digite um numero aleatorio [se quiser parar, digite 999]: ')) 
while num != 999:
   cont += 1
   soma += num 
   num = int(input('Digite um numero aleatorio [se quiser parar, digite 999]: ')) 
print(f'Foram digitados {cont} nunmeros e a soma deles é {soma}')