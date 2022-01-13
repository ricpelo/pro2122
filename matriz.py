M = [
    [3, 5, 9],
    [4, 2, 1],
    [8, 7, 6],
    [2, 9, 5]
]

# Recorre la lista por filas:
i = 0
while i < len(M):
    # Recorre la fila actual por columnas:
    j = 0
    while j < len(M[i]):
        print(M[i][j], end=' ')
        j += 1
    print()
    i += 1

for fila in M:
    for e in fila:
        print(e, end=' ')
    print()


def es_vocal(c):
    return c == 'a' or c == 'e' or c == 'i' or c == 'o' or \
           c == 'u' or c == 'A' or c == 'E' or c == 'I' or \
           c == 'O' or c == 'U'
