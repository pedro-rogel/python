salario  = float(input('Digite seu salario para saber o seu aumento: '))
if salario > 1200:
    aumento = salario * (1 + 0.10)
    print(f'O seu novo salario com 10% a mais é: {aumento}')
else: 
    aumento = salario * (1 + 0.15)
    print(f'O seu novo salario com 15% a mais é: {aumento}')
