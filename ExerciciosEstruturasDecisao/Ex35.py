# Questão 35. Faça um algoritmo para ler dois valores (valide para que o segundo valor seja maior
# que o primeiro), mostrar os valores existentes entre os dois valores lidos

def verificador(n1, n2):
    if n1 < n2:
        return True
    return False


def printValoresIntermediarios(start, stop):
    for i in range(start, stop + 1):
        print(i, end=' ')


n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if verificador(n1, n2):
    printValoresIntermediarios(n1, n2)
else:
    print('O primeiro valor deve ser menor que o segundo!')
