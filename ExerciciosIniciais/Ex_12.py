# 12. Calcule o valor de uma prestação em atraso, utilizando a fórmula:
#   PRESTAÇÃO = VALOR + (VALOR * (TAXA/100) * TEMPO).

valor = float(input('Digite o valor em atraso:'))
tempo = int(input('Digite o tempo de atraso em dias: '))
taxa = float(input('Digite a taxa de juros diária:'))
prestacao = valor + (valor * (taxa/100) * tempo)

print(f'Um valor de ${valor} com taxa de juros de {taxa}% em {tempo} dias de atraso custará ${prestacao:.2f}')