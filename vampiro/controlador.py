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
        if interprete.verbo == v.NORTE or \
           interprete.verbo == v.SUR or \
           interprete.verbo == v.ESTE or \
           interprete.verbo == v.OESTE:
            if mapa.hay_salida(jugador.localidad, interprete.verbo):
                destino = mapa.destino(jugador.localidad, interprete.verbo)
                jugador.localidad = destino
                print(mapa.nombre(jugador.localidad))
                print(mapa.descripcion(jugador.localidad))
            else:
                print('No hay salida en esa dirección.')
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
