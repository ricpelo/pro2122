"""
try:
    f = open('suma.txt', 'r+')
    a = int(f.readline().rstrip())
    b = int(f.readline().rstrip())
    f.write('La suma de ' + str(a) + ' y ' + str(b) + ' es ' + str(a + b))
finally:
    f.close()
"""

with open('suma.txt', 'r+') as f:
    a = int(f.readline().rstrip())
    b = int(f.readline().rstrip())
    f.write('La suma de ' + str(a) + ' y ' + str(b) + ' es ' + str(a + b))
