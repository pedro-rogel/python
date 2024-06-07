num = int(input('Digite um numero: '))
print('Escolha uma das basespara conversão:\n[1] Converter para Binario\n[2] Converter para OCTAL\n[3] Converter para HEXADECIMAL')
op = int(input('Sua opção: '))
if op == 1:
    conversao = bin(num)
    print(f'{num} convertido em binario fica: {conversao[2:]}')
elif op == 2:
    conversao = oct(num)
    print(f'{num} convertido para OCTAL fica: {conversao[2:]}')
elif op == 3:
    conversao = hex(num)
    print(f'{num} convertido para HEXADECIMAL fica: {conversao[2:]}')
else: 
    print(f'Opção invalida!')