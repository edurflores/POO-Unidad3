from claseMenu import Menu

if __name__ == '__main__':
    menu = Menu()
    ban = False

    while not ban:
        print('Menu Principal.')
        print('-----------------------')
        print('1- Registrar jugador y crear contrato.\n2- Consultar jugador contratado.\n3- Consultar contratos.\n4- Obtener importe de contratos.')
        print('5- Guardar contratos en archivo.\n0- Salir.')
        op = input('Seleccione opcion:')
        menu.opcion(op)
        ban = op == '0'