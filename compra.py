from lista import *

class Compra:

    def __init__(self):
        self.compras = aplicacoes()

    def qt_comprado(self):
        entrada5 = input('informe o produto          =')

        for i in range(len(self.compras.listaProdutos)):
            if entrada5 == self.compras.listaProdutos[i].cod:
                entrada2 = int(input('quantidade desejada                 ='))
                self.compras.listaProdutos[i].quantidade += entrada2