def decoradora(func):
    def funcao_decoradora(*args, **kwargs):
        if args[1] == 0:
            return "Impossível dividir por zero"
        return func(*args, **kwargs)

    return funcao_decoradora


@decoradora
def divisao(x, y):
    return x / y


print(divisao(5, 5))
