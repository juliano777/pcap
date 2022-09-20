from threading import Thread as threading_Thread
from time import sleep as time_sleep

def main() -> None:
    threads = (
        threading_Thread(target=contar, args=('elefante', 10)),
        threading_Thread(target=contar, args=('buraco', 8)),
        threading_Thread(target=contar, args=('moeda', 23)),
        threading_Thread(target=contar, args=('pato', 12)),
    )

    # Adiciona as threads na pool de threads prontas para execução
    [i.start() for i in threads]

    print('======== Podemos fazer outras coisas no programa enquanto'
            ' a thread é executada ========')
    time_sleep(3)
    print('======== Curso de Performance em Python ========')

    # Avisa para aguardar até as threads terminarem a execução
    [i.join() for i in threads]

    print('======== Execução finalizada! ========')

def contar(objeto: str, num: int) -> None:
    for i in range(1, num+1):
        print(f'{i} {objeto}s...')
        time_sleep(1)

if __name__ == '__main__':
    main()
