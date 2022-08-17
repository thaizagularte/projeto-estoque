import sqlite3

class action:
    #Função adicionar alimento no estoque/Banco de dados
    def addAlimento(cod, nome, atual, min, max):
        banco = sqlite3.connect('estoque.db')
        cursor = banco.cursor()
        cursor.execute("INSERT INTO Alimentos VALUES("+cod+",'"+nome+"', "+atual+", "+max+", "+min+")")
        banco.commit()
        Estoque()
        banco.close()

    #Função para atualizar o estoque depois dos gastos diários
    def contabilizarGastos(prato, qPrato):
        print(prato, qPrato)

    #Função para excluir um alimento do estoque
    def excluirAlimento(cod, nome):
        banco = sqlite3.connect('estoque.db')
        cursor = banco.cursor()
        cursor.execute("DELETE from Alimentos WHERE codAlim = "+cod+"")
        banco.commit()
        Estoque()
        banco.close()

class Estoque:
    def __init__(self):
        banco = sqlite3.connect('estoque.db')
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM Alimentos")
        self.lista = cursor.fetchall()
        banco.close()

    def listaDados(self):
        return self.lista