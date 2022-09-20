from threading import Thread as threading_Thread
from time import sleep as time_sleep

def main():
    th = threading_Thread(target=contar, args=('elefante', 10))

    # Adiciona a thread na pool de threads prontas para execução
    th.start()

    print('Podemos fazer outras coisas no programa enquanto a thread'
            ' é executada')
    time_sleep(3)
    print('Curso de Performance em Python')

    # Avisa para aguardar até a thread terminar a execução
    th.join()

    print('Execução finalizada!')

def contar(objeto: str, num: int) -> None:
    for i in range(1, num+1):
        print(f'{i} {objeto}s...')
        time_sleep(1)

if __name__ == '__main__':
    main()
