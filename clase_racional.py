from math import gcd

class Racional:
    def __init__(self, num, den):
        self.__num = num
        self.__den = den

    def __eq__(self, otro):
        if not isinstance(otro, type(self)):
            return NotImplemented

        return self.numer() * otro.denom() == self.denom() * otro.numer()

    def __hash__(self):
        rac_simp = self.__simplificar()
        return hash((rac_simp.numer(), rac_simp.denom()))

    def __repr__(self):
        num = self.numer()
        den = self.denom()
        return f'Racional({num!r},{den!r})'

    def __str__(self):
        return f'{self.numer()}/{self.denom()}'

    def numer(self):
        return self.__num

    def denom(self):
        return self.__den

    def __simplificar(self):
        mcd = gcd(self.numer(), self.denom())
        num = self.numer() // mcd
        den = self.denom() // mcd
        return Racional(num, den)
