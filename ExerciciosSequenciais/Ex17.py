# Questão 17. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
# velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download
# do arquivo usando este link (em minutos).

def calcular_tempo_download(tamanhoMB, velocidadeMbps):
    velocidadeMBps = velocidadeMbps / 8  # Converter Mbps para MBps
    return (tamanhoMB / velocidadeMBps) / 60


def converter_minutos_para_formato_mm_ss(tempo_minutos):
    minutos = int(tempo_minutos)
    segundos = int((tempo_minutos - minutos) * 60)
    return f"{minutos:02d}:{segundos:02d}"


def main():
    tamanhoMB = int(input("Digite o tamanho do arquivo (MB): "))
    velocidadeMbps = int(input("Digite a velocidade de download (Mbps): "))
    print(f'O tempo de download será de {converter_minutos_para_formato_mm_ss(calcular_tempo_download(tamanhoMB, velocidadeMbps))}')


main()
