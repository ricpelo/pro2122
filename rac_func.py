def pareja(x, y):
    def primero():
        return x

    def segundo():
        return y

    def set_primero(nuevo_x):
        nonlocal x
        x = nuevo_x

    def set_segundo(nuevo_y):
        nonlocal y
        y = nuevo_y

    dic = {'primero': primero,
           'segundo': segundo,
           'set_primero': set_primero,
           'set_segundo': set_segundo}

    def despacho(mensaje):
        if mensaje in dic:
            return dic[mensaje]
        else:
            raise ValueError('Mensaje incorrecto')

    return despacho

def racional(n, d):
    p = pareja(n, d)

    def numer():
        return p('primero')()

    def denom():
        return p('segundo')()

    def set_numer(nuevo_num):
        p('set_primero')(nuevo_num)

    def set_denom(nuevo_den):
        p('set_segundo')(nuevo_den)

    dic = {'numer': numer,
           'denom': denom,
           'set_numer': set_numer,
           'set_denom': set_denom}

    def despacho(mensaje):
        if mensaje in dic:
            return dic[mensaje]
        else:
            raise ValueError('Mensaje incorrecto')

    return despacho

def mult(r1, r2):
    return racional(r1('numer')() * r2('numer')(),
                    r1('denom')() * r2('denom')())

def imprimir(r):
    print(r('numer')(), '/', r('denom')(), sep='')
