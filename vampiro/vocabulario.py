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
MIRAR = 'mirar'

# Nombres:
CUCHILLO = 'cuchillo'

# Vocabulario:
_VOCABULARIO = {
    COGER: (TIPO_VERBO, ['COGER', 'TOMAR']),
    NORTE: (TIPO_VERBO, ['NORTE', 'N']),
    SUR: (TIPO_VERBO, ['SUR', 'S']),
    ESTE: (TIPO_VERBO, ['ESTE', 'E']),
    OESTE: (TIPO_VERBO, ['OESTE', 'O']),
    FIN: (TIPO_VERBO, ['FIN', 'ACABAR', 'TERMINAR', 'FINALIZAR']),
    CUCHILLO: (TIPO_NOMBRE, ['CUCHILLO', 'NAVAJA']),
    MIRAR: (TIPO_VERBO, ['MIRAR', 'M', 'L'])
}

_vocabulario = {}

def crear_vocabulario():
    global _vocabulario

    for token, tupla in _VOCABULARIO.items():
        tipo, lexemas = tupla
        palabra = { TOKEN: token, TIPO: tipo }
        for lexema in lexemas:
            _vocabulario[lexema] = palabra

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
    return _vocabulario[lexema]

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

crear_vocabulario()
