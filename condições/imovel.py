vp = float(input('Digite a sua poupança: '))
vi = float(input('Digite o valor do imolvel: '))
financia = vi * 0.30
if vi <= vp:
    print('Comprado a vista!')
elif vi > vp and vp >= financia:
    print('Compra financiada')
else: 
    print('Poupe mais') 
 