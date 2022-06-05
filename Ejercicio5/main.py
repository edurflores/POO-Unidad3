from Interfaces import IPrueba
from claseManejadorColeccion import ManejadorColeccion


if __name__ == '__main__':

    mc = ManejadorColeccion()
    mc.cargaElementos()
    pruebadeinterface = IPrueba(mc)
    pruebadeinterface.mostrarElemento(5)
    pruebadeinterface.mostrarElemento(7)
    print('Se agrega elemento "Javier Milei" en posicion 7.')
    print('-----------------------------')
    pruebadeinterface.insertarElemento('Javier Milei',7)
    print('Muestra:')
    pruebadeinterface.mostrarElemento(7)