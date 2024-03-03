# Questão 43. Calcule e mostre a área de um triângulo e mostre a área de um losango.
def calcular_area(base, altura):
    area = (base * altura) / 2
    return area


base_triangulo = float(input("Digite a base do triângulo: "))
altura_triangulo = float(input("Digite a altura do triângulo: "))

diagonal_maior_losango = float(input("Digite a diagonal maior do losango: "))
diagonal_menor_losango = float(input("Digite a diagonal menor do losango: "))

area_triangulo = calcular_area(base_triangulo, altura_triangulo)
area_losango = calcular_area(diagonal_maior_losango, diagonal_menor_losango)

print("Área do triângulo:", area_triangulo)
print("Área do losango:", area_losango)
