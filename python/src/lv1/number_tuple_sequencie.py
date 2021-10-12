'''
Nível 1
Questão 4

Pergunta: Escreva um programa que aceite uma sequência de números separados
por vírgulas do console e gere uma lista e uma tupla que contém todos os
números. Suponha que a seguinte entrada seja fornecida ao programa:
34,67,55,33,12,98 Então, a saída deve ser:
['34', '67', '55', '33', '12', ' 98 ']
(' 34 ',' 67 ',' 55 ',' 33 ',' 12 ',' 98 ')320

'''


def sequenci(n):
    seq = []
    for item in n:
        seq.append(item)
    return seq, tuple(seq)
