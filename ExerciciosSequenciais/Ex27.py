# Questão 27. Mostrar a média aritmética entre 3 números informados pelo usuário.
def media(*args):
    tamanho = len(args)
    soma = 0
    for valor in args:
        soma += valor
    return soma / tamanho


numeros = [
    float(input('Digite o 1° número: ')),
    float(input('Digite o 2° número: ')),
    float(input('Digite o 3° número: '))
]
print(f'A média é: {media(*numeros):.2f}')
