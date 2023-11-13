import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget

class MinhaAplicacao(QMainWindow):
    def __init__(self):
        super(MinhaAplicacao, self).__init__()

        self.setWindowTitle("Tabela de Itens")
        self.setGeometry(100, 100, 800, 400)

        # Layout principal
        layout = QVBoxLayout()

        # Tabela
        self.tabela = QTableWidget(self)
        self.tabela.setColumnCount(5)  # Colunas: ID, Nome, Quantidade, Categoria, Ações
        self.tabela.setHorizontalHeaderLabels(["ID", "Nome", "Quantidade", "Categoria", "Ações"])
        layout.addWidget(self.tabela)

        # Dados de exemplo
        dados_exemplo = [
            {"id": 1, "nome": "Item 1", "quantidade": 5, "categoria": "Eletrônico"},
            {"id": 2, "nome": "Item 2", "quantidade": 10, "categoria": "Decoração"},
            {"id": 3, "nome": "Item 3", "quantidade": 3, "categoria": "Eletrodoméstico"},
        ]

        # Preencher a tabela com dados de exemplo
        self.preencher_tabela(dados_exemplo)

        # Configurando o layout principal
        widget_central = QWidget()
        widget_central.setLayout(layout)
        self.setCentralWidget(widget_central)

    def preencher_tabela(self, dados):
        self.tabela.setRowCount(len(dados))

        for linha, item in enumerate(dados):
            for coluna, valor in enumerate(item.values()):
                self.tabela.setItem(linha, coluna, QTableWidgetItem(str(valor)))

            # Botões
            btn_editar = QPushButton("Editar", self)
            btn_editar.clicked.connect(lambda _, row=linha: self.editar_item(row, item['id']))

            btn_excluir = QPushButton("Excluir", self)
            btn_excluir.clicked.connect(lambda _, item_id=item['id']: self.excluir_item(item_id))

            layout_botoes = QVBoxLayout()
            layout_botoes.addWidget(btn_editar)
            layout_botoes.addWidget(btn_excluir)

            widget_botoes = QWidget()
            widget_botoes.setLayout(layout_botoes)

            self.tabela.setCellWidget(linha, len(item), widget_botoes)

    def editar_item(self, linha, item_id):
        print(f"Editar item ID {item_id} na linha {linha}")

    def excluir_item(self, item_id):
        print(f"Excluir item ID {item_id}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MinhaAplicacao()
    janela.show()
    sys.exit(app.exec_())
