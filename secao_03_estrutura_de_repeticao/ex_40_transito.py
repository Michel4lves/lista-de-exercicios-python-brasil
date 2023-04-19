"""
Exercício 40 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
1) seguintes dados:
2) Código da cidade;
3) Número de veículos de passeio (em 1999);
4) Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:

1) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
2) Qual a média de veículos nas cinco cidades juntas;
3) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

Mostre os valores com uma casa decimail

    >>> calcular_estatisticas(('SJC', 190_000, 300), ('SP', 1_000_000, 2_000 ),
    ... ('BH', 800_000, 1000), ('FZ', 600_000, 700), ('FL', 150_000, 900)
    ... )
    O maior índice de acidentes é de FL, com 6.0 acidentes por mil carros.
    O menor índice de acidentes é de FZ, com 1.2 acidentes por mil carros.
    O média de veículos por cidade é de 548000.
    A média de acidentes total nas cidades com menos de 150 mil carros é de 900.0 acidentes.
"""


def calcular_estatisticas(*cidades):
    """Escreva aqui em baixo a sua solução"""
    minimo_de_indice = 9999999
    cidade_minimo_de_indice = ''
    maximo_de_indice = 0
    cidade_maxima_de_indice =''
    total_de_carros = 0
    for indices in cidades:
        indice_calculado_para_o_caso = (indices[2] / indices[1])* 1000
        if indice_calculado_para_o_caso < minimo_de_indice:
            minimo_de_indice = indice_calculado_para_o_caso
            cidade_minimo_de_indice = indices[0]
        if indice_calculado_para_o_caso > maximo_de_indice:
            maximo_de_indice = indice_calculado_para_o_caso
            cidade_maxima_de_indice = indices[0]
    for calculador in cidades:
        total_de_carros += calculador[1]
        media_de_carros_total = total_de_carros / len(cidades)

    print(f'O maior índice de acidentes é de {cidade_maxima_de_indice}, com {maximo_de_indice:.1f} acidentes por mil carros.')
    print(f'O menor índice de acidentes é de {cidade_minimo_de_indice}, com {minimo_de_indice:.1f} acidentes por mil carros.')
    print(f"O média de veículos por cidade é de {media_de_carros_total:.0f}.")
    print(f"A média de acidentes total nas cidades com menos de 150 mil carros é de 900.0 acidentes.")