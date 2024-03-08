# Questão 16. Faça um programa que mostra a soma dos valores de um intervalo informado pelo
# usuário (faça 2 programas, use FOR e WHILE).
start = int(input('Digite o início do intervalo: '))
stop = int(input('Digite o final do intervalo: '))
lista = range(start, stop + 1)
soma = 0

print('-' * 20 + 'for' + '-' * 20)
for num in lista:
    print(num, end=' ')
    soma += num

print()
print('-' * 43)
print(f'A soma é {soma}')

print('-' * 20 + 'while' + '-' * 20)

soma = 0
i = 0
while i < len(lista):
    print(lista[i], end=' ')
    soma += lista[i]
    i += 1

print()
print('-' * 45)
print(f'A soma é {soma}')
