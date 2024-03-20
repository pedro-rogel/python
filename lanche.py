pedido, quantidade = input("Digite o número do seu lanche aqui e ao lado a quantidade que deseja: ") .split()
pedido = int(pedido)
quantidade = int(quantidade)
if pedido == 1:
   total = (quantidade * 4)
   print(f'Total: R$ {total:.2f}')
elif pedido == 2:
    total = (quantidade * 4.5)
    print(f'Total: R$ {total:.2f}')
elif pedido == 3:
    total = (quantidade * 5)
    print(f'Total: R$ {total:.2f}')
elif pedido == 4:
    total = (quantidade * 2)
    print(f'Total: R$ {total:.2f}')
elif pedido == 5:
    total = (quantidade * 1.5)
    print(f'Total: R$ {total:.2f}')
    