"""
Exercício 02 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

    >>> from secao_04_exercicios_lista import ex_03_notas_e_media
    >>> notas =['10', '9.5', '8.5', '10']
    >>> ex_03_notas_e_media.input = lambda k: notas.pop(0)
    >>> ex_03_notas_e_media.notas_e_media()
    'As notas foram: 10.0, 9.5, 8.5 e 10.0. Sua média foi: 9.5'
"""

def notas_e_media():
    """Escreva aqui em baixo a sua solução"""
    notas = []
    for i in range(1, 5):
        notas.append(float(input(f'Digite a {i}° nota: ')))
    media = sum(notas) / len(notas)
    return f'As notas foram: {notas[0]}, {notas[1]}, {notas[2]} e {notas[3]}. Sua média foi: {media}'

