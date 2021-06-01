from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Solver(object):
    def setupUi(self, Solver, x, y):
        Solver.setObjectName("Solver")
        Solver.resize(296, 344)
        self.verticalLayout = QtWidgets.QVBoxLayout(Solver)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Solver)
        self.label.setStyleSheet("QTableWidget::item { \n"
                                 "border-left: 2px solid white; \n"
                                 "border-top: 2px solid white; \n"
                                 "} \n"
                                 "QTableWidget{ \n"
                                 "border-bottom: 2px solid white; \n"
                                 "border-right: 2px solid white; \n"
                                 "}")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(Solver)
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.AnyKeyPressed | QtWidgets.QAbstractItemView.DoubleClicked | QtWidgets.QAbstractItemView.EditKeyPressed | QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(x * y)
        self.tableWidget.setColumnCount(x * y)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(30)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(23)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.annuler_btn = QtWidgets.QPushButton(Solver)
        self.annuler_btn.setObjectName("annuler_btn")
        self.horizontalLayout.addWidget(self.annuler_btn)
        self.resoudre_btn = QtWidgets.QPushButton(Solver)
        self.resoudre_btn.setDefault(True)
        self.resoudre_btn.setObjectName("solve_btn")
        self.horizontalLayout.addWidget(self.resoudre_btn)
        self.reset_btn = QtWidgets.QPushButton(Solver)
        self.reset_btn.setObjectName("reset_btn")
        self.horizontalLayout.addWidget(self.reset_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Solver)
        QtCore.QMetaObject.connectSlotsByName(Solver)

    def retranslateUi(self, Solver):
        _translate = QtCore.QCoreApplication.translate
        Solver.setWindowTitle(_translate("Solver", "Sudoku 9000 Solver"))
        self.label.setText(
            _translate("Solver", "Entrez la grille puis cliquez sur \'Résoudre\' pour afficher la solution."))
        self.annuler_btn.setText(_translate("Solver", "Annuler"))
        self.resoudre_btn.setText(_translate("Resoudre", "Résoudre"))
        self.reset_btn.setText(_translate("Solver", "Reset"))
