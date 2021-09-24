'''
Nível 1

Pergunta: Escreva um programa que possa calcular o fatorial de um determinado número.
Os resultados devem ser impressos em uma seqüência separada por vírgulas em uma única linha.
Suponha que a seguinte entrada seja fornecida ao programa: 8 Então, a saída deve ser: 40320

'''


def fatorial(n):
    value = 1
    for item in range(1, n + 1):
        value = value * item
    return value
