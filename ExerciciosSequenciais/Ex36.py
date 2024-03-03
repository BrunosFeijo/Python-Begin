# Questão 36. Entre com a base e a altura de um retângulo e mostre os resultados: Perímetro, Área, Diagonal
import math


def calcular_retangulo(base, altura):
    perimetro = 2 * (base + altura)
    area = base * altura
    diagonal = math.sqrt(base ** 2 + altura ** 2)

    return perimetro, area, diagonal


base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

perimetro, area, diagonal = calcular_retangulo(base, altura)

print(f"Perímetro do retângulo: {perimetro}")
print(f"Área do retângulo: {area}")
print(f"Diagonal do retângulo: {diagonal}")
