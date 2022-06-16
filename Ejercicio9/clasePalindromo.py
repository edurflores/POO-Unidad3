class Palindromo:
    __palabra = None

    def __init__(self, palabra):
        self.__palabra = palabra.lower()

    def esPalindromo(self):
        i = 0
        j = len(self.__palabra) - 1 ### Correccion para que no salga de indice
        bandera = True
        while i < abs(j) and bandera:
            if self.__palabra[i].lower() != self.__palabra[j].lower(): ### Correccion: aplicado lower() para evitar problema por case sensitive
                bandera = False
            else:
                i += 1
                j -= 1 ### Empieza desde el final hacia delante
        return bandera

    def setPalabra(self, nuevaPalabra):
        self.__palabra = nuevaPalabra

    def getPalabra(self):
        return self.__palabra