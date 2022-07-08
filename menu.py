from aplicacoes import C_loja
#
from produto import *

class Menu:
    def __init__(self):
        loja = C_loja()

        while True:
            entrada_menu = input('Digite\n'
                                 '1 - Cadastrar\n'
                                 '2 - Listar Todos\n'
                                 '3 - Alterar produto \n'
                                 '4 - procurar produto\n'
                                 '5 - sair\n')


            if entrada_menu == '1':
                cod = int(input('digite o codigo'
                                ''))
                quantidade = int(input('informe a quantidade'
                                       ''))
                fabricante = input('fabricante'
                                   '')
                atributo = input('descricao')

            elif entrada_menu == '2':
                loja.lista_produtos()


            elif entrada_menu == '3':
                cod = int(input('Informe o código : '))
                quantidade = int(input('informe a quantidade'
                                       ''))
                fabricante = input('fabricante'
                                   '')
                atributo = input('descricao')

            #elif entrada_menu == '4':

            elif entrada_menu == '5':
                break
