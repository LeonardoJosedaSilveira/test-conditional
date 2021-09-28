'''
Nível 1

Pergunta: Com um determinado número integral n, escreva um programa para gerar
um dicionário que contenha (i, i * i) tal que seja um número integral entre 1
e n (ambos incluídos). e então o programa deve imprimir o dicionário. Suponha
que a seguinte entrada seja fornecida ao programa: 8 Então, a saída deve
ser: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64 }

'''


def double(n):
    dic = {}
    for item in range(1, n + 1):
        dic[item] = item*item

    return dic
