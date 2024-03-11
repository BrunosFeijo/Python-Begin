# Questão 4. Faça uma função que recebe por parâmetro os valores necessário para o cálculo da
# fórmula de báskara e retorna, também por parâmetro, as suas raízes, caso seja possível calcular
import math


def baskara(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return 'delta negativo', 'delta negativo'

    resultado1 = (-b + math.sqrt(delta)) / (2 * a)
    resultado2 = (-b - math.sqrt(delta)) / (2 * a)
    return resultado1, resultado2


re1, re2 = baskara(1, 6, 3)
print(f'Resultados: {re1} e {re2}')
