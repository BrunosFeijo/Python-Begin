# Questão 35. Elabore um algoritmo que converta um valor em dólar (U$) para real (R$). O
# algoritmo deverá solicitar o valor da cotação do dólar e também a quantidade de dólares a ser
# convertida
cotacao = float(input('Digita a cotação do dólar: '))
dolar = float(input('Digite o valor em dólar: U$'))
real = cotacao * dolar
print(f'O valor em real é R${real:.2f}')
