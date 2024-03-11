# Questão 1. Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o seu
# volume (v = (4 * Pi * R3) / 3).
import math


def volume(raio):
    return (4 * math.pi * raio) / 3


raio = float(input('Digite o raio da esfera: '))
v = volume(raio)

print(f'A volume é: {v:.2f}')
