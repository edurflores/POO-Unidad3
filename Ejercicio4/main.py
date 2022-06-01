from claseMenu import Menu

menu = Menu()
ban = False

while not ban:
    print('Menu Principal')
    print('-----------------------')
    print('1- Buscar calefactor a gas de menor consumo.\n2- Buscar calefactor electrico de menor consumo.\n3- Mostrar datos de calefactor de menor consumo.')
    print('0- Salir.')
    op = input('Seleccione opcion:')
    menu.opcion(op)
    ban = op == '0'