from PySide2.QtWidgets import (QApplication, QMainWindow)
from ui_pag_principal import Ui_MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    openEst = Ui_MainWindow()
    janela = QMainWindow()
    openEst.setupUi(janela)
    janela.show()
    sys.exit(app.exec_())