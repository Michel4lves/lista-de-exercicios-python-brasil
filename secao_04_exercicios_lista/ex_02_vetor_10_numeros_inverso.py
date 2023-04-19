"""
Exercício 02 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

    >>> from secao_04_exercicios_lista import ex_02_vetor_10_numeros_inverso
    >>> numeros =['0', '1', '2.5', '3', '4', '5', '6.5', '7.7', '8', '9']
    >>> ex_02_vetor_10_numeros_inverso.input = lambda k: numeros.pop(0)
    >>> ex_02_vetor_10_numeros_inverso.ler_10_valores_inverso()
    [9.0, 8.0, 7.7, 6.5, 5.0, 4.0, 3.0, 2.5, 1.0, 0.0]
"""

def ler_10_valores_inverso():
    """Escreva aqui em baixo a sua solução"""
    lista = []
    for n in range(1, 11):
        lista.append(float(input(f'Digite o {n}° número: ')))
    lista.reverse()
    return lista
