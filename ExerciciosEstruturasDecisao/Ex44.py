# Questão 44. Faça um programa que lê 10 valores e verifica quantos estão no intervalo [10, 30] e
# quantos estão fora deste intervalo

def separaNumeros(lista):
    dentro = []
    fora = []
    for i in lista:
        if i in range(10, 30):
            dentro.append(i)
        else:
            fora.append(i)
    return dentro, fora


i = 0
valores = []
while i < 10:
    valor = int(input('Digite um valor inteiro: '))
    valores.append(valor)
    i += 1
dentro, fora = separaNumeros(valores)

print(f'{len(dentro)} elementos dentro do intervalo')
print(f'{len(fora)} elementos fora do intervalo')
