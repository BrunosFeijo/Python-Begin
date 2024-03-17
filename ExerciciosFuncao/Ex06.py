# Questão 6. Faça uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna
# essa idade expressa em dias.

# assumindo anos de 365 dias e meses de 30 dias
def calcularDias(anos, meses, dias):
    return anos * 365 + meses * 30 + dias


print('Digite sua idade em anos, meses e dias: ')
ano = int(input('Digite o ano: '))
mes = int(input('Digite o mês: '))
dia = int(input('Digite o dia: '))

print("Sua idade em dias é: ", calcularDias(ano, mes, dia))
