# from random import randint
# cont = 0
# computador = randint(1, 10)

# acertou = False
# while not acertou:
#     num = int(input('Digite um numero de 0 a 10: '))
#     if num == computador:
#         acertou = True
#         cont += 1
#     else:
#         if num < computador:
#             print('Chute mais alto...')
#             cont += 1
#         else:
#             print('Chute mais baixo...')
#             cont += 1
# print(f'Acertou na posição de numero {cont}°')        





# from random import randint
# cont = 0
# computador = randint(1, 10)
# num = int(input('Digite um numero de 0 a 10: '))
# acertou = False
# while not acertou:
#     if num == computador:
#         acertou = True
#     else:
#         if num < computador:
#             print('Chute mais alto...')
#         else:
#             print('Chute mais baixo...')
# print(f'Acertou na posição de numero {cont}°')        







from random import randint
cont = 0
computador = randint(1, 10)
while True:
    num = int(input('Digite um numero de 0 a 10: '))
    if num == computador:
        cont += 1
        break
    else:
        if num < computador:
            print('Chute mais alto...')
            cont += 1
        else:
            print('Chute mais baixo...')
            cont += 1
print(f'Acertou na posição de numero {cont}°')        