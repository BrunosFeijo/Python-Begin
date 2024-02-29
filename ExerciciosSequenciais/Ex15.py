# Questão 15. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
# metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada
# 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao
# usuário a quantidades de latas de tinta a serem compradas e o preço total.
import math

area = float(input('Digite o tamanho da área a ser pintada (m²): '))
VOLUME_LATA = 18
PRECO_LATA = 80.00
AREA_PINTADA_LATA = 3 * VOLUME_LATA
quantidade_lata = math.ceil(area / AREA_PINTADA_LATA)
preco_total = quantidade_lata * PRECO_LATA

print(f'Quantidade de Latas: {quantidade_lata}')
print(f'Valor Total: ${preco_total:.2f}')