import re


def suma_diagonales():
    regex = re.compile(r'^\((\d+),\s*(\d+)\):\s*([-+]?\d+)$')
    matriz = {}
    with open('entrada_matriz.txt') as f:
        while True:
            entrada = f.readline()
            if entrada == '':
                break
            encaje = regex.search(entrada)
            if encaje is None:
                raise IOError(
                    "Hay datos incorrectos en el archivo de entrada.")
            i, j, n = map(int, encaje.groups())
            matriz[(i, j)] = n
    p = [matriz[(i, j)] for i, j in matriz if i == j]
    s = (matriz[(i, j)] for i, j in matriz if i + j == len(p) - 1)
    with open('salida_matriz.txt', 'w') as f:
        f.write(str(abs(sum(p) - sum(s))))
        f.write('\n')


suma_diagonales()
