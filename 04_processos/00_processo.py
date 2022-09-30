# _*_ coding: utf8 _*_

from multiprocessing import Process as mp_Process
from multiprocessing import current_process as mp_current_process


# msg = lambda n=mp_current_process().name: f'Nome do processo atual: {n}'
def msg(n: str = mp_current_process().name) -> str:
    return f'Nome do processo atual: {n}'


def faz_algo() -> None:
    print(msg())


def main() -> None:
    linha = '-' * 79

    print(msg())

    print(linha)

    p = (
            mp_Process(
                target=faz_algo,                
                name='Processo Rumpelstiltskin'
                ),
            mp_Process(target=faz_algo),
            mp_Process(target=faz_algo),
        )

    # Exibe o nome dos processos
    [print(i.name) for i in p]

    print(linha)

    # xxxxxx
    [i.start() for i in p]

    # xxxxxx
    [i.join() for i in p]


if __name__ == '__main__':
    main()
