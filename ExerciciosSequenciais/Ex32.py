# Questão 32. Entre com uma data e mostre a data no formato: DD/MM/ANO
from datetime import datetime


def formatar_data(data):
    data_formatada_str = data.strftime('%d/%m/%Y')
    return data_formatada_str


ano = int(input('Digite o ano: '))
mes = int(input('Digite o mes: '))
dia = int(input('Digite o dia: '))
data_formatada = formatar_data(datetime(ano, mes, dia))

print(datetime(ano, mes, dia))
print("Data formatada:", data_formatada)
