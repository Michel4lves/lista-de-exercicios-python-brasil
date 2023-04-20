"""
Exercício 01 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosComStrings

Tamanho de strings. Faça um programa que compare 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings

String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.

    >>> comparar('Brasil Hexa 2026', 'Brasil! Hexa 2026!')
    String 1: Brasil Hexa 2026
    String 2: Brasil! Hexa 2026!
    Tamanho de "Brasil Hexa 2026": 16 caracteres
    Tamanho de "Brasil! Hexa 2026!": 18 caracteres
    As duas strings são de tamanhos diferentes
    As duas strings possuem conteúdo diferentes
    >>> comparar('python pro', 'python pro')
    String 1: python pro
    String 2: python pro
    Tamanho de "python pro": 10 caracteres
    Tamanho de "python pro": 10 caracteres
    As duas strings são de tamanhos iguais
    As duas strings possuem conteúdos iguais
    >>> comparar('python pro', 'python bra')
    String 1: python pro
    String 2: python bra
    Tamanho de "python pro": 10 caracteres
    Tamanho de "python bra": 10 caracteres
    As duas strings são de tamanhos iguais
    As duas strings possuem conteúdo diferentes

"""


def comparar(s1: str, s2: str):
    """Escreva aqui em baixo a sua solução"""
    tamanho_s1 = len(s1)
    tamanho_s2 = len(s2)
    print(f"String 1: {s1}")
    print(f"String 2: {s2}")
    print(f'Tamanho de "{s1}": {tamanho_s1} caracteres')
    print(f'Tamanho de "{s2}": {tamanho_s2} caracteres')
    if s1 == s2:
        print('As duas strings são de tamanhos iguais')
        print('As duas strings possuem conteúdos iguais')
    else:
        if tamanho_s1 == tamanho_s2:
            print('As duas strings são de tamanhos iguais')
            print('As duas strings possuem conteúdo diferentes')
        else:
            print('As duas strings são de tamanhos diferentes')
            print('As duas strings possuem conteúdo diferentes')