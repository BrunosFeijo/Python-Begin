# 10. Lê o raio de um círculo e mostre como saída o perímetro (2*π*Raio) e a área (π*Raio2).
import math

raio = float(input("Digite o raio do círculo: "))

perimetro = 2 * math.pi * raio
area = math.pi * raio ** 2

print("Perímetro do círculo:", f'{perimetro:.2f}')
print("Área do círculo:", f'{area:.2f}')