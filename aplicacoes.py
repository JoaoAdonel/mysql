from mysql.connector import *
from produto import Produto


class C_loja:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='q1w2e3',
            database='loja')
        self.mycursor = self.conexao.cursor



    def cadastrar_produto(self,cod,descricao,fabricante,quantidade):
        obj_contato = Produto( cod, descricao, fabricante, quantidade)
        commando_sql = f'insert into Produtos ' \
                       f'(cod, descricao, fabricante, quantidade)value'\
                       f'("{obj_contato.cod}",'\
                       f'"{obj_contato.descricao}",'\
                       f'"{obj_contato.fabricante}"'\
                       f',"{obj_contato.quantidade}")'
        self.mycursor.execute(commando_sql)
        self.conexao.commit()

    def lista_produtos(self):
        comando_sql = f'select * from Produtos'
        self.mycursor.execute(comando_sql)
        lista = self.mycursor.fetchall()
        for i in lista:
            print(i)

    def alterar_descricao(self, atributo,descricao , cod):
        comando_sql = f'update Produtos set {atributo} = "{descricao}" where id = {cod}'
        self.mycursor.execute(comando_sql)
        self.conexao.commit()














































