# Questão 36. Faça um programa que mostra as 4 operações básicas (adição, subtração,
# multiplicação e divisão) a partir de valores digitados pelo usuário. PS: cuidado com as restrições,
# por exemplo, divisão de valores por zero.
def operacao(n1, n2, operador):
    if operador == '+':
        return n1 + n2
    elif operador == '-':
        return n1 - n2
    elif operador == '*':
        return n1 * n2
    elif operador == '/':
        try:
            return n1 / n2
        except ZeroDivisionError:
            return 'Nao pode dividir valores por 0'
    else:
        return 'Operador inválido'


num1 = float(input('Digite o primeiro valor: '))
operador = input('Digite a operação: [+,-,*,/,]: ').strip()
num2 = float(input('Digite o segundo valor: '))
print(operacao(num1, num2, operador))
