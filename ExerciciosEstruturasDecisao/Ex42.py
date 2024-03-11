# Questão 42. Faça um programa que calcula a média do valores compreendidos entre 1 e o valor
# que o usuário informará no início do programa. Use WHILE para resolver a questão

stop = int(input('Digite o um valor inteiro: '))
i = 1
lista = []
while i <= stop:
    lista.append(i)
    i += 1

print(lista)
print(f'Média: {(sum(lista) / len(lista)):.2f}')

