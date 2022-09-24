#_*_ coding: utf8 _*_

# Imports
from datetime import datetime
from math import sqrt
from multiprocessing import cpu_count as multiprocessing_cpu_count
from threading import 

# Função main
def main():
    # 
    qtd_cores = multiprocessing_cpu_count()

    # Variável de início de execução
	inicio = datetime.now()

    # Chama a função computar (que é definida logo depois)
	computar(fim=50_000_000)

    # Tempo decorrido da execução
	tempo = datetime.now() - inicio

    # Exibe mensagem informando quanto tempo demorou em segundos.
	print(f'Terminou em {tempo.total_seconds():.2f}s.')


# Função computar
def computar(fim: int, pos: int=1) -> None:
    # Variável fator
	fator = 1000 * 1000

    # Enquanto pos for menor que fim:
	while pos < fim:
		pos += 1  # Incrementa 1
		sqrt((pos - fator) * (pos - fator))  # Raiz quadrada

# Execução como script
if __name__ == '__main__':
	main()

# 9.86s	
