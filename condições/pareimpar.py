num = int(input('Digite um numero maior ou igual a 2: '))
if num >=2 and num % 2 == 0 :
    impar_atras = num - 1 
    par_frente = num + 2 
    print(impar_atras, par_frente)
elif num >=2 and num % 2 == 1:
     impar_atras = num - 2
     par_frente = num + 1
     print(impar_atras, par_frente)

