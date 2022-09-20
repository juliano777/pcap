#_*_ coding: utf8 _*_

from datetime import datetime
from math import sqrt


def main():
	inicio = datetime.now()

	computar(fim=50_000_000)

	tempo = datetime.now() - inicio

	print(f'Terminou em {tempo.total_seconds():.2f}s.')


def computar(fim: int, pos: int=1) -> None:
	fator = 1000 * 1000

	while pos < fim:
		pos += 1
		sqrt((pos - fator) * (pos - fator))

if __name__ == '__main__':
	main()

# 9.86s	
