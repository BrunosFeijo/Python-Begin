# Questão 18. Faça um programa que mostra a soma dos valores pares, onde o intervalo considera
# o valor 1 até um valor que será informado pelo usuário.

# usando list comprehension

stop = int(input('Digite um número inteiro: '))
lista = [
    numero
    for numero in range(1, stop)
    if numero % 2 == 0
]
print(lista)
