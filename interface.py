import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from sudoku_menu2 import Ui_Menu
from sudoku_jeu import Ui_Play
from sudoku_solver import Ui_Solver
import main
from solv_func import SolvFunc
from backtrack import Backtrack
import generator
import copy


class Menu(QDialog, Ui_Menu):
    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)
        self.setupUi(self)
        self.play_btn.clicked.connect(self.openPlay)
        self.resoudre_btn.clicked.connect(self.openSolver)
        self.setWindowIcon(QtGui.QIcon('icone.jpg'))

    def openPlay(self):
        global x
        global y
        x = int(self.lineEdit_2.text())
        y = int(self.lineEdit.text())
        self.play = Jeu(self)
        self.play.show()

    def openSolver(self):
        global x
        global y
        x = int(self.lineEdit_2.text())
        y = int(self.lineEdit.text())
        self.solver = Solver(self)
        self.solver.show()


class Jeu(QDialog, Ui_Play):
    def __init__(self, parent=None):
        super(Jeu, self).__init__(parent)
        self.setupUi(self, x, y)
        self.lignes = []
        self.bloc = []
        for i in range(x):
            ligne = []
            for j in range(y):
                ligne.append(self.blocs[y * i + j])
                self.blocs[y * i + j].cellChanged.connect(self.modif)
            self.bloc.append(ligne)
            # print(ligne)
        self.nouvClick()
        self.annuler_btn.clicked.connect(self.close)
        self.nouv_btn.clicked.connect(self.nouvClick)
        self.verif_btn.clicked.connect(self.verif)

    def nouvClick(self):
        global grille
        global grille_origine
        gen = generator.Generator(x, y)
        grille = gen.generate()
        grille_origine = copy.deepcopy(grille)
        for l, ligne_bloc in enumerate(self.bloc):
            for b, blocs_cases in enumerate(ligne_bloc):
                for i in range(y):
                    for j in range(x):
                        val = grille.bloc(l * y + b)[x * i + j].sol
                        if val != 0:  # si un chiffre est présent dans la grille générée
                            item = QTableWidgetItem(str(val))
                            item.setFlags(Qt.ItemIsSelectable or Qt.ItemIsEnabled)  # grille d'origine non modifiable
                        else:
                            item = QTableWidgetItem("")
                        blocs_cases.setItem(i, j, item)
                blocs_cases.clearSelection()

    def modif(self):
        # print("modif!")
        for i in range(x):  # on cherche le bloc modifié
            for j in range(y):
                try:
                    val = self.bloc[i][j].currentItem().text()
                    if val:  # fausse alerte (arrive parfois lorsque que l'on clique sur une autre cellule après avoir entré un nombre)
                        cur = self.bloc[i][j].currentColumn()
                        cur2 = self.bloc[i][j].currentRow()
                        # print(i*y+j,cur,cur2,val)
                        grille.bloc(i * y + j)[cur2 * x + cur].set(int(val))  # mise à jour de la grille
                        # print(grille)
                except AttributeError:  # sert lors de l'intialisation de l'ihm
                    pass

    def verif(self):
        # solver = Backtrack(grille_copy)
        # solver.resoudre()
        solver = SolvFunc(grille_origine)
        print(grille_origine)
        solver.solve()
        print(grille)
        print(grille_origine)
        if grille_origine.compare(grille):  # la grille que l'on a rentrée correspond à celle résolue par l'IA
            msg = QMessageBox()
            msg.setWindowTitle("Vérification")
            msg.setText("Sudoku réussi, félicitations!")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Vérification")
            msg.setText("Sudoku non conforme, dommage")
            msg.exec_()


class Solver(QDialog, Ui_Solver):
    def __init__(self, parent=None):
        super(Solver, self).__init__(parent)
        self.setupUi(self, x, y)
        self.resoudre_btn.clicked.connect(self.solveClick)
        self.reset_btn.clicked.connect(self.tableWidget.clear)
        self.annuler_btn.clicked.connect(self.close)

    def solveClick(self):
        grille_ihm = []  # on rentre tous les nombres dans une liste
        for i in range(x * y):
            row = []
            for j in range(x * y):
                item = self.tableWidget.item(i, j)
                if item is None:
                    item = 0
                else:
                    item = item.text()
                if item not in [str(i) for i in range(0, x * y + 1)]:
                    item = 0
                row.append(int(item))
            grille_ihm.append(row[:])
        grille_backend = main.grille()
        grille_backend.importGrille(grille_ihm, x, y)  # on crée la grille correspondante pour pouvoir la résoudre
        solver = SolvFunc(grille_backend)
        solver.solve()
        self.showSolution(grille_backend)

    def showSolution(self, g):
        for i in range(x * y):
            for j in range(x * y):
                item = QTableWidgetItem(str(g[i][j].sol))
                self.tableWidget.setItem(i, j, item)


if __name__ == '__main__':
    order66 = QApplication(sys.argv)
    form = Menu()
    form.show()
    sys.exit(order66.exec_())
