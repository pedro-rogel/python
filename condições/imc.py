peso = float(input('Qanto você pesa? (Kg): '))
altura = float(input('Qual é a sua altura? (m): '))
imc = peso / (altura**2)
if imc < 18.5:
    print(f'Você está com um IMC de {imc:.1f}! Você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print(f'Você está com um IMC de {imc:.1f}! Você está com o Peso Ideal.')
elif imc >= 25 and imc < 30:
    print(f'Você está com um IMC de {imc:.1f}! Você está em Sobre peso.')
elif imc >= 30 and imc < 40:
     print(f'Você está com um IMC de {imc:.1f}! Você está em Obesidade!')
else:
     print(f'Você está com um IMC de {imc:.1f}! Você está em Obesidade Móbida!')