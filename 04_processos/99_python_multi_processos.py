# _*_ coding: utf8 _*_

# Imports
from datetime import datetime
from math import sqrt
from multiprocessing import cpu_count as mp_cpu_count
from multiprocessing import Process as mp_Process


# Função main
def main():
    # Variável de início de execução
    inicio = datetime.now()

    # Captura a quantidade de cores de CPU
    ncpu = mp_cpu_count()

    print(f'Processamento matemático com {ncpu} cores.')

    p = []

    # xxxxx
    for i in range(1, ncpu + 1):
        ini = (50_000_000 * (i - 1)) / ncpu
        fim = (50_000_000 * i) / ncpu
        print(f'Core [{i - 1}]: {ini} -> {fim}')
        p.append(
            mp_Process(
                target=computar,
                kwargs={'inicio': ini, 'fim': fim},
                daemon=True
            )
        )

    [i.start() for i in p]
    [i.join() for i in p]

    # Tempo decorrido da execução
    tempo = datetime.now() - inicio

    # Exibe mensagem informando quanto tempo demorou em segundos.
    print(f'Terminou em {tempo.total_seconds():.2f}s.')


# Função computar
def computar(fim: int, inicio: int=1) -> None:

    # Variável fator
    fator = 1000 * 1000

    # Enquanto inicio for menor que fim:
    while inicio < fim:
        inicio += 1  # Incrementa 1
        sqrt((inicio - fator) * (inicio - fator))  # Raiz quadrada


# Execução como script
if __name__ == '__main__':
    main()

# 10.54s
# 9.85s
# 1.08s
