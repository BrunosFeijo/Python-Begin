# Questão 33. Refaça o exercício anterior da tabuada usando as estruturas outras de repetição.

# Usando função recursiva
def tabuada(numero, contador=1):
    if contador <= 10:
        print(f'{numero} x {contador} = {numero * contador}')
        tabuada(numero, contador + 1)


valor = int(input('Digite um número: '))
tabuada(valor)
