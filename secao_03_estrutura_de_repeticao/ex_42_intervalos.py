"""
Exercício 42 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes
intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo.

    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[-1, 10, 15, 20, 50, 13, 78, 22, 14, 16]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    7 número(s) entre o intervalo de zero a 25
    1 número(s) entre o intervalo de 26 a 50
    1 número(s) entre o intervalo de 76 a 100
    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[14, -5, 10, 2, 80, 99]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    2 número(s) entre o intervalo de zero a 25
    2 número(s) entre o intervalo de 76 a 100
    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[-55, 144, 5, 32, 18, 43, 12, 26, 76]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    3 número(s) entre o intervalo de zero a 25
    3 número(s) entre o intervalo de 26 a 50
    1 número(s) entre o intervalo de 76 a 100
    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[3, 5, 100, -5, 70, 88, 28, 12]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    1 número(s) entre o intervalo de zero a 25
    1 número(s) entre o intervalo de 26 a 50
    1 número(s) entre o intervalo de 51 a 75
    1 número(s) entre o intervalo de 76 a 100

"""

def listar_numeros_para_avaliacao():
    """Escreva aqui em baixo a sua solução"""
    def impressao_de_valores(intervalo_um, intervalo_dois, intervalo_tres, intervalo_quatro):
        if len(intervalo_um) > 0:
            print(f"{len(intervalo_um)} número(s) entre o intervalo de zero a 25")
        if len(intervalo_dois) > 0:
            print(f"{len(intervalo_dois)} número(s) entre o intervalo de 26 a 50")
        if len(intervalo_tres) > 0:
            print(f"{len(intervalo_tres)} número(s) entre o intervalo de 51 a 75")
        if len(intervalo_quatro) > 0:
            print(f"{len(intervalo_quatro)} número(s) entre o intervalo de 76 a 100")

    intervalo_um = []
    intervalo_dois = []
    intervalo_tres = []
    intervalo_quatro =[]
    while True:
        valor = int(input(""))
        if valor < 0:
            impressao_de_valores(intervalo_um,intervalo_dois,intervalo_tres,intervalo_quatro)
            break
        elif valor > 1 and valor <= 25:
            intervalo_um.append(valor)
        elif valor > 25 and valor <= 50:
            intervalo_dois.append(valor)
        elif valor > 50 and valor <= 75:
            intervalo_tres.append(valor)
        elif valor > 75 and valor <= 100:
            intervalo_quatro.append(valor)
        else:
            pass