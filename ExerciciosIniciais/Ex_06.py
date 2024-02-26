# 6. Lê dois números e mostre os seguintes resultados:
    # a. Dividendo:
    # b. Divisor:
    # c. Quociente:
    # d. Resto (para calcular o resto de uma divisão, utilize o operador MOD (em C: %)

dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))
quociente = dividendo / divisor
quociente_inteiro = dividendo // divisor
resto = dividendo % divisor

print("Dividendo:", dividendo)
print("Divisor:", divisor)
print("Quociente:", f'{quociente:.2f}')
print("Quociente_Inteiro:", quociente_inteiro)
print("Resto:", resto)