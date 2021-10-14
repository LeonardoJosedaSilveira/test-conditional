'''
Level 2
Question 8

Pergunta: Escreva um programa que aceite uma sequência de palavras
separadas por vírgulas como entrada e imprima as palavras em uma
sequência separada por vírgulas após classificá-las em ordem alfabética.
Suponha que a seguinte entrada seja fornecida ao programa: without, hello,
bag, world Então, a saída deve ser: bag, hello, without, world

Dicas: No caso de dados de entrada fornecidos para a pergunta,
deve ser considerada uma entrada do console.
'''


def words_order(words):
    result = '-'
    words_list = words.split(',')
    complete_list = sorted([word.strip() for word in words_list])

    for word in complete_list:
        if result == '-':
            result = word.strip()
        else:
            result += ', {}'.format(word.strip())

    return result
