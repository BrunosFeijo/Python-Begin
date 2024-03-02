# Questão 18. Elabore um algoritmo que lê dois valores inteiros e mostra o produto dos valores.
def multiplicar(n1,n2):
    return n1*n2

def main():
    n1 = int(input('Digite o valor do primeiro número: '))
    n2 = int(input('Digite o valor do segundo número: '))
    print(f'O produto de {n1} e {n2} é {multiplicar(n1,n2)}')

main()