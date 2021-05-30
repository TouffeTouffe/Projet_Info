from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Play(object):
    def setupUi(self, Jeu, x, y):
        Jeu.setObjectName("Jeu")
        Jeu.resize(314, 343)
        self.verticalLayout = QtWidgets.QVBoxLayout(Jeu)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.blocs=[]
        #print("x=", x, " y=", y)
        for i in range(x * y):
            self.blocs.append(QtWidgets.QTableWidget(Jeu))
            self.blocs[i].setRowCount(y)
            self.blocs[i].setColumnCount(x)
            self.blocs[i].setObjectName("bloc" + "i")
            self.blocs[i].horizontalHeader().setVisible(False)
            self.blocs[i].horizontalHeader().setDefaultSectionSize(30)
            self.blocs[i].horizontalHeader().setMinimumSectionSize(23)
            self.blocs[i].verticalHeader().setVisible(False)
            self.gridLayout_2.addWidget(self.blocs[i], i // y, i % y, 1, 1)
            #print(i//(y),i%y)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel_btn = QtWidgets.QPushButton(Jeu)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.check_btn = QtWidgets.QPushButton(Jeu)
        self.check_btn.setObjectName("check_btn")
        self.horizontalLayout.addWidget(self.check_btn)
        self.new_btn = QtWidgets.QPushButton(Jeu)
        self.new_btn.setObjectName("new_btn")
        self.horizontalLayout.addWidget(self.new_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Jeu)
        QtCore.QMetaObject.connectSlotsByName(Jeu)

    def retranslateUi(self, Jeu):
        _translate = QtCore.QCoreApplication.translate
        Jeu.setWindowTitle(_translate("Jeu", "Sudoku 9000"))
        self.cancel_btn.setText(_translate("Jeu", "Annuler"))
        self.check_btn.setText(_translate("Jeu", "Vérififer"))
        self.new_btn.setText(_translate("Jeu", "Nouvelle grille"))
