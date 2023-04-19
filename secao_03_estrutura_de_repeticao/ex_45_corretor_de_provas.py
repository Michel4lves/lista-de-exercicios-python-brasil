"""
Exercício 45 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno
a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a
nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro
aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma com uma casa decimal.

Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

    >>> corrigir(('Renzo','A','B','C','D','E','E','D','C','B','A' ))
    Aluno                 Nota
    Renzo                 10
    ---------------------------
    Média geral: 10.0
    Maior nota: 10
    Menor nota: 10
    Total de Alunos: 1
    >>> corrigir(
    ... ('Renzo','A','B','C','D','E','E','D','C','B','A' ),
    ... ('Fulano','A','B','C','D','E','E','D','C','B','B' ),
    ... )
    Aluno                 Nota
    Renzo                 10
    Fulano                 9
    ---------------------------
    Média geral: 9.5
    Maior nota: 10
    Menor nota: 9
    Total de Alunos: 2
"""




def corrigir(*provas):
    """Escreva aqui em baixo a sua solução"""

    def calcular_nota(prova):
        gabarito = ('Nome', 'A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A')
        total_da_nota = 0
        nome_do_aluno = ''
        for resposta_correta, nota_prova in zip(gabarito, prova):
            if resposta_correta == 'Nome':
                nome_do_aluno = prova[0]
            elif resposta_correta == nota_prova:
                total_da_nota += 1
        return nome_do_aluno, total_da_nota

    print('Aluno                 Nota')
    soma_das_notas = 0
    min_nota = 99999
    max_nota = -1
    for prova in provas:
        nome_do_aluno, total_da_nota = calcular_nota(prova)
        soma_das_notas += total_da_nota
        if total_da_nota > max_nota:
            max_nota = total_da_nota
        if total_da_nota < min_nota:
            min_nota = total_da_nota
        print(f'{nome_do_aluno}                 {total_da_nota}')
    print('---------------------------')
    print(f'Média geral: {soma_das_notas/len(provas)}')
    print(f'Maior nota: {max_nota}')
    print(f'Menor nota: {min_nota}')
    print(f'Total de Alunos: {len(provas)}')