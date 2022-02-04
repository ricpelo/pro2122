from math import gcd

class Racional:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __eq__(self, otro):
        if type(self) != type(otro):
            return NotImplemented

        return self.numer() * otro.denom() == self.denom() * otro.numer()

    def __hash__(self):
        rac_simp = self.simplificar()
        return hash((rac_simp.numer(), rac_simp.denom()))

    def __repr__(self):
        num = self.numer()
        den = self.denom()
        return f'Racional({num},{den})'

    def numer(self):
        return self.num

    def denom(self):
        return self.den

    def imprimir(self):
        print(self.numer(), '/', self.denom(), sep='')

    def simplificar(self):
        mcd = gcd(self.numer(), self.denom())
        num = self.numer() // mcd
        den = self.denom() // mcd
        return Racional(num, den)
