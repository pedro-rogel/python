frases = input('Digite uma frase:\n ').strip() .upper()
palavras = frases.split()
junto = ''.join(palavras)
# inverso = ''
inverso = junto[::-1]
# for letra in range(len(junto) - 1, -1, -1):
#     inverso += junto[letra]
print(f'O inverso de {junto} é {inverso} ')
if inverso == junto:
    print('A frase é um palindromo')
else:
    print('Não é um palindromo')


