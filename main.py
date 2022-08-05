from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton)
from ui_pag_principal import Ui_MainWindow
import sys

class AbrirEstoque(QWidget, Ui_MainWindow):
    def __init__(self):
        super(AbrirEstoque, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Estoque mais para mais que para menos")
    
class açõesSistema():
    def ExcluirAlim(self):
        print("Cheguei")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    openEst = Ui_MainWindow()
    janela = QMainWindow()
    openEst.setupUi(janela)
    janela.show()
    sys.exit(app.exec_())