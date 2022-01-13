"""
La dirección del coche.
"""

_angulo = 0

def girar_izquierda(grados=15):
    global _angulo
    _angulo -= grados

def girar_derecha(grados=15):
    global _angulo
    _angulo += grados

def angulo():
    return _angulo
