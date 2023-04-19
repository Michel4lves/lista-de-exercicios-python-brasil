"""
Exercício 39 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o nome do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o nome do aluno mais alto
 e o número do aluno mais baixo, junto com suas alturas.
    >>> calcular_aluno_mais_baixo_e_mais_alto(('Renzo', 162))
    'O maior aluno é o Renzo com 162 cm. O menor aluno é o Renzo com 162 cm'
    >>> calcular_aluno_mais_baixo_e_mais_alto(('Renzo', 162), ('Clara', 165))
    'O maior aluno é o Clara com 165 cm. O menor aluno é o Renzo com 162 cm'
    >>> calcular_aluno_mais_baixo_e_mais_alto(('Renzo', 162), ('Clara', 165), ('Oscar', 199))
    'O maior aluno é o Oscar com 199 cm. O menor aluno é o Renzo com 162 cm'

"""


def calcular_aluno_mais_baixo_e_mais_alto(*alunos) -> str:
    """Escreva aqui em baixo a sua solução"""
    altura_min = 99999
    altura_max = 0
    nome_da_altura_min = ''
    nome_da_altura_max = ''
    for aluno in alunos:
        if aluno[1] < altura_min:
            altura_min = aluno[1]
            nome_da_altura_min = aluno[0]
        if aluno[1] > altura_max:
           altura_max = aluno[1]
           nome_da_altura_max = aluno[0]
    return f'O maior aluno é o {nome_da_altura_max} com {altura_max} cm. O menor aluno é o {nome_da_altura_min} com {altura_min} cm'
