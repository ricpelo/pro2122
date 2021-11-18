# Determina si una cadena tiene una cierta cantidad
# de caracteres
# Pre: True
# Signatura: tiene_longitud(c: str, n: int) -> bool
# Post: tiene_longitud(c, n) =
#   - True si c tiene n caracteres
#   - False en caso contrario
tiene_longitud = lambda c, n: len(c) == n
