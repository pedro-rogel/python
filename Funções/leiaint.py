def leiaint(txt):
    ok = False
    valor = 0
    while True:
        n = input(txt)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro! Digite um numero inteiro válido!')
        if ok:
            break
    return valor


n = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')
