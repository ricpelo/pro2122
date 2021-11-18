"""
Escribir un programa que imprima cuántos alumnos han aprobado
y cuántos han suspendido.
"""

NOTAS = [
    ('Manolo', 7.5),
    ('María', 9.9),
    ('Pepe', 4.3),
    ('Juan', 2.1),
    ('Luisa', 6.3)
]

aprobados = 0
suspendidos = 0
i = 0
while i < len(NOTAS):
    if NOTAS[i][1] >= 4.5:
        aprobados += 1
    else:
        suspendidos += 1
    i += 1
print('Hay', aprobados, 'aprobados y', suspendidos, 'suspendidos.')
