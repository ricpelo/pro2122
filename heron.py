from math import sqrt

def superficie(a, b, c):
    sp = (a + b + c) / 2
    s = sqrt(sp * (sp - a) * (sp - b) * (sp - c))
    return s
