# Questão 46. Uma fabrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma
# sendo vendida respectivamente por 10, 12 e 15 reais. Construa um algoritmo em que o usuário
# forneça a quantidade de camisetas pequenas, medias e grandes referentes a uma venda, e a
# maquina informe quanto será o valor arrecadado.

def calcularValor(pequena, media, grande):
    valorPequena = 10
    valorMedia = 12
    valorGrande = 15
    return (pequena * valorPequena), (media * valorMedia), (grande * valorGrande)


qtds = [
    int(input('Informe a qtd de camisetas pequenas: ')),
    int(input('Informe a qtd de camisetas médias: ')),
    int(input('Informe a qtd de camisetas grandes: '))
]
valores = calcularValor(*qtds)

print('-' * 40)
print(f'Pequenas: R$ {valores[0]}')
print(f'Media: R$ {valores[1]}')
print(f'Grande: R$ {valores[2]}')
print(f'Total: R$ {sum(valores)}')
