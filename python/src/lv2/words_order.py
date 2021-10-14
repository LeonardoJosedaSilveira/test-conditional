'''
Level 2
Question 8

Pergunta: Escreva um programa que aceite uma sequência de palavras 
separadas por vírgulas como entrada e imprima as palavras em uma 
sequência separada por vírgulas após classificá-las em ordem alfabética. 
Suponha que a seguinte entrada seja fornecida ao programa: without, hello, 
bag, world Então, a saída deve ser: bag, hello, without, world

Dicas: No caso de dados de entrada fornecidos para a pergunta, deve ser considerada uma entrada do console.
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
