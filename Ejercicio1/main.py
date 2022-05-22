from claseMenu import Menu


if __name__ == '__main__':
    menu = Menu()
    ban = False
    while not ban:
        print('Menu principal')
        print('--------------------')
        print('1- Mostrar datos de facultad y duracion de sus carreras.\n2- Buscar carrera.\n0- Salir.')
        op = input('Ingrese opcion:')
        menu.opcion(op)
        ban = op == '0'