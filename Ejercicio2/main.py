from claseMenu import Menu

if __name__ == '__main__':
    menu = Menu()

    ban = False
    while not ban:
        print('Menu Principal')
        print('--------------------')
        print('1- Registrar un ramo vendido.\n2- Mostrar 5 flores mas pedidas en un ramo.\n3- Mostrar flores vendidas por tipo de ramo.\n0- Salir.')
        op = input('Seleccione opcion:')
        menu.opcion(op)
        ban = op == '0'