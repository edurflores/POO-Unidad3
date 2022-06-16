import unittest
from clasePalindromo import Palindromo

class TestPalindromo(unittest.TestCase):
    def setUp(self):
        self.__palindromo = Palindromo('menem')

    def test_secuencia(self): ### Test si coinciden los caracteres en orden y numero
        self.assertSequenceEqual(self.__palindromo.getPalabra(),'menem')

    def test_CantidadLetras(self): ### Test que comprueba la cantidad de letras
        self.assertEqual(len(self.__palindromo.getPalabra()),5)

    ### Tests que fallan porque es case sensitive, es decir Menem != menem. Medida: Se aplicara lower() en el ingreso de palabra en el programa principal

    def test_PrimeraSegundaLetra(self):
        self.assertEqual(self.__palindromo.getPalabra()[0],self.__palindromo.getPalabra()[4])

    def test_PosicionUltimaLetra(self):
        self.assertEqual(self.__palindromo.getPalabra()[4],'m') ### Test para comprobar si la ultima letra es m, para asegurar que se recorra desde atras hacia adelante

    ### Medida: Corregir para que variable j contenga cantidad de caracteres - 1 de la palabra. Ademas debe ser positivo.
    ### Corregido a j = len(self.__palabra) - 1. Asi, para el caso de 'Menem', j = 4

    def test_Palindromo(self):
        self.assertEqual(self.__palindromo.esPalindromo(),True)

    ### Medida: Corregir linea 16 (j += 1), ya que produce excepcion IndexError.
    ### Corregida a j -= 1, para que continue el recorrido de atras hacia delante