# Questão 14. Faça um programa que mostra os valores a partir de um intervalo informado pelo
# usuário.
start = int(input('Digite o início do intervalo: '))
stop = int(input('Digite o final do intervalo: '))
lista = range(start, stop + 1)
for num in lista:
    print(num, end=' ')