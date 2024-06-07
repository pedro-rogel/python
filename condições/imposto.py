renda = round(float(input()), 2)
if renda <= 2000:
    imposto_renda = 'Isento'
else:
    if renda <= 3000:
        imposto_renda = renda * 0.8
    else:
        if renda <= 4500:
            imposto_renda = renda * 0.18
        else:
                imposto_renda = renda * 0.28
print(f'R$ {imposto_renda:.2f}')