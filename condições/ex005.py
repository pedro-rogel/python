metros = int(input('Digite aqui em metros: '))
centimetros = metros * 100
milimetros = centimetros * 100 or metros * 1000 
print(f'{metros} metros tem {centimetros} centimetros')
print(f'{metros} metros tem {milimetros} milimetros')