num = int(input('Digite um numero: '))
if num >= 1 and num <= 1000:
    for num in range(1, num+1):
        if num % 2 == 1:
            print(num)