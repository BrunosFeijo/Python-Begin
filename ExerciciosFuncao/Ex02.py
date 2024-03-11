# Questão 2. Escreva uma função que recebe as 3 notas de um aluno por parâmetro e uma letra.
# Se a letra for A o procedimento calcula a média aritmética das notas do aluno, se for P, a sua média
# ponderada (pesos: 5, 3 e 2) e se for H, a sua média harmônica. A média calculada também deve
# retornar por parâmetro.

def media(n1, n2, n3, tipo):
    if tipo == 'A':
        return f'Média Aritmética: {((n1 + n2 + n3) / 3):.2f}'
    elif tipo == 'P':
        return f'Média Ponderada: {((n1 * 5 + n2 * 3 + n3 * 2) / 10):.2f}'
    elif tipo == 'H':
        return f'Média Harmônica: {(3 / (1 / n1 + 1 / n2 + 1 / n3)):.2f}'


nota1 = float(input('Digite a 1° nota: '))
nota2 = float(input('Digite a 2° nota: '))
nota3 = float(input('Digite a 3° nota: '))
tipo = input('Digite o tipo de média [A/P/H]: ').strip().upper()

print(media(nota1, nota2, nota3, tipo))
