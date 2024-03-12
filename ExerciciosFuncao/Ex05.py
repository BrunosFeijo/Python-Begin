# Questão 5. Faça uma função que recebe por parâmetro o tempo de duração de uma fábrica
# expressa em segundos e retorna também por parâmetro esse tempo em horas, minutos e segundos

def horaMinutoSegundo(tempo):
    horas = tempo // 3600
    minutos = tempo % 3600 // 60
    segundos = tempo % 60
    return horas, minutos, segundos


tempo = int(input('Informe o tempo em segundos: '))
horas, minutos, segundos = horaMinutoSegundo(tempo)

print(f'{horas:02d}:{minutos:02d}:{segundos:02d}')
