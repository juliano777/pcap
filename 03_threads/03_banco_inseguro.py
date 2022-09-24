from random import choice as random_choice
from random import randint as random_randint
from threading import Thread as threading_Thread
from time import sleep as time_sleep
from typing import List as typing_List


class Conta(object):
    def __init__(self, saldo:int=0) -> None:
        self.saldo = saldo


def main() -> None:
    contas = criar_contas()
    total = sum(i.saldo for i in contas)
    print('Iniciando transferências...')

    tarefas = [
        threading_Thread(target=servicos, args=(contas, total)),
        threading_Thread(target=servicos, args=(contas, total)),
        threading_Thread(target=servicos, args=(contas, total)),
        threading_Thread(target=servicos, args=(contas, total)),
        threading_Thread(target=servicos, args=(contas, total)),
        threading_Thread(target=servicos, args=(contas, total)),
    ]

    [i.start() for i in tarefas]
    [i.join() for i in tarefas]
    print('Tarefas completadas.')
    valida_banco(contas, total)


def servicos(contas: Conta, total: int) -> None:
    for _ in range(1, 10_000):
        c1, c2 = pega_duas_contas(contas)
        valor = random_randint(1, 100)
        transferir(c1, c2, valor)
        valida_banco(contas, total)

def criar_contas() -> typing_List[Conta]:
    return [
        Conta(saldo=random_randint(5_000, 10_000)),
        Conta(saldo=random_randint(5_000, 10_000)),
        Conta(saldo=random_randint(5_000, 10_000)),
        Conta(saldo=random_randint(5_000, 10_000)),
        Conta(saldo=random_randint(5_000, 10_000)),
        Conta(saldo=random_randint(5_000, 10_000)),
        Conta(saldo=random_randint(5_000, 10_000)),
    ]

def transferir(origem: Conta, destino:Conta, valor: int) -> None:
    if origem.saldo < valor:
        return

    origem.saldo -= valor
    time_sleep(0.001)
    destino.saldo += valor

def valida_banco(contas: typing_List[Conta], total: int) -> None:
    atual = sum(i.saldo for i in contas)

    if atual != total:
        print('Erro!: Balanço bancário inconsistente:\n'
            f'(BRL) {atual:.2f} vs {total:.2f}',
            flush=True
        )

    else:
        print(f'Balanço bancário consistente: (BRL) {total:.2f}', flush=True)


def pega_duas_contas(contas: typing_List[Conta]) -> tuple:
    c1 = random_choice(contas)
    c2 = random_choice(contas)

    while c1 == c2:
        c2 = random_choice(contas)

    return c1, c2


if __name__ == '__main__':
    main()
