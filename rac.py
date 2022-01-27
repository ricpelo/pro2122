# Nivel de abstracción -1:

def pareja(x, y):
    return [x, y]

def select(p, n):
    return p[n]

# Nivel de abstracción 0:

def racional(n, d):
    return pareja(n, d)

def numer(r):
    return select(r, 0)

def denom(r):
    return select(r, 1)

# De aquí en adelante, no se enteran de los cambios en los
# detalles internos de implementación:

# Nivel de abstracción 1:

def suma(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return racional(nx * dy + ny * dx, dx * dy)

def mult(x, y):
    return racional(numer(x) * numer(y), denom(x) * denom(y))

def iguales(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)

def imprimir(x):
    print(numer(x), '/', denom(x), sep='')

# Nivel de abstracción 2:

def cuadrado(r):
    return mult(r, r)

def elevar(r, n):
    pass
