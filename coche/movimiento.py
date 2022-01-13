"""
El coche se mueve o se para.
"""

import motor

_velocidad = 0

def acelerar(fuerza=1):
    global _velocidad
    if motor.encendido():
        _velocidad += fuerza

def frenar(fuerza=1):
    global _velocidad
    _velocidad -= fuerza

def velocidad():
    return _velocidad
