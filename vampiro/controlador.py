"""
El controlador.
"""

import jugador
import mapa
import interprete as i
import vocabulario as v

mapa.describir(jugador.localidad)

while True:
    print()
    entrada = input('>> ')

    if i.analizar(entrada):
        if i.verbo in (v.NORTE, v.SUR, v.ESTE, v.OESTE):
            if mapa.hay_salida(jugador.localidad, i.verbo):
                destino = mapa.destino(jugador.localidad, i.verbo)
                jugador.localidad = destino
                mapa.describir(jugador.localidad)
            else:
                print('No hay salida en esa dirección.')
        elif i.verbo == v.COGER:
            if i.nombre is None:
                print('¿Qué quieres que coja?')
            else:
                print('El jugador intenta coger algo...')
        elif i.verbo == v.MIRAR:
            mapa.describir(jugador.localidad)
        elif i.verbo == v.FIN:
            print('Gracias por jugar.')
            break
    else:
        print('No entiendo qué quieres decirme.')
