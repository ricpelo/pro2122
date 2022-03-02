class Coleccion:
    def __init__(self):
        self.__elementos = {}

    def insertar(self, elemento):
        numero = elemento.get_numero()
        if numero is None:
            numero = self.siguiente_numero_libre()
            elemento.set_numero(numero)
        self.__elementos[numero] = elemento
        return numero

    def buscar(self, numero):
        return self.__elementos.get(numero)

    def borrar(self, elemento):
        del self.__elementos[elemento.get_numero()]

    def siguiente_numero_libre(self):
        return 1 if len(self.__elementos) == 0 else \
               max(self.__elementos) + 1

    def __repr__(self):
        return repr(self.__elementos)
