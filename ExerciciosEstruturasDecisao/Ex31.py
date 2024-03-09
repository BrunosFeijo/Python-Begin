# Questão 31. Faça um programa que lê N valores; Ao final mostra a soma, a média, o maior valor
# e menor valor digitado considerando apenas os valores positivos
def media(*args):
    soma = 0
    for valor in args:
        soma += valor

    return soma / len(args)


op = ''
lista = []
while op != 'n':
    valor = float(input('Digite um valor: '))
    lista.append(valor)
    op = input('Deseja incluir outro valor? [S/N] ').strip().lower()

print('-' * 40)
print(f'Soma: {sum(lista)}')
print(f'Media: {media(*lista):.2f}')
print(f'Maior: {max(lista)}')
print(f'Menor: {min(lista)}')
print(lista)
