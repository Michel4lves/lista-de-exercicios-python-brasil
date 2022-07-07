"""
Exercício 24 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
operação deve ser acompanhado de uma frase que diga se o número é:
  par ou ímpar;
  positivo ou negativo;
  inteiro ou decimal.

Mostre o restultado com duas casas decimais

    >>> fazer_operacao_e_classificar(2, 3, '+')
    Resultado: 5.00
    Número é impar, positivo e inteiro.
    >>> fazer_operacao_e_classificar(-4, 2, '/')
    Resultado: -2.00
    Número é par, negativo e inteiro.
    >>> fazer_operacao_e_classificar(0, 2, '*')
    Resultado: 0.00
    Número é par, neutro e inteiro.
    >>> fazer_operacao_e_classificar(-3.14, 2, '*')
    Resultado: -6.28
    Número é negativo e decimal.
    >>> fazer_operacao_e_classificar(3.14, 2, '-')
    Resultado: 1.14
    Número é positivo e decimal.

"""


def fazer_operacao_e_classificar(n_1: float, n_2: float, operacao: str):
    """Escreva aqui em baixo a sua solução"""

    import math

    resultado = 0
    par_x_impar = positivo_x_negativo = decimal_x_inteiro = ''

    if operacao == "+":
        resultado = n_1 + n_2
    elif operacao == "-":
        resultado = n_1 - n_2
    elif operacao == "*":
        resultado = n_1 * n_2
    elif operacao == "/":
        resultado = n_1 / n_2
    print(f'Resultado: {resultado:.2f}')

    if resultado > 0:
        positivo_x_negativo = 'positivo'
    elif resultado < 0:
        positivo_x_negativo = 'negativo'
    else:
        positivo_x_negativo = 'neutro'

    n_inteiro = math.floor(resultado / 1)
    n_decimal = resultado - n_inteiro

    if n_decimal != 0:
        decimal_x_inteiro = 'decimal'
    else:
        decimal_x_inteiro = 'inteiro'

    if resultado == 0:
        par_x_impar = 'par'
    elif resultado == 1:
        par_x_impar = 'impar'
    elif resultado >= 2 or resultado < 0:
        par, resultado = divmod(resultado, 2)
        if resultado != 0:
            par_x_impar = 'impar'
        else:
            par_x_impar = 'par'

    if decimal_x_inteiro == 'inteiro':
        print(f"Número é {par_x_impar}, {positivo_x_negativo} e {decimal_x_inteiro}.")
    else:
        print(f"Número é {positivo_x_negativo} e {decimal_x_inteiro}.")
