from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, \
    QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QHeaderView, QSpinBox, QSpacerItem, QSizePolicy

from controllers import get_itens

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Tabela e Botões')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QHBoxLayout(central_widget)

        # Tabela
        self.table = QTableWidget(self)
        self.table.setColumnCount(6)  # Adicionei duas colunas para "Editar" e "Excluir"
        self.table.setHorizontalHeaderLabels(['Id','Nome', 'Quantidade', 'Categoria', ' ', ''])
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        layout.addWidget(self.table)

        # Botões ao lado da tabela
        buttons_container = QWidget(self)
        buttons_layout = QVBoxLayout(buttons_container)

        # Botão Adicionar
        btn_adicionar = QPushButton('Adicionar', self)
        btn_adicionar.clicked.connect(self.adicionar_item)
        buttons_layout.addWidget(btn_adicionar)

        # Botão Relatório Diário
        btn_diario = QPushButton('Relatório Diário', self)
        btn_diario.clicked.connect(self.gerar_relatorio_diario)
        buttons_layout.addWidget(btn_diario)

        # Botão Relatório Mensal
        btn_mensal = QPushButton('Relatório Mensal', self)
        btn_mensal.clicked.connect(self.gerar_relatorio_mensal)
        buttons_layout.addWidget(btn_mensal)

        buttons_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        
        layout.addWidget(buttons_container)

        self.carregar_dados_tabela()  # Carregar dados iniciais para a tabela

    def carregar_dados_tabela(self):
        # Substitua esta função pela lógica real para obter dados do seu banco de dados
        dados = get_itens()
        print(dados)

        self.table.setRowCount(len(dados))
        for row, item in enumerate(dados):
            for col, value in enumerate(item):
                if col == 0: 
                    self.table.setItem(row, col, QTableWidgetItem(str(value)))
                elif col == 2:  # Para a coluna de quantidade, use QSpinBox
                    spin_box = QSpinBox()
                    spin_box.setValue(value)
                    self.table.setCellWidget(row, col, spin_box)
                else:
                    self.table.setItem(row, col, QTableWidgetItem(str(value)))

            # Adicionar botões de Editar e Excluir
            btn_editar = QPushButton('Editar', self)
            btn_editar.clicked.connect(lambda _, r=row: self.editar_item(r))
            self.table.setCellWidget(row, 4, btn_editar)

            btn_excluir = QPushButton('Excluir', self)
            btn_excluir.clicked.connect(lambda _, r=row: self.excluir_item(r))
            self.table.setCellWidget(row, 5, btn_excluir)

    def adicionar_item(self):
        # Adicione aqui a lógica para adicionar um item à tabela e ao banco de dados
        print('Adicionar Item')

    def editar_item(self, row):
        # Adicione aqui a lógica para editar um item na tabela e no banco de dados
        print(f'Editar item na linha {row}')

    def excluir_item(self, row):
        # Adicione aqui a lógica para excluir um item da tabela e do banco de dados
        print(f'Excluir item na linha {row}')

    def gerar_relatorio_diario(self):
        # Adicione aqui a lógica para gerar o relatório diário
        print('Gerar Relatório Diário')

    def gerar_relatorio_mensal(self):
        # Adicione aqui a lógica para gerar o relatório mensal
        print('Gerar Relatório Mensal')


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
