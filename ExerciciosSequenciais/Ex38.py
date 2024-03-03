# Questão 38. Elabore um algoritmo que calcula e mostra a média das notas de todos os alunos de
# Algoritmos e Lógica de Programação.

# é para calcular a "média de todos os alunos" ou calcular a "média de cada aluno"? Optei pela média de todos
def inserirNotas():
    op = "s"
    i = 1
    lista = []
    while op == "s":
        nota = float(input(f"Digite a nota do {i}° aluno: "))
        lista.append(nota)
        i += 1
        op = input("Deseja continuar? [S/N] ").lower()
    return lista


notasAlunos = inserirNotas()

print(f'A média de todas as notas é {sum(notasAlunos) / len(notasAlunos):.2f}')
print(notasAlunos)
