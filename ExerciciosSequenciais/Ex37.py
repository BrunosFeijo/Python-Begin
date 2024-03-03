# Questão 37. Elabore um algoritmo que lê o raio de um círculo e mostre como saída o perímetro e a área.
import math


def calcular_circulo(raio):
    perimetro = 2 * math.pi * raio
    area = math.pi * raio ** 2

    return perimetro, area


raio = float(input("Digite o raio do círculo: "))

perimetro, area = calcular_circulo(raio)

print(f"Perímetro do círculo: {perimetro:.2f}")
print(f"Área do círculo: {area:.2f}")
