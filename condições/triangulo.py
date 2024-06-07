mostra_ae = print
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r2 and r3 < r1 + r2:
    mostra_ae(f'Os segmentos acima PODEM FORMAR triângulos!')
    if r1 == r2 == r3:
        mostra_ae(f'Triangulo EQUILÁTERO')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
        mostra_ae(f'Triangulo ISÓSCELES')
    elif r1 != r2 != r3:
        mostra_ae(f'Triangulo ESCALENO')
else:
    mostra_ae('Os segmentos acima NÃO PODEM FORMAR triângulos')