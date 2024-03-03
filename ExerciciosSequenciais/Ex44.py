# Questão 44. A padaria HotBread vende uma certa quantidade de pães franceses e uma
# quantidade de broas a cada dia. Cada pãozinho custa R$ 0,12 e a broa custa R$ 1,50. Ao final do
# dia, o dono quer saber quanto arrecadou com a venda dos pães e broas (juntos), e quanto deve
# guardar numa conta de poupança (10% do total arrecadado). Você foi contratado para fazer os
# cálculos para o dono. Com base nestes fatos, faca um algoritmo para ler as quantidades de pães e
# de broas, e depois calcular os dados solicitados
valorPao = 0.12
valorBroa = 1.50
qtdPao = int(input('Quantos pães foram vendidos: '))
qtdBroa = int(input('Quantas broas foram vendidos: '))
ganhoPao = valorPao * qtdPao
ganhoBroa = valorBroa * qtdBroa
valorTotal = ganhoPao + ganhoBroa
poupanca = valorTotal * 0.1

print('O valor vendido foi R${:.2f}'.format(valorTotal))
print('O valor a ser depositado na poupança é R${:.2f}'.format(poupanca))
