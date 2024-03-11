# Questão 3. Faça uma função que recebe por parâmetro um valor inteiro e positivo e retorna o
# valor lógico Verdadeiro caso o valor seja primo e Falso em caso contrário

def primo(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i <= n / 2:
        if n % i == 0:
            return False
        i += 1
    return True


valor = int(input('Digite um numero inteiro positivo: '))
print(primo(valor))