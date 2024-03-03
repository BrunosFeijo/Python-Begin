# Questão 34. Elabore um algoritmo que lê dois números e mostre os seguintes resultados:
# Dividendo, Divisor, Quociente, Resto.

dividendo = float(input('Digite o valor do dividendo: '))
divisor = float(input('Digite o valor do divisor: '))
quociente = int(dividendo // divisor)
resto = int(dividendo % divisor)
print(f'Dividendo: {dividendo}')
print(f'Divisor: {divisor}')
print(f'Quociente: {quociente}')
print(f'Resto: {resto}')