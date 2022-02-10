class Deposito:
    """
    Descripción:
       Las instancias de esta clase representan depósitos
       bancarios en una entidad de crédito. Cada una tienen un
       saldo disponible que representa los fondos de ese depósito
       y se puede ingresar y retirar una cantidad de dinero.
       Un depósito nunca puede quedar al descubierto.

    Invariante:
        saldo >= 0
    """
    def __init__(self, fondos, historial=None):
        """
        Pre: fondos >= 0
        Post: self.saldo() == fondos
        """
        if fondos < 0:
            raise ValueError('Los fondos deben ser positivos.')
        self.__fondos = fondos
        if historial is None:
            self.__historial = []
        else:
            self.__historial = historial
        assert self.saldo() == fondos

    def __eq__(self, otro):
        """
        Post: self.__eq__(otro) <==> self == otro
        """
        if not isinstance(otro, type(self)):
            return NotImplemented
        return self.saldo() == otro.saldo() and \
               self.__historial == otro.historial

    def __repr__(self):
        return f'Deposito({self.saldo()!r}, {self.__historial!r})'

    def __str__(self):
        return f'Depósito con saldo {self.saldo()}.\nMovimientos:\n' + \
               '\n'.join(self.__historial)

    def saldo(self):
        return self.__fondos

    def ingresar(self, cantidad):
        """
        Pre: cantidad >= 0
        Post: saldo_nuevo == saldo_viejo + cantidad
        """
        self.__cantidad_positiva(cantidad)
        saldo_viejo = self.saldo()
        self.__fondos += cantidad
        self.__historial.append(f'Ingresa {cantidad}')
        assert self.saldo() == saldo_viejo + cantidad

    def retirar(self, cantidad):
        """
        Pre: cantidad >= 0 and cantidad <= self.saldo()
        Post: saldo_nuevo == saldo_viejo - cantidad
        """
        self.__cantidad_positiva(cantidad)
        if self.__fondos < cantidad:
            raise ValueError('No hay suficientes fondos')
        saldo_viejo = self.saldo()
        self.__fondos -= cantidad
        self.__historial.append(f'Retira {cantidad}')
        assert self.saldo() == saldo_viejo - cantidad

    def __cantidad_positiva(self, cantidad):
        if cantidad < 0:
            raise ValueError('La cantidad debe ser positiva.')
