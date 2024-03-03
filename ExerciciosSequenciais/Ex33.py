# Questão 33. Elabore um algoritmo que leia uma temperatura em graus centígrados e mostre-a
# convertida em graus Fahrenheit. A fórmula de conversão é: F = (9 * C + 160) / 5 onde F é a
# temperatura em Fahrenheit e C é a temperatura em centígrados.
celsius = float(input('Informe a temperatura em graus Celsius: '))
fahrenheit = (9 * celsius + 160) / 5

print(f'A temperatura em fahrenheit é {fahrenheit:.2f}')
