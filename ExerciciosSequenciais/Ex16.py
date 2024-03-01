# Questão 16. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em
# metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada
# 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em
# galões de 3,6 litros, que custam R$ 25,00.
# ! Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços
# em 3 situações:
# ! comprar apenas latas de 18 litros;
# ! comprar apenas galões de 3,6 litros;
# ! misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e
# sempre arredonde os valores para cima, isto é, considere latas cheias.

import math


def calcular_quantidade_tinta(area):
    return area / 6


def calcular_preco_latas(area):
    quantidade_latas = math.ceil(calcular_quantidade_tinta(area) / 18)
    preco_total = quantidade_latas * 80
    return quantidade_latas, preco_total


def calcular_preco_galoes(area):
    quantidade_galoes = math.ceil(calcular_quantidade_tinta(area) / 3.6)
    preco_total = quantidade_galoes * 25
    return quantidade_galoes, preco_total


def calcular_preco_misturado(area):
    quantidade_latas = math.floor(calcular_quantidade_tinta(area) / 18)
    quantidade_galoes = math.ceil((calcular_quantidade_tinta(area) % 18) / 3.6)
    preco_total = quantidade_latas * 80 + quantidade_galoes * 25
    return quantidade_latas, quantidade_galoes, preco_total


def main():
    area = float(input('Digite o tamanho da área a ser pintada (m²): '))

    quantidade_latas, preco_latas = calcular_preco_latas(area)
    quantidade_galoes, preco_galoes = calcular_preco_galoes(area)
    quantidade_latas_misturadas, quantidade_galoes_misturados, preco_misturado = \
        calcular_preco_misturado(area)

    print('\n' + '-' * 40)
    print("Situação 1: Comprar apenas latas de 18 litros")
    print("Quantidade de Latas: ", quantidade_latas)
    print("Preço Total: $", preco_latas)

    print('\n' + '-' * 40)
    print("Situação 2: Comprar apenas galões de 3,6 litros")
    print("Quantidade de galões: ", quantidade_galoes)
    print("Preço Total: R$", preco_galoes)

    print('\n' + '-' * 40)
    print("Situação 3: Misturar latas e galões")
    print("Quantidade de latas:", quantidade_latas_misturadas)
    print("Quantidade de galões:", quantidade_galoes_misturados)
    print("Preço Total: R$", preco_misturado)


main()
