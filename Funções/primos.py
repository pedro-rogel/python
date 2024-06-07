def primo(n):
    qtd = 0 
    p = 1
    while p <= n:
        if n % p == 0:
            qtd += 1
        p +=1 
    if qtd == 2:
        return True
    else:
        return False    
    
n = int(input('Digite seu numero: '))
r = primo(n)
if r: 
    print(f'{n} é primo')
else:
    print(f'{n} não é primo')