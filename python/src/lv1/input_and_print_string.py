'''
nivel 1
Questão 5

Defina uma classe que tenha pelo menos dois métodos: 
  getString: 
      para obter uma string da entrada do console 
  printString: 
      para imprimir a string em maiúsculas. Também inclua uma função de teste 
      simples para testar os métodos da classe.

Dicas: Use o método init para construir alguns parâmetros
'''


class Get_Up_String:
    def __init__(self):
        self.phrase = ''

    def in_phrase(self):
        self.phrase = input().upper()

    def out_phrase(self):
        print(self.phrase)
