class Movimiento:
    @staticmethod
    def es_valido(direccion, limite):
        return direccion in ['N', 'S', 'E', 'O',
                             'NE', 'SE', 'NO', 'SO', 'L'] and \
               (limite is None or limite >= 1)

    def __init__(self, direccion, limite):
        if not Movimiento.es_valido(direccion, limite):
            raise ValueError('El movimiento no es válido')
        self.__direccion = direccion
        self.__limite = limite
