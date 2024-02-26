# 11. Calcule e mostre a área de um triângulo (área é igual a (base x altura) dividido por 2)

base = float(input('Digite a base do tringulo: '))
altura = float(input('Digite a altura do tringulo: '))
area = (base * altura) / 2

print(f'Um tringulo de base {base} e altura {altura} tem área {area:.2f}')