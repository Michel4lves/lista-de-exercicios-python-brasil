"""
Exercício 43 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que receba os itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido e quantidade de itens
comprados.


    >>> fechar_conta()
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          0 |       0.00 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          1 |       1.20 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          1 |       1.20 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          3 |       3.60 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          5 |       6.20 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          8 |      10.70 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         12 |      15.50 |
    -----------------------------------------------------------------------------

    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4), ('104', 5))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    | Cheeseburger     | 104    | 1.30                |          5 |       6.50 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         17 |      22.00 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4), ('105', 6))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    | Refrigerante     | 105    | 1.00                |          6 |       6.00 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         18 |      21.50 |
    -----------------------------------------------------------------------------

"""


def fechar_conta(*itens):
    """Escreva aqui em baixo a sua solução"""
    produtos = {'100': 0, '101': 0, '102': 0, '103': 0, '104': 0, '105': 0}
    total_de_itens = 0

    for chave, quantidade in itens:
        produtos[chave] += quantidade
        total_de_itens += quantidade

    qtd_cachorro_quente, qtd_bauru_simples, qtd_bauru_com_ovo, qtd_hamburger, qtd_cheeseburguer, qtd_refrigerante = produtos.values()

    cachorro_quente = qtd_cachorro_quente * 1.20
    bauru_simples = qtd_bauru_simples * 1.30
    bauru_com_ovo = qtd_bauru_com_ovo * 1.50
    hamburger = qtd_hamburger * 1.20
    cheeseburguer = qtd_cheeseburguer * 1.30
    refrigerante = qtd_refrigerante * 1.00
    total = cachorro_quente + bauru_simples + bauru_com_ovo + hamburger + cheeseburguer + refrigerante
    nota_fiscal(qtd_cachorro_quente, cachorro_quente, qtd_bauru_simples, bauru_simples, bauru_com_ovo, qtd_bauru_com_ovo, hamburger, qtd_hamburger,
                cheeseburguer, qtd_cheeseburguer, total, total_de_itens, refrigerante, qtd_refrigerante)

def nota_fiscal(qtd_cachorro_quente, cachorro_quente, qtd_bauru_simples, bauru_simples, bauru_com_ovo, qtd_bauru_com_ovo, hamburger, qtd_hamburger,
                cheeseburguer, qtd_cheeseburguer, total, total_de_itens, refrigerante, qtd_refrigerante):
    print('_____________________________________________________________________________')
    print('|                              RESUMO DA CONTA                              |')
    print('|---------------------------------------------------------------------------|')
    print('| Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |')
    if cachorro_quente > 0:
        print(f'| Cachorro Quente  | 100    | 1.20                |          {qtd_cachorro_quente} |       {cachorro_quente:.2f} |')
    if bauru_simples > 0:
        print(
            f'| Bauru Simples    | 101    | 1.30                |          {qtd_bauru_simples} |       {bauru_simples:.2f} |')
    if bauru_com_ovo > 0:
        print(
            f'| Bauru com Ovo    | 102    | 1.50                |          {qtd_bauru_com_ovo} |       {bauru_com_ovo:.2f} |')
    if hamburger > 0:
        print(
            f'| Hamburger        | 103    | 1.20                |          {qtd_hamburger} |       {hamburger:.2f} |')
    if cheeseburguer > 0:
        print(
            f'| Cheeseburger     | 104    | 1.30                |          {qtd_cheeseburguer} |       {cheeseburguer:.2f} |')
    if refrigerante > 0:
        print(
            f'| Refrigerante     | 105    | 1.00                |          {qtd_refrigerante} |       {refrigerante:.2f} |')
    print('|---------------------------------------------------------------------------|')
    print(f'| Total Geral:                                    | {total_de_itens:10d} | {total:10.2f} |')
    print('-----------------------------------------------------------------------------')
