#_*_ coding: utf8 _*_

# Imports
from datetime import datetime
from math import sqrt

# Função main
def main():
	
    # Variável de início de execução
	inicio = datetime.now()

    # Chama a função computar (que é definida logo depois)
	computar(fim=50_000_000)

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
