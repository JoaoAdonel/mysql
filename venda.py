from lista import *

class Venda:
    def __init__(self):
        self.vender = aplicacoes()



    def vendido(self):
        entrada4 =  input('informe o produto          =')

        for i in range(len(self.vender.listaProdutos)):
            if entrada4 == self.vender.listaProdutos[i].cod:
                entrada6 = int(input('quantidade desejada                 ='))
                self.vender.listaProdutos[i].quantidade -= entrada6