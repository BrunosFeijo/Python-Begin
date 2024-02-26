# 7. Leia 4 números e mostre a média ponderada, sabendo-se que os pesos são respectivamente: 1, 2, 3 e 4.

n1 = float(input('Digite o 1° número:'))
n2 = float(input('Digite o 2° número:'))
n3 = float(input('Digite o 3° número:'))
n4 = float(input('Digite o 4° número:'))

average = ((n1 * 1) +
           (n2 * 2) +
           (n3 * 3) +
           (n4 * 4)) / 10

print('A média ponderada foi {:.2f}'.format(average))