'''
Level 2
Question 6

Escreva um programa que calcule e imprima o valor de acordo com a fórmula 
fornecida: Q = Raiz quadrada de [(2 * C * D) / H] A seguir estão os valores 
fixos de C e H: C é 50. H é 30 .D é a variável cujos valores devem ser inseridos 
em seu programa em uma seqüência separada por vírgulas. Exemplo Vamos supor que a 
seguinte seqüência de entrada separada por vírgulas seja fornecida ao 
programa: 100,150,180 A saída do programa deve ser: 18,22,24

Dicas: Se a saída recebida estiver no formato decimal, deve ser arredondado 
para o valor mais próximo (por exemplo, se a saída recebida for 26,0, deve ser 
impresso como 26). No caso de dados de entrada sendo fornecidos para a questão,
deve ser considerada uma entrada do console.
'''

import math


def calc_extra_sqrt(n):
    result = []
    for item in n:
        vraw = (2 * 50 * item) / 30
        result.append(round(math.sqrt(vraw)))

    return result
