"""
El vocabulario del juego.
"""

# Propiedades de las palabras:
TOKEN = 'token'
TIPO = 'tipo'

# Tipos de palabras:
TIPO_VERBO = 'tipo_verbo'
TIPO_NOMBRE = 'tipo_nombre'

# Verbos:
NORTE = 'norte'
SUR = 'sur'
ESTE = 'este'
OESTE = 'oeste'
COGER = 'coger'
DEJAR = 'dejar'

# Nombres:
CUCHILLO = 'cuchillo'

VOCABULARIO = {
    'COGER': {
        TOKEN: COGER,
        TIPO: TIPO_VERBO
    },
    'TOMAR': {
        TOKEN: COGER,
        TIPO: TIPO_VERBO
    },
    'CUCHILLO': {
        TOKEN: CUCHILLO,
        TIPO: TIPO_NOMBRE
    },
    'NORTE': {
        TOKEN: NORTE,
        TIPO: TIPO_VERBO
    },
    'N': {
        TOKEN: NORTE,
        TIPO: TIPO_VERBO
    },
    'SUR': {
        TOKEN: SUR,
        TIPO: TIPO_VERBO,
    },
    'S': {
        TOKEN: SUR,
        TIPO: TIPO_VERBO,
    },
}
