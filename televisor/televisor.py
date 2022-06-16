class Televisor:
    def __init__(self):
        self.__encendido = False
        self.__canal = 1
        self.__volumen = 0
        self.__soporte = None

    def encender(self):
        self.__encendido = True
        return self

    def apagar(self):
        self.__encendido = False
        return self

    def subir_volumen(self):
        if self.__encendido and self.volumen() < 30:
            self.__volumen += 1
        return self

    def bajar_volumen(self):
        if self.__encendido and self.volumen() > 0:
            self.__volumen -= 1
        # if self.__encendido:
        #     self.__volumen = max(0, self.__volumen - 1)
        return self

    def volumen(self):
        return self.__volumen

    def sintonizar(self, canal):
        if canal not in range(1, 101):
            raise ValueError('El canal no es correcto')

        if self.__encendido:
            self.__canal = canal

        return self

    def conectar(self, soporte):
        self.__soporte = soporte
        return self

    def desconectar_si_conectado(self):
        self.__soporte = None
        return self

    def reproducir_si_conectado(self):
        if self.__encendido and self.__soporte is not None:
            return set(self.__soporte.playlist())

        return set()

class Soporte:
    def __init__(self, contenido):
        self.__contenido = tuple(contenido)

    def playlist(self):
        return self.__contenido

    def reproducir(self, indice):
        return self.__contenido[indice]
