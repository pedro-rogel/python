from math import factorial
def fatorial(n, re):
    result = factorial(n)
    if re == 1:
        for i in range(n, 0, -1):
            if i > 1:
                print(f'{i} x ', end='')
            else:
                print(f'= {result}')
    elif re == 2:
        print(result) 
    else:
        print('Não existe essa opção!')
    
            

n = int(input('Digite um numero para saber o fatorial dele: '))
re = int(input('''
Quer ver a resposta com a 
conta completa ou só o resultado? 
[1 para conta completa]
[2 para o resultado sozinho]: '''))
fatorial(n, re)
        