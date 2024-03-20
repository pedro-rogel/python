preco_mercadoria = float(input())
marcdoria_comprada = int(input())
desconto_fixo = 0.10
desconto_unidade = 0.01
valor_sem_desconto = preco_mercadoria * marcdoria_comprada 
desconto_total = desconto_fixo + (desconto_unidade * marcdoria_comprada)
preco_final = valor_sem_desconto * (1 - desconto_total)
print(f'{valor_sem_desconto:.2f}')
print(f'{preco_final:.2f}')