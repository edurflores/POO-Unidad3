import unittest
from clasePalindromo import Palindromo
from claseTestPalindromo import TestPalindromo

if __name__ == '__main__':
    ### unittest.main() ### Testeos, quitar comentario para usar


    palindromo = Palindromo('Eduardo') ### No deberia ser palindromo
    print('Palabra: Eduardo')
    if palindromo.esPalindromo(): ### True
        print('Esta palabra es palindromo.')
    else:
        print('Esta palabra NO es palindromo.')
    print('---------------------')
    print('Palabra: NeUqUeN')
    palindromo.setPalabra('NeUqUeN') ### Deberia ser palindromo
    if palindromo.esPalindromo(): ### True
        print('Esta palabra es palindromo.')
    else:
        print('Esta palabra NO es palindromo.')
    print('---------------------')
    print('Palabra: Japon')
    palindromo.setPalabra('Japon')  ### No Deberia ser palindromo
    if palindromo.esPalindromo():  ### True
        print('Esta palabra es palindromo.')
    else:
        print('Esta palabra NO es palindromo.')
    print('---------------------')
    print('Palabra: ana')
    palindromo.setPalabra('ana')  ### Deberia ser palindromo
    if palindromo.esPalindromo():  ### True
        print('Esta palabra es palindromo.')
    else:
        print('Esta palabra NO es palindromo.')
    print('---------------------')
    print('Palabra: kitsune')
    palindromo.setPalabra('kitsune')  ### No deberia ser palindromo
    if palindromo.esPalindromo():  ### True
        print('Esta palabra es palindromo.')
    else:
        print('Esta palabra NO es palindromo.')
    print('---------------------')
    print('Palabra: ANA')
    palindromo.setPalabra('ANA')  ### Deberia ser palindromo
    if palindromo.esPalindromo():  ### True
        print('Esta palabra es palindromo.')
    else:
        print('Esta palabra NO es palindromo.')
    print('---------------------')
    print('Palabra: anana')
    palindromo.setPalabra('anana') ### Deberia ser palindromo
    if palindromo.esPalindromo(): ### True
        print('Esta palabra es palindromo.')
    else:
        print('Esta palabra NO es palindromo.')
    print('---------------------')
    print('Palabra: MENEM')
    palindromo.setPalabra('MENEM') ### Deberia ser palindromo
    if palindromo.esPalindromo(): ### True
        print('Esta palabra es palindromo.')
    else:
        print('Esta palabra NO es palindromo.')
    print('---------------------')
    print('Palabra: amorroma')
    palindromo.setPalabra('amorroma')  ### Deberia ser palindromo
    if palindromo.esPalindromo():  ### True
        print('Esta palabra es palindromo.')
    else:
        print('Esta palabra NO es palindromo.')
    print('---------------------')


    print('Pruebe usted una palabra.')
    palabra = input('Ingrese una palabra:')
    palindromo = Palindromo(palabra)
    if palindromo.esPalindromo():  ### True
        print('Esta palabra es palindromo.')
    else:
        print('Esta palabra NO es palindromo.')