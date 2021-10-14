'''
Level 2
Question 7

Pergunta: Escreva um programa que tenha 2 dígitos, X, Y como entrada 
e gere um array bidimensional. 
O valor do elemento na i-ésima linha e j-ésima coluna da matriz 
deve ser i * j. Nota: i = 0,1 .., X-1; j = 0,1, ¡Y-1. 
Exemplo Suponha que as seguintes entradas sejam fornecidas ao 
programa: 3,5 Então, a saída do programa deve ser: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [ 0, 2, 4, 6, 8]]

Dicas: Nota: No caso de dados de entrada sendo fornecidos para a questão, 
deve ser assumido como uma entrada de console em um formato separado 
por vírgulas.
'''


def calc_create_line(x, y):
    line = []
    for collum in range(x):
        line.append(y*collum)
    return line


def calc_and_create_matriz(x, y):
    matriz = []
    for line in range(x):
        matriz.append(calc_create_line(y, line))

    return matriz
