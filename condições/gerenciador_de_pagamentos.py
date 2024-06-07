i = '=' * 10
print(i,"ROGELS'S STORES", i)
compras = float(input('Valor das compras: R$ '))
p = ('formas de pagamento:').upper()
print(p)
print('''
[1] à vista no dinheiro
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
op = int(input('Qual é a opção?: '))
if op == 1:
    valor1 = compras * (1 - 0.10)
    print(f'O novo valor a ser pago é {valor1}')
elif op == 2:
    valor1 = compras * (1 - 0.5)
    print(f'O novo valor a ser pago é {valor1}')
elif op == 3:
    valor1 = compras
    parcela = valor1 / 2
    print(f'Sua compra será parcelada em 2x de {parcela} ')
elif op == 4:
    valor1 = compras * (1 + 0.20)
    totalvalor = int(input('Quantas parcelas? '))
    parcela = valor1 / totalvalor
    print(f'Sua compra será parcelada em {totalvalor} de {parcela} ')

# i = '=' * 10
# print(i, "ROGELS'S STORES", i)
# compras = float(input('Valor das compras: R$ '))
# p = ('formas de pagamento:').upper()
# print(p)
# print('''
# [1] à vista no dinheiro
# [2] à vista no cartão
# [3] 2x no cartão
# [4] 3x ou mais no cartão''')
# op = int(input('Qual é a opção?: '))

# if op == 1:
#     valor1 = compras * (1 - 0.10)
#     print(f'O novo valor a ser pago é {valor1}')
# elif op == 2:
#     valor1 = compras * (1 - 0.5)
#     print(f'O novo valor a ser pago é {valor1}')
# elif op == 3:
#     valor1 = compras
#     parcela = valor1 / 2
#     print(f'Sua compra será parcelada em 2x de {parcela} ')
# elif op == 4:
#     valor1 = compras * (1 + 0.20)
#     totalvalor = int(input('Quantas parcelas? '))
#     parcela = valor1 / totalvalor
#     print(f'Sua compra será parcelada em {totalvalor} de {parcela} ')
