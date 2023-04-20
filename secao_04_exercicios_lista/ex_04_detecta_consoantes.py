"""
Exercício 02 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

    >>> from secao_04_exercicios_lista import ex_04_detecta_consoantes
    >>> notas =['p', 'y', 't', 'h', 'o', 'n', 'b', 'r', 'a', 's']
    >>> ex_04_detecta_consoantes.input = lambda k: notas.pop(0)
    >>> ex_04_detecta_consoantes.ler_consoantes()
    'Foram lidas 8 consoantes: P Y T H N B R S'
"""

def ler_consoantes():
    """Escreva aqui em baixo a sua solução"""
    lista_consoantes = []
    lista_vogais = []
    for _ in range(10):
        letras = input('Digite uma letra qualquer: ').upper()
        if letras in ['A', 'E', 'I', 'O', 'U']:
            lista_vogais.append(letras)
        else:
            lista_consoantes.append(letras)
    numero_de_consoantes = len(lista_consoantes)
    # print(' '.join(lista_consoantes))
    consoantes = ' '.join([str(letra) for letra in lista_consoantes])
    return f'Foram lidas {numero_de_consoantes} consoantes: {consoantes}'

