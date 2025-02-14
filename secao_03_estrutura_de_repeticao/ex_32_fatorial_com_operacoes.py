"""
Exercício 32 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120

    >>> calcular_fatorial(1)
    Fatorial de 1:
    1! = 1 = 1
    >>> calcular_fatorial(2)
    Fatorial de 2:
    2! = 2 . 1 = 2
    >>> calcular_fatorial(3)
    Fatorial de 3:
    3! = 3 . 2 . 1 = 6
    >>> calcular_fatorial(4)
    Fatorial de 4:
    4! = 4 . 3 . 2 . 1 = 24
    >>> calcular_fatorial(5)
    Fatorial de 5:
    5! = 5 . 4 . 3 . 2 . 1 = 120

"""
def calcular_fatorial(n: int) -> int:
    """Escreva aqui em baixo a sua solução"""
    def resultado_do_fatorial(n):
        fatorial = 1
        for n in range(n, 0, -1):
            fatorial *= n
            print(f"{n}{' .' if n > 1 else ''} ", end="")
        return fatorial

    print(f"Fatorial de {n}:")
    print(f"{n}! = ", end ="")
    # print(f"{n}{' .' if n > 1 else ''} ", end="")
    fatorial = resultado_do_fatorial(n)
    print(f"= {fatorial}")

