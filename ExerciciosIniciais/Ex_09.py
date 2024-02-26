# 9. Entre com a base e a altura de um retângulo e mostre os resultados:
#   a. Perímetro (Perímetro é igual à soma dos 4 lados)
#   b. Área (Área é igual à lado vezes lado)

base = float(input('Digite o valor da base:'))
altura = float(input('Digite o valor da altura: '))
perimetro = (base + altura) * 2
area = base * altura

print(f'O retângulo de base {base} e altura {altura} tem o perimetro de {perimetro} e a area de {area}')