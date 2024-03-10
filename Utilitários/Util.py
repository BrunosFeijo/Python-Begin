def media(*args):
    soma = 0
    for valor in args:
        soma += valor

    return soma / len(args)
