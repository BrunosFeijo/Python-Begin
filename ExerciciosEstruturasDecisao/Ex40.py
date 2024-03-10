# Questão 40. Faça um programa que o usuário digita N valores, o programa deve calcular a média
# dos valores e mostrar o resultado indicando se a média é maior que 30

op = ' '
valores = []
while op != 'n':
    valor = float(input('Digite um número: '))
    valores.append(valor)
    op = input('Deseja continuar[S,N]: ').lower()

media = sum(valores) / len(valores)
print(f'Média: {media:.2f}')
if media > 30:
    print('A média é maior que 30')
else:
    print('A média não é maior que 30')
