
class Deposito:
    def __init__(self, fondos, historial=None):
        self.__fondos = fondos
        if historial is None:
            self.__historial = []
        else:
            self.__historial = historial

    def __eq__(self, otro):
        if type(self) != type(otro):
            return NotImplemented
        return self.saldo() == otro.saldo() and self.__historial == otro.historial

    def __repr__(self):
        return f'Deposito({self.saldo()!r}, {self.__historial!r})'

    def __str__(self):
        return f'Depósito con saldo {self.saldo()}.\nMovimientos:\n' + \
               '\n'.join(self.__historial)

    def saldo(self):
        return self.__fondos

    def ingresar(self, cantidad):
        self.__fondos += cantidad
        self.__historial.append(f'Ingresa {cantidad}')

    def retirar(self, cantidad):
        if self.__fondos < cantidad:
            raise ValueError('No hay suficientes fondos')
        self.__fondos -= cantidad
        self.__historial.append(f'Retira {cantidad}')
