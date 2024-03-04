# Questão 50. Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e
# mostre-a expressa apenas em dias.
def calcular_idade_em_dias(anos, meses, dias):
    dias_totais = anos * 365
    dias_totais += meses * 30
    dias_totais += dias
    return dias_totais

anos = int(input("Informe a idade em anos: "))
meses = int(input("Informe a idade em meses: "))
dias = int(input("Informe a idade em dias: "))

idade_em_dias = calcular_idade_em_dias(anos, meses, dias)
print("A idade expressa apenas em dias é:", idade_em_dias)
