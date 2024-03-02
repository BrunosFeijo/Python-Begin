# Questão 19. Elabore um algoritmo que lê dois valores decimais e mostra a soma e o produto dos valores.
def multiplicar(n1,n2):
    return n1*n2

def soma(n1,n2):
    return n1+n2

def main():
    n1 = float(input('Digite o valor do primeiro número: '))
    n2 = float(input('Digite o valor do segundo número: '))
    print(f'O produto de {n1} e {n2} é {multiplicar(n1,n2)}')
    print(f'A soma de {n1} e {n2} é {soma(n1,n2)}')

main()
