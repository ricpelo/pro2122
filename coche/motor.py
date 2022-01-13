"""
El motor del coche.
"""

import electrico

CILINDRADA = 1500

_encendido = 0

def arrancar():
    global _encendido
    if electrico.activo():
        _encendido = 1
        print('¡Brrrrrrrrrrrmmmmm!')
    else:
        print('No se puede arrancar si no tiene la llave.')

def parar():
    global _encendido
    _encendido = 0
    print('Parando el motor...')

def encendido():
    return _encendido == 1
