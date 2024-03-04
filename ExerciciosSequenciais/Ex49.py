# Questão 49. Lê um valor de hora e informa quantos minutos se passaram desde início do dia.
def calculaMinuto(tempo):
    if ':' in tempo:
        tempo = tempo.split(':')
        hora = int(tempo[0])
        minuto = int(tempo[1])
    else:
        hora = int(tempo)
        minuto = 0
    return (hora * 60) + minuto


tempo = input('Informe a hora: ')
tempo = calculaMinuto(tempo)
print(f'Desde o início do dia se passaram {tempo} minutos')
