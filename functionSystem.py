from configparser import NoOptionError
import sqlite3
banco = sqlite3.connect('estoque.db')

class action:
    #Função adicionar alimento no estoque/Banco de dados
    def addAlimento(cod, nome, atual, min, max):
        cursor = banco.cursor()
        cursor.execute("INSERT INTO Alimentos VALUES("+cod+",'"+nome+"', "+atual+", "+max+", "+min+")")
        nome =  str(nome).upper()
        cursor.execute("ALTER TABLE Pratos ADD COLUMN '"+nome+"' TEXT")
        banco.commit()

    #Função para atualizar o estoque depois dos gastos diários
    def contabilizarGastos(prato, qPrato):
        print(prato, qPrato)

    #Função para excluir um alimento do estoque
    def excluirAlimento(cod, nome):
        cursor = banco.cursor()
        cursor.execute("DELETE from Alimentos WHERE codAlim = "+cod+"")
        banco.commit()