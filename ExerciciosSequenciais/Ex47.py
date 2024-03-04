# Questão 47. Em época de pouco investimento e poucas vendas, os comerciantes estão buscando
# aumentar a venda de seus produtos oferencendo descontos. Faça um algoritmo que possa receber
# o valor de um produto e que mostre: o valor do produto, o novo valor do produto considerando
# um desconto de 9% e qual foi o desconto dado. Por exemplo, o valor do produto é R$10,00, com o
# desconto de 9% o valor do produto fica R$ 9,10, e o desconto foi de R$0,90.
def calculaDesconto(valor, percentual):
    desconto = valor * percentual
    return desconto, valor - desconto


valor = float(input('Digite o valor: '))
desconto, valorDesconto = calculaDesconto(valor, 0.09)
print('Valor: R${:.2f}'.format(valor))
print('Desconto: R${:.2f}'.format(desconto))
print('Valor com Desconto: R${:.2f}'.format(valorDesconto))
