"""
El mapa del juego y todo lo relacionado con las localidades
del juego.
"""

from vocabulario import NORTE, SUR, ESTE, OESTE

# Propiedades de cada localidad:
_NOMBRE = 'nombre'
_DESCRIPCION = 'descripcion'
_CONEXIONES = 'conexiones'


# Identificadores de las localidades:
VESTIBULO = 'vestibulo'
PASILLO = 'pasillo'
COCINA = 'cocina'

# El mapeado del juego:
_MAPA = {
    VESTIBULO: {
        _NOMBRE: 'Vestibulo',
        _DESCRIPCION: 'Estás en el vestíbulo del castillo. El ambiente es muy húmedo y frío. Estás en un pasillo que se extiende hacia el norte. Al sur queda la puerta de entrada al castillo.',
        _CONEXIONES: {
            NORTE: PASILLO
        }
    },
    PASILLO: {
        _NOMBRE: 'Pasillo',
        _DESCRIPCION: 'Te encuentras en medio del pasillo principal de este piso. Al oeste está la cocina y al este la biblioteca. El pasillo sigue hacia el norte.',
        _CONEXIONES: {
            SUR: VESTIBULO,
            OESTE: COCINA
        }
    },
    COCINA: {
        _NOMBRE: 'Cocina',
        _DESCRIPCION: 'Estás en la cocina del castillo. Esto está lleno de cacerolas y de cacharros para cocinar. Hay un horno, un fregadero y un armario pequeño.',
        _CONEXIONES: {
            ESTE: PASILLO
        }
    }
}

def nombre(loc):
    return _MAPA[loc][_NOMBRE]

def descripcion(loc):
    return _MAPA[loc][_DESCRIPCION]

def hay_salida(localidad, direccion):
    return direccion in _MAPA[localidad][_CONEXIONES]

def destino(localidad, direccion):
    return _MAPA[localidad][_CONEXIONES].get(direccion)

def describir(localidad):
    print(nombre(localidad))
    print(descripcion(localidad))
