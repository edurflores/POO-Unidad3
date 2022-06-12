from claseMenu import Menu

if __name__ == '__main__':
    menu = Menu()
    ban = False
    while not ban:
        print('Menu Principal')
        print('----------------------------------')
        print('1- Insertar un aparato en la coleccion en una posicion determinada. \n2- Agregar un aparato a la coleccion.')
        print('3- Mostrar que objeto se encuentra en una determinada posicion.')
        print('4- Mostrar cantidad de aparatos de marca Phillips.')
        print('5- Mostrar marca de lavarropas con carga superior.\n6- Mostrar aparatos en venta.')
        print('7- Almacenar en archivo JSON.\n8- Volver a cargar archivo JSON.\n0- Salir.')
        op = input('Seleccione opcion: ')
        menu.opcion(op)
        ban = op == '0'