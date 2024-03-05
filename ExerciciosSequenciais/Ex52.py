# Questão 52. Faça um algoritmo que leia a idade de uma pessoa expressa em dias e mostre-a
# expressa em anos, meses e dias
def calculaTempo(dias):
    anos = dias // 365
    meses = (dias % 365) // 30
    dias = (dias % 365) % 30
    return anos, meses, dias


dias = int(input('Digite sua idade em dias: '))
anos, meses, dias = calculaTempo(dias)
print(f'Você tem {anos} ano(s), {meses} mês(es) e {dias} dia(s)')