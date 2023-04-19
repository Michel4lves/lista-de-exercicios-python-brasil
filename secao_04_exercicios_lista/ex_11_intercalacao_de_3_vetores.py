"""
Exercício 11 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Altere o programa anterior, intercalando 3 vetores.

    >>> intercalar([], [], [])
    []
    >>> intercalar([1], [2], [3])
    [1, 2, 3]
    >>> intercalar([1, 2], [3, 4], [5, 6])
    [1, 3, 5, 2, 4, 6]
    >>> intercalar(list(range(5)), list(range(5, 10)), list(range(10, 15)))
    [0, 5, 10, 1, 6, 11, 2, 7, 12, 3, 8, 13, 4, 9, 14]

"""


def intercalar(lista_1: list, lista_2: list, lista_3: list) -> list:
    """Escreva aqui em baixo a sua solução"""
    lista_resposta =[]
    for v1, v2, v3  in zip (lista_1,lista_2,lista_3):
        lista_resposta.append(v1)
        lista_resposta.append(v2)
        lista_resposta.append(v3)
    return lista_resposta
