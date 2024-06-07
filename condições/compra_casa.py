valor = float(input('Qual é o valor da casa?: '))
salario =  float(input('Qual é o seu salário?: '))
anos = float(input('Quantos anos será pago?: '))
prestacao = valor / (anos * 12)
porcentagem = salario * 0.30
if prestacao <= porcentagem:
    print(f'Pode comprar, meu bom! Você pagará {prestacao:.2f} por mês!')
else:
    print(f'Foi negado meu patrão!\nTá duro dorme!')