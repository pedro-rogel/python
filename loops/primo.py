n = int(input('Digite: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[m', end='')
        tot +=1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print(f'\n\033[mO numero {n} foi divisivel {tot} vezes')
if tot == 2:
    print('Ele é primo')
else:
    print('Ele não é primo')