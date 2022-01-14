"""
El mapa del juego y todo lo relacionado con las localidades
del juego.
"""

# Propiedades de cada localidad:
NOMBRE = 'nombre'
DESCRIPCION = 'descripcion'
CONEXIONES = 'conexiones'

# Posibles conexiones de una localidad a la otra:
NORTE = 'norte'
SUR = 'sur'
ESTE = 'este'
OESTE = 'oeste'

# Localidades:
VESTIBULO = 'vestibulo'
PASILLO = 'pasillo'
COCINA = 'cocina'

MAPA = {
    VESTIBULO: {
        NOMBRE: 'Vestibulo',
        DESCRIPCION: 'Estás en el vestíbulo del castillo. El ambiente es muy húmedo y frío. Estás en un pasillo que se extiende hacia el norte. Al sur queda la puerta de entrada al castillo.',
        CONEXIONES: {
            NORTE: PASILLO
        }
    },
    PASILLO: {
        NOMBRE: 'Pasillo',
        DESCRIPCION: 'Te encuentras en medio del pasillo principal de este piso. Al oeste está la cocina y al este la biblioteca. El pasillo sigue hacia el norte.',
        CONEXIONES: {
            SUR: VESTIBULO,
            OESTE: COCINA
        }
    },
    COCINA: {
        NOMBRE: 'Cocina',
        DESCRIPCION: 'Estás en la cocina del castillo. Esto está lleno de cacerolas y de cacharros para cocinar. Hay un horno, un fregadero y un armario pequeño.',
        CONEXIONES: {
            ESTE: PASILLO
        }
    }
}
