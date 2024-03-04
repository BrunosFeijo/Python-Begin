# Questão 48. A fabrica de refrigerantes Meia-Cola vende seu produto em três formatos: lata de
# 350 ml, garrafa de 600 ml e garrafa de 2 litros. Se um comerciante compra uma determinada
# quantidade de cada formato, faca um algoritmo para calcular quantos litros de refrigerante ele
# comprou

def calculaLitro(volumeMl):
    return volumeMl / 1000


def calculaVolume(lata, garrafinha, garrafa):
    return (lata * 350) + (garrafinha * 600) + (garrafa * 2000)


lata = float(input('Quantas latas vocês deseja comprar: '))
garrafinha = float(input('Quantas garrafinhas (600ml) você deseja comprar: '))
garrafa = float(input('Quantas garrafas (2l) você deseja comprar: '))
volumeMl = calculaVolume(lata, garrafinha, garrafa)

if volumeMl >= 1000:
    print(f'Você comprou {calculaLitro(volumeMl):.3f}l')
else:
    print(f'Você comprou {volumeMl}ml')
