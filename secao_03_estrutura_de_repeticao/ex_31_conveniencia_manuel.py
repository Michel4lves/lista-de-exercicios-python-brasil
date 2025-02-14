"""
Exercício 31 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

FO Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de
valores referentes aos preços das mercadorias.
Um valor zero deve ser informado pelo operador para indicar o final da compra.
Um valor -1 deve ser informado pelo operador para finalizar o programas
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então
calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial,
para registrar a próxima compra.

    >>> from secao_03_estrutura_de_repeticao import ex_31_conveniencia_manuel
    >>> entradas = ['-1']  # Encerrando o programa sem nenhuma compra
    >>> ex_31_conveniencia_manuel.input = lambda k: entradas.pop()
    >>> ex_31_conveniencia_manuel.rodar_programa_de_caixa()
    Lojas Tabajara
    -------------------
    Programa encerrado!
    >>> entradas = ['2.00', '-1', '1.99']  # Compra de apenas um produto
    >>> ex_31_conveniencia_manuel.input = lambda k: entradas.pop()
    >>> ex_31_conveniencia_manuel.rodar_programa_de_caixa()
    Lojas Tabajara
    Total     : R$   1.99
    Dinheiro  : R$   2.00
    Troco     : R$   0.01
    -------------------
    Programa encerrado!
    >>> entradas = ['5.00', '-1', '1.99', '1.99']  # Compra de dois produtos
    >>> ex_31_conveniencia_manuel.input = lambda k: entradas.pop()
    >>> ex_31_conveniencia_manuel.rodar_programa_de_caixa()
    Lojas Tabajara
    Total     : R$   3.98
    Dinheiro  : R$   5.00
    Troco     : R$   1.02
    -------------------
    Programa encerrado!
    >>> entradas = ['10.00', '-1', '5.35', '5.00', '0', '1.98', '1.99']  # Compra de dois produtos
    >>> ex_31_conveniencia_manuel.input = lambda k: entradas.pop()
    >>> ex_31_conveniencia_manuel.rodar_programa_de_caixa()
    Lojas Tabajara
    Total     : R$   3.97
    Dinheiro  : R$   5.00
    Troco     : R$   1.03
    -------------------
    Lojas Tabajara
    Total     : R$   5.35
    Dinheiro  : R$  10.00
    Troco     : R$   4.65
    -------------------
    Programa encerrado!

"""

def gerar_nota_fiscal(valores_com_lista_de_produtos, total_da_compra, pgto_do_cliente):
    print("Lojas Tabajara")
    if len(valores_com_lista_de_produtos) != 0:
        print(f"Total     : R${total_da_compra:7.2f}")
        print(f"Dinheiro  : R${pgto_do_cliente:7.2f}")
        print(f"Troco     : R${(pgto_do_cliente - total_da_compra):7.2f}")
    print("-------------------")

def rodar_programa_de_caixa():
    """Escreva aqui em baixo a sua solução"""
    valores_com_lista_de_produtos = []
    total_da_compra = 0
    pgto_do_cliente = 0
    while True:
        valor_do_input = float(input(""))
        if valor_do_input == -1:
            try:
                pgto_do_cliente = float(input("Pagamento do cliente"))
                gerar_nota_fiscal(valores_com_lista_de_produtos, total_da_compra, pgto_do_cliente)
            except:
                gerar_nota_fiscal(valores_com_lista_de_produtos, total_da_compra, pgto_do_cliente)
            break
        if valor_do_input == 0:
            pgto_do_cliente = float(input("Pagamento do cliente"))
            gerar_nota_fiscal(valores_com_lista_de_produtos, total_da_compra, pgto_do_cliente)
            valores_com_lista_de_produtos = []
        else:
            valores_com_lista_de_produtos.append(valor_do_input)
            total_da_compra = sum(valores_com_lista_de_produtos)
    print("Programa encerrado!")
