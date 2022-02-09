class Pila:
    """
    Invariante:
    len(pila) == pila.get_num_apilar() - pila.get_num_desapilar()
    """
    def __init__(self, elementos=None):
        if elementos is None:
            self.__elementos = []
        else:
            self.__elementos = list(elementos)
        self.__num_apilar = 0
        self.__num_desapilar = 0

    def __eq__(self, otro):
        if not isinstance(otro, type(self)):
            return NotImplemented
        return self.__elementos == otro.__elementos

    def __repr__(self):
        return f'Pila({self.__elementos!r})'

    def __iter__(self):
        return iter(self.__elementos)

    def __len__(self):
        return len(self.__elementos)

    def apilar(self, elem):
        self.__elementos.append(elem)
        self.__num_apilar += 1

    def es_vacia(self):
        return len(self.__elementos) == 0

    def cima(self):
        self.__comprobar_no_vacia()
        return self.__elementos[-1]

    def desapilar(self):
        self.__comprobar_no_vacia()
        self.__num_desapilar += 1
        return self.__elementos.pop()

    def get_num_apilar(self):
        return self.__num_apilar

    def get_num_desapilar(self):
        return self.__num_desapilar

    def __comprobar_no_vacia(self):
        if self.es_vacia():
            raise ValueError('La pila está vacía.')
