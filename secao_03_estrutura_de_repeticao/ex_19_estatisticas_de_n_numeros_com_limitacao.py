"""
Exercício 19 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

    >>> calcular_estatisticas()
    'Maior valor: não existe. Menor valor: não existe. Soma: 0'
    >>> calcular_estatisticas(1)
    'Maior valor: 1. Menor valor: 1. Soma: 1'
    >>> calcular_estatisticas(1, 2)
    'Maior valor: 2. Menor valor: 1. Soma: 3'
    >>> calcular_estatisticas(1, 2, -1)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, -10)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, 1001)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, 1198)
    'Somente números de 0 a 1000 são permitidos'

"""


def calcular_estatisticas(*numeros) -> str:
    """Escreva aqui em baixo a sua solução"""
    if len(numeros) == 0:
        return 'Maior valor: não existe. Menor valor: não existe. Soma: 0'
    intervalo_valido = set(range(0, 1001))
    lista_vazia = set(numeros).difference(intervalo_valido)
    if len(lista_vazia) == 0:
        lista_org = sorted(numeros)
        soma = sum(lista_org)
        return f'Maior valor: {lista_org[-1]}. Menor valor: {lista_org[0]}. Soma: {soma}'
    return 'Somente números de 0 a 1000 são permitidos'
