'''
Questão 1
Nível 1

Pergunta: Escreva um programa que encontre todos os números divisíveis por 7,
mas não múltiplos de 5, entre 2000 e 3200 (ambos incluídos).
Os números obtidos devem ser impressos em seqüência separada por vírgulas em uma única linha.
'''


def multiply():
    list = set()
    for item in range(2000, 3201):
        if (item % 7) == 0 and (item % 5) != 0:
            list.add(item)
    return sorted(list)
