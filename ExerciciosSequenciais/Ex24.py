# Questão 24. Calcula a média das notas de Algoritmos e Lógica de Programação. Assuma que
# serão fornecidas 4 diferentes notas (2 trabalhos e 2 provas). Observe que as provas equivalem a 60%
# da nota final, enquanto que os trabalhos equivalem a 40% da nota final. Nota final = (Prova 1 +
# Prova 2) * 0,60 + (Trabalho 1 + Trabalho 2) * 0,40

def media(notasTrabalho, notasProva):
    return ((sum(notasTrabalho) * 0.4) + (sum(notasProva) * 0.6)) / 2


trabalhos = [float(input('Digite a nota do 1° trabalho: ')),
             float(input('Digite a nota do 2° trabalho: '))]
provas = [float(input('Digite a nota da 1° prova: ')),
          float(input('Digite a nota da 2° prova: '))]

media = media(trabalhos, provas)
print('A media é de {:.2f}'.format(media))
