MAPA = [
    [False, True, True, False],
    [True, False, False, True],
    [False, True, False, False],
    [False, False, True, False]
]

def ejer104(mapa, ini, fin, camino):
    camino.append(ini)

    if mapa[ini][fin]:
        camino.append(fin)
        return True

    adyacentes = [nodo for nodo, valor in enumerate(mapa[ini]) \
                       if valor and nodo not in camino]

    for nodo in adyacentes:
        if ejer104(mapa, nodo, fin, camino):
            return True

    return False

camino = []
print(ejer104(MAPA, 3, 1, camino))
print(camino)
