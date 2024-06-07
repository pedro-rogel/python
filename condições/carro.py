pg1 = input('Está em bom estado? ')
pg2 = input('Documentação está em dia? ')
pg3 = input('Aceita pix? ')
if pg1 == 'Sim' and pg2 == 'Sim':
    print('Comprado')
elif pg2 == 'Sim' and pg3 == 'Sim':
    print('Comprado')
elif pg1 == 'Sim' and pg3 == 'Sim':
    print('Comprado')
else:
    print('Compra não realizada!')       
