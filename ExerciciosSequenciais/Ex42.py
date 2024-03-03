# Questão 42. Elabora um algoritmo onde o usuário informa o tamanho de um quadrado e o
# resultado é mostrar a área e o perímetro do quadrado (Perímetro; 4 * L; área = L**2 ).
lado = float(input('Digite o lado do quadrado: '))
area = lado * lado
perimetro = lado * 4
print(f'Lado: {lado:.2f}')
print(f'Area: {area:.2f}')
print(f'Perimetro: {perimetro:.2f}')
