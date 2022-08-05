# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pag_principal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(585, 437)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Paginas = QStackedWidget(self.frame)
        self.Paginas.setObjectName(u"Paginas")
        sizePolicy.setHeightForWidth(self.Paginas.sizePolicy().hasHeightForWidth())
        self.Paginas.setSizePolicy(sizePolicy)
        self.pag_Estoque = QWidget()
        self.pag_Estoque.setObjectName(u"pag_Estoque")
        sizePolicy.setHeightForWidth(self.pag_Estoque.sizePolicy().hasHeightForWidth())
        self.pag_Estoque.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.pag_Estoque)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_3 = QFrame(self.pag_Estoque)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Courier New")
        font.setPointSize(14)
        self.label.setFont(font)

        self.verticalLayout_4.addWidget(self.label)

        self.tab_estoque = QTableWidget(self.frame_3)
        if (self.tab_estoque.columnCount() < 5):
            self.tab_estoque.setColumnCount(5)
        font1 = QFont()
        font1.setFamily(u"Courier New")
        font1.setPointSize(7)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tab_estoque.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font2 = QFont()
        font2.setFamily(u"Courier")
        font2.setPointSize(6)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.tab_estoque.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tab_estoque.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.tab_estoque.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.tab_estoque.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tab_estoque.setObjectName(u"tab_estoque")

        self.verticalLayout_4.addWidget(self.tab_estoque)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.Paginas.addWidget(self.pag_Estoque)
        self.pag_addAlim = QWidget()
        self.pag_addAlim.setObjectName(u"pag_addAlim")
        sizePolicy.setHeightForWidth(self.pag_addAlim.sizePolicy().hasHeightForWidth())
        self.pag_addAlim.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.pag_addAlim)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_4 = QFrame(self.pag_addAlim)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setFamily(u"Courier New")
        font3.setPointSize(15)
        self.label_2.setFont(font3)

        self.verticalLayout_8.addWidget(self.label_2)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        font4 = QFont()
        font4.setFamily(u"Courier New")
        self.label_3.setFont(font4)

        self.verticalLayout_7.addWidget(self.label_3)

        self.ent_codAlim = QLineEdit(self.frame_6)
        self.ent_codAlim.setObjectName(u"ent_codAlim")

        self.verticalLayout_7.addWidget(self.ent_codAlim)

        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font4)

        self.verticalLayout_7.addWidget(self.label_4)

        self.ent_nomeAlim = QLineEdit(self.frame_6)
        self.ent_nomeAlim.setObjectName(u"ent_nomeAlim")

        self.verticalLayout_7.addWidget(self.ent_nomeAlim)

        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)

        self.verticalLayout_7.addWidget(self.label_5)

        self.ent_qAtual = QLineEdit(self.frame_6)
        self.ent_qAtual.setObjectName(u"ent_qAtual")

        self.verticalLayout_7.addWidget(self.ent_qAtual)

        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)

        self.verticalLayout_7.addWidget(self.label_6)

        self.ent_qMin = QLineEdit(self.frame_6)
        self.ent_qMin.setObjectName(u"ent_qMin")

        self.verticalLayout_7.addWidget(self.ent_qMin)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font4)

        self.verticalLayout_7.addWidget(self.label_7)

        self.ent_qMax = QLineEdit(self.frame_6)
        self.ent_qMax.setObjectName(u"ent_qMax")

        self.verticalLayout_7.addWidget(self.ent_qMax)

        self.btn_adicionaAlim = QPushButton(self.frame_6)
        self.btn_adicionaAlim.setObjectName(u"btn_adicionaAlim")
        font5 = QFont()
        font5.setFamily(u"Courier New")
        font5.setBold(True)
        font5.setWeight(75)
        self.btn_adicionaAlim.setFont(font5)

        self.verticalLayout_7.addWidget(self.btn_adicionaAlim)


        self.verticalLayout_8.addWidget(self.frame_6)


        self.verticalLayout_6.addWidget(self.frame_5)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.Paginas.addWidget(self.pag_addAlim)
        self.pag_contabilizando = QWidget()
        self.pag_contabilizando.setObjectName(u"pag_contabilizando")
        sizePolicy.setHeightForWidth(self.pag_contabilizando.sizePolicy().hasHeightForWidth())
        self.pag_contabilizando.setSizePolicy(sizePolicy)
        self.verticalLayout_9 = QVBoxLayout(self.pag_contabilizando)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_7 = QFrame(self.pag_contabilizando)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_7)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_8 = QFrame(self.frame_9)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")
        font6 = QFont()
        font6.setFamily(u"Courier New")
        font6.setPointSize(13)
        self.label_8.setFont(font6)

        self.verticalLayout_13.addWidget(self.label_8)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_9 = QLabel(self.frame_10)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)

        self.verticalLayout_10.addWidget(self.label_9)

        self.ent_prato = QLineEdit(self.frame_10)
        self.ent_prato.setObjectName(u"ent_prato")

        self.verticalLayout_10.addWidget(self.ent_prato)

        self.label_10 = QLabel(self.frame_10)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font4)

        self.verticalLayout_10.addWidget(self.label_10)

        self.ent_qPratos = QLineEdit(self.frame_10)
        self.ent_qPratos.setObjectName(u"ent_qPratos")

        self.verticalLayout_10.addWidget(self.ent_qPratos)

        self.btn_contabilizar = QPushButton(self.frame_10)
        self.btn_contabilizar.setObjectName(u"btn_contabilizar")
        self.btn_contabilizar.setFont(font5)

        self.verticalLayout_10.addWidget(self.btn_contabilizar)


        self.verticalLayout_13.addWidget(self.frame_10)


        self.verticalLayout_12.addWidget(self.frame_8)


        self.verticalLayout_11.addWidget(self.frame_9)


        self.verticalLayout_9.addWidget(self.frame_7)

        self.Paginas.addWidget(self.pag_contabilizando)
        self.pag_excluirAlim = QWidget()
        self.pag_excluirAlim.setObjectName(u"pag_excluirAlim")
        sizePolicy.setHeightForWidth(self.pag_excluirAlim.sizePolicy().hasHeightForWidth())
        self.pag_excluirAlim.setSizePolicy(sizePolicy)
        self.verticalLayout_14 = QVBoxLayout(self.pag_excluirAlim)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_11 = QFrame(self.pag_excluirAlim)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_11)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_12)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_11 = QLabel(self.frame_12)
        self.label_11.setObjectName(u"label_11")
        font7 = QFont()
        font7.setFamily(u"Courier New")
        font7.setPointSize(12)
        self.label_11.setFont(font7)

        self.verticalLayout_16.addWidget(self.label_11)


        self.verticalLayout_15.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_13)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_12 = QLabel(self.frame_13)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font4)

        self.verticalLayout_17.addWidget(self.label_12)

        self.exc_codAlim = QLineEdit(self.frame_13)
        self.exc_codAlim.setObjectName(u"exc_codAlim")

        self.verticalLayout_17.addWidget(self.exc_codAlim)

        self.label_13 = QLabel(self.frame_13)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font4)

        self.verticalLayout_17.addWidget(self.label_13)

        self.exc_nomeAlim = QLineEdit(self.frame_13)
        self.exc_nomeAlim.setObjectName(u"exc_nomeAlim")

        self.verticalLayout_17.addWidget(self.exc_nomeAlim)

        self.btn_excluir = QPushButton(self.frame_13)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setFont(font5)

        self.verticalLayout_17.addWidget(self.btn_excluir)


        self.verticalLayout_15.addWidget(self.frame_13)


        self.verticalLayout_14.addWidget(self.frame_11)

        self.Paginas.addWidget(self.pag_excluirAlim)

        self.verticalLayout.addWidget(self.Paginas)

        self.Botoes = QFrame(self.frame)
        self.Botoes.setObjectName(u"Botoes")
        sizePolicy.setHeightForWidth(self.Botoes.sizePolicy().hasHeightForWidth())
        self.Botoes.setSizePolicy(sizePolicy)
        self.Botoes.setFrameShape(QFrame.StyledPanel)
        self.Botoes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Botoes)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_addAlim = QPushButton(self.Botoes)
        self.btn_addAlim.setObjectName(u"btn_addAlim")
        self.btn_addAlim.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.pag_addAlim))
        font8 = QFont()
        font8.setFamily(u"Courier New")
        font8.setPointSize(6)
        font8.setBold(True)
        font8.setWeight(75)
        self.btn_addAlim.setFont(font8)

        self.horizontalLayout.addWidget(self.btn_addAlim)

        self.btn_ExcluirAlim = QPushButton(self.Botoes)
        self.btn_ExcluirAlim.setObjectName(u"btn_ExcluirAlim")
        self.btn_ExcluirAlim.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.pag_excluirAlim))
        font9 = QFont()
        font9.setFamily(u"Courier New")
        font9.setPointSize(6)
        font9.setBold(True)
        font9.setItalic(False)
        font9.setWeight(75)
        self.btn_ExcluirAlim.setFont(font9)

        self.horizontalLayout.addWidget(self.btn_ExcluirAlim)

        self.btn_contGastos = QPushButton(self.Botoes)
        self.btn_contGastos.setObjectName(u"btn_contGastos")
        self.btn_contGastos.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.pag_contabilizando))
        self.btn_contGastos.setFont(font8)

        self.horizontalLayout.addWidget(self.btn_contGastos)

        self.btn_visualizar = QPushButton(self.Botoes)
        self.btn_visualizar.setObjectName(u"btn_visualizar")
        self.btn_visualizar.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.pag_Estoque))
        self.btn_visualizar.setFont(font8)

        self.horizontalLayout.addWidget(self.btn_visualizar)


        self.verticalLayout.addWidget(self.Botoes)


        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Paginas.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Estoque Mais para mais que para menos", None))
        ___qtablewidgetitem = self.tab_estoque.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Cod Alimento", None));
        ___qtablewidgetitem1 = self.tab_estoque.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem2 = self.tab_estoque.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Quant. Atual", None));
        ___qtablewidgetitem3 = self.tab_estoque.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Quant. M\u00ednimo", None));
        ___qtablewidgetitem4 = self.tab_estoque.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Quant. M\u00e1xima", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Adicione o novo alimento", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo do alimento", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nome do alimento", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Quantidade Atual no Estoque", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Quantidade M\u00ednima", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Quantidade M\u00e1xima", None))
        self.btn_adicionaAlim.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Contabilizando gastos no Estoque", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Prato vendido", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Quantidade de pratos", None))
        self.btn_contabilizar.setText(QCoreApplication.translate("MainWindow", u"Contabilizar", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Excluir alimento do Estoque", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo do alimento", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_addAlim.setText(QCoreApplication.translate("MainWindow", u"Adicionar novo alimento", None))
        self.btn_ExcluirAlim.setText(QCoreApplication.translate("MainWindow", u"Excluir alimento", None))
        self.btn_contGastos.setText(QCoreApplication.translate("MainWindow", u"Contabilizar os gastos", None))
        self.btn_visualizar.setText(QCoreApplication.translate("MainWindow", u"Visualizar Estoque", None))
    # retranslateUi

