from claseMenu import Menu

if __name__ == '__main__':
    menu = Menu()
    ban = False
    while not ban:
        print('Menu Principal')
        print('1- Insertar agente.\n2- Agregar agente.\n3- Mostrar que agente se encuentra en una posicion dada.')
        print('4- Mostrar listado de docentes investigadores en una carrera.')
        print('5- Contar personal docente investigador e investigador en un area de investigacion.')
        print('6- Mostrar listado ordenado de agentes con sueldo.\n7- Mostrar informe de sueldos en una categoria de investigacion.')
        print('8- Guardar archivo JSON.\n9- Volver a cagar archivo JSON.\n0- Salir.')
        op = input('Seleccione opcion:')
        menu.opcion(op)
        ban = op == '0'