# 8. Lê o saldo de uma aplicação e imprima o novo saldo, considerado o reajuste de 1%.

saldo = float(input('Digite um número: '))
novo_saldo = saldo + (saldo * 0.01)

print('O novo saldo é de R${:.2f}'.format(novo_saldo))
