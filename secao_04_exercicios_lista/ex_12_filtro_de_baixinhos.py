"""
Exercício 12 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Foram anotados os nomes, as idades e alturas de de vários alunos.
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses
alunos.

Mostre a média com uma casa decimal.

    >>> calcular_baixinhos_com_mais_de_13_anos(('Renzo', 39, 162))
    Média de altura: 162.0 centímetros.
    Não há nenhum aluno abaixo da média
    >>> calcular_baixinhos_com_mais_de_13_anos(('Renzo', 39, 162), ('Priscila', 33, 158))
    Média de altura: 160.0 centímetros.
    Existe(m) 1 aluno(s) com altura abaixo da média com mais de 13 anos:
    1. Priscila, com 158 centímetros e 33 ano(s) de idade
    >>> calcular_baixinhos_com_mais_de_13_anos(('Renzo', 39, 162), ('Priscila', 33, 158), ('Gigante', 20, 210))
    Média de altura: 176.7 centímetros.
    Existe(m) 2 aluno(s) com altura abaixo da média com mais de 13 anos:
    1. Renzo, com 162 centímetros e 39 ano(s) de idade
    2. Priscila, com 158 centímetros e 33 ano(s) de idade
    >>> calcular_baixinhos_com_mais_de_13_anos(
    ...     ('Renzo', 39, 162), ('Priscila', 33, 158), ('Gigante', 20, 210), ('Criança', 7, 100)
    ... )
    Média de altura: 157.5 centímetros.
    Não há nenhum aluno abaixo da média
    >>> calcular_baixinhos_com_mais_de_13_anos(
    ...     ('Renzo', 39, 162), ('Priscila', 33, 158), ('Gigante', 20, 210),
    ...     ('Criança', 7, 100), ("Shaquille O'Neal", 25, 216)
    ... )
    Média de altura: 169.2 centímetros.
    Existe(m) 2 aluno(s) com altura abaixo da média com mais de 13 anos:
    1. Renzo, com 162 centímetros e 39 ano(s) de idade
    2. Priscila, com 158 centímetros e 33 ano(s) de idade

"""


def calcular_baixinhos_com_mais_de_13_anos(*alunos):
    """Escreva aqui em baixo a sua solução"""
    media_de_altura = 0
    altura_acumulado = 0
    contador = 0
    classificador = 1
    for nome, idade, altura in alunos:
        altura_acumulado += altura
        media_de_altura = altura_acumulado/len(alunos)
    print(f"Média de altura: {media_de_altura:.1f} centímetros.")
    for nome, idade, altura in alunos:
        if idade > 13:
            if altura < media_de_altura:
                contador += 1
    if contador > 0:
        print(f'Existe(m) {contador} aluno(s) com altura abaixo da média com mais de 13 anos:')
    else:
        print("Não há nenhum aluno abaixo da média")
    for i, (nome, idade, altura) in enumerate(alunos):
        if idade > 13:
            if altura < media_de_altura:
                print(f'{classificador}. {nome}, com {altura} centímetros e {idade} ano(s) de idade')
                classificador += 1


