"""
El sistema eléctrico
"""

import motor

_activo = False

def activar():
    global _activo
    _activo = True
    print('Sistema eléctrico activado.')

def desactivar():
    global _activo
    if motor.encendido():
        print('No se puede quitar la llave porque el motor está encendido.')
    else:
        _activo = False
        print('Sistema eléctrico desactivado.')

def activo():
    return _activo
