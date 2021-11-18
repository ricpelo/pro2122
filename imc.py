# Calcula el IMC de una persona
# Pre: peso >= 0 and altura != 0
# Signatura: imc(peso: float, altura: float) -> float
# Post: imc(a, b) es el índice de masa corporal de una persona con
#       peso a (en Kg) y altura b (en m)
imc = lambda peso, altura: peso / (altura ** 2)
