# def mensagem(msg):
#     print('-'*5)
#     print(msg)
# mensagem('oi,...')   
# print('pedro')
# mensagem('oi,...')
# print('joao')
# mensagem('oi,...')
# print('cleber')
def tabuada(x):
    for i in range(11):
        valor = x * i
        print(f'{x} x {i} = {valor}')
        

x = int(input('Digite  numero da tabuada que você quer saber:'))
print(tabuada(x))