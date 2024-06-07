from time import sleep
n = int(input('Digite seu numero aqui: '))
for contar in range(0, n+1):
    if contar % 2 ==0:
        print(contar)
        sleep(1)
        