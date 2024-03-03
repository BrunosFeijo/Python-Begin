# Questão 31. Elabore um algoritmo que lê 6 números decimais e mostra a soma e a subtração dos valores digitados.
def subtrair(*args):
    sub = args[0]
    for i in args[1:]:
        sub = sub - i
    return sub


numeros = [
    float(input('Digite o 1° número: ')),
    float(input('Digite o 2° número: ')),
    float(input('Digite o 3° número: ')),
    float(input('Digite o 4° número: ')),
    float(input('Digite o 5° número: ')),
    float(input('Digite o 6° número: '))
]

print(f'Soma: {sum(numeros)}')
print(f'Subtração: {subtrair(*numeros)}')