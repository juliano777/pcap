
from queue import Queue as queue_Queue
from threading import Thread as threading_Thread
from time import sleep as time_sleep


from colorama import Fore

def main() -> None:
    print(f'{Fore.YELLOW}Sistema iniciado!', flush=True)
    queue = queue_Queue()
    th1 = threading_Thread(target=gerador_de_dados, args=(queue,))
    th2 = threading_Thread(target=consumidor_de_dados, args=(queue,))
    th1.start()
    th1.join()

    th2.start()
    th2.join()

def gerador_de_dados(queue: queue_Queue) -> None:
    for i in range(1, 11):
        print(f'{Fore.GREEN}Dado {i} gerado.', flush=True)
        time_sleep(2)
        queue.put(i)

def consumidor_de_dados(queue: queue_Queue) -> None:        
    while queue.qsize() > 0:
        valor = queue.get()
        print(f'{Fore.BLUE}Dado: {valor * 2}.', flush=True)
        time_sleep(1)
        queue.task_done()

if __name__ == '__main__':
    main()
