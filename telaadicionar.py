from PySide6.QtCore import Qt, QCoreApplication, QRect
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QFrame, QPushButton,
                               QLineEdit, QComboBox, QSpinBox)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(340, 280)
        self.adicionar = QWidget(MainWindow)
        self.adicionar.setObjectName(u"adicionar")
        self.frame = QFrame(self.adicionar)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(130, 90, 391, 211))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.confirm = QPushButton(self.frame)
        self.confirm.setObjectName(u"confirm")
        self.confirm.setGeometry(QRect(280, 150, 91, 31))
        self.nome = QLineEdit(self.frame)
        self.nome.setObjectName(u"nome")
        self.nome.setGeometry(QRect(40, 50, 91, 21))
        self.nome.setAlignment(Qt.AlignCenter)
        self.selecionar = QComboBox(self.frame)
        self.selecionar.addItem("")
        self.selecionar.addItem("")
        self.selecionar.addItem("")
        self.selecionar.addItem("")
        self.selecionar.setObjectName(u"selecionar")
        self.selecionar.setGeometry(QRect(150, 50, 101, 21))
        self.quant = QSpinBox(self.frame)
        self.quant.setObjectName(u"quant")
        self.quant.setGeometry(QRect(270, 50, 61, 21))
        self.quant.setMaximum(9000)
        MainWindow.setCentralWidget(self.adicionar)

        self.retranslateUi(MainWindow)

        self.selecionar.setCurrentIndex(0)

        # Conectando os sinais aos slots
        self.confirm.clicked.connect(self.adicionar_clicked)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.confirm.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.nome.setText("")
        self.nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Produto", None))
        self.selecionar.setItemText(0, QCoreApplication.translate("MainWindow", u"Eletrodomestico", None))
        self.selecionar.setItemText(1, QCoreApplication.translate("MainWindow", u"m\u00f3vel", None))
        self.selecionar.setItemText(2, QCoreApplication.translate("MainWindow", u"decora\u00e7\u00e3o", None))
        self.selecionar.setItemText(3, QCoreApplication.translate("MainWindow", u"eletronico", None))

        self.selecionar.setCurrentText(QCoreApplication.translate("MainWindow", u"Eletrodomestico", None))

    # Slot para ação do botão "Adicionar"
    def adicionar_clicked(self):
        # Lógica para adicionar item
        pass

if __name__ == "__main__":
    app = QApplication([])
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec()

