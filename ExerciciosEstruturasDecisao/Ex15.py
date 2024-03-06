# Questão 15. Faça um programa que calcula a soma dos valores a partir de um intervalo
# informado pelo usuário.
start = int(input('Digite o início do intervalo: '))
stop = int(input('Digite o final do intervalo: '))
lista = range(start, stop + 1)
soma = 0
for num in lista:
    print(num, end=' ')
    soma += num

print()
print('-' * 40)
print(f'A soma é {soma}')