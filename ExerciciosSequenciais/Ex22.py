# Questão 22. Um colega pediu dinheiro emprestado, você aceitou emprestar com a condição de
# que ele irá devolver o valor emprestado com juros de 15%. Qual o valor que o colega pediu e
# quanto ele irá devolver depois?
valor = float(input('Digite um valor: '))
juros = 0.15
valorComJuros = valor + (juros * valor)
print('O valor solicitado foi R${:.2f}'.format(valor))
print('O valor com juros será de R${:.2f}'.format(valorComJuros))
