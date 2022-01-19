"""
El controlador.
"""

import jugador
import mapa
import interprete
import vocabulario as v

print(mapa.nombre(jugador.localidad))
print(mapa.descripcion(jugador.localidad))

while True:
    print()
    entrada = input('>> ')

    if interprete.analizar(entrada):
        if interprete.verbo == v.NORTE:
            print('Intentamos mover al jugador al norte.')
        elif interprete.verbo == v.SUR:
            print('Intentamos mover al jugador al sur.')
        elif interprete.verbo == v.COGER:
            if interprete.nombre is None:
                print('¿Qué quieres que coja?')
            else:
                print('El jugador intenta coger algo...')
        elif interprete.verbo == v.FIN:
            print('Gracias por jugar.')
            break
    else:
        print('No entiendo qué quieres decirme.')
