lista = []
while len(lista) < 10:
    entrada = input('Introduzca la cadena número ' +
                    str(len(lista)) + ': ')
    lista.append(entrada)

i = len(lista) - 1
while i >= 0:
    print(lista[i])
    i -= 1
