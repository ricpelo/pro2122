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
FIN = 'fin'

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
    'FIN': {
        TOKEN: FIN,
        TIPO: TIPO_VERBO,
    }
}

def buscar(lexema):
    """
    Busca una palabra en el diccionario a partir de un lexema.

    Args:
        lexema (str): El lexema de la palabra a buscar.

    Returns:
        La palabra.

    Raises:
        KeyError: Si en el diccionario no hay ninguna palabra
                  con ese lexema.
    """
    return VOCABULARIO[lexema]

def tipo(palabra):
    """
    Devuelve el tipo de la palabra recibida como argumento.

    Precondición:
        La palabra recibida debe ser una palabra válida y
        correctamente formada. Eso significa que:

        - No puede ser None.
        - Debe contener un Tipo y un Token.

    Args:
        palabra: La palabra.

    Returns:
        El tipo de la palabra.
    """
    return palabra[TIPO]

def token(palabra):
    """
    Devuelve el token de la palabra recibida como argumento.

    Precondición:
        La palabra recibida debe ser una palabra válida y
        correctamente formada. Eso significa que:

        - No puede ser None.
        - Debe contener un Tipo y un Token.

    Args:
        palabra: La palabra.

    Returns:
        El token de la palabra.
    """
    return palabra[TOKEN]
