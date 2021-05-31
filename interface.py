import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from PyQt5.QtCore import Qt
from sudoku_menu2 import Ui_Menu
from sudoku_jeu import Ui_Play
from sudoku_solver import Ui_Solver
import main
from solv_func import SolvFunc
import generator


class Menu(QDialog, Ui_Menu):
    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)
        self.setupUi(self)
        self.play_btn.clicked.connect(self.openPlay)
        #self.resoudre_btn.clicked.connect(self.openSolver)

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

    def nouvClick(self):
        global grille
        gen=generator.Generator(x, y)
        grille = gen.generate()
        for l, ligne_bloc in enumerate(self.bloc):
            for b, blocs_cases in enumerate(ligne_bloc):
                for i in range(y):
                    for j in range(x):
                        val = grille.bloc(l*y+b)[x*i+j].sol
                        if val != 0:  # si un chiffre est présent dans la grille générée
                            item = QTableWidgetItem(str(val))
                            item.setFlags(Qt.ItemIsSelectable
                                          or Qt.ItemIsEnabled)
                        else:
                            item = QTableWidgetItem("")
                        blocs_cases.setItem(i, j, item)
                blocs_cases.clearSelection()

    def modif(self):
        # print("modif!")
        for i in range(x):
            for j in range(y):
                try:
                    val = self.bloc[i][j].currentItem().text()
                    if val:
                        cur = self.bloc[i][j].currentColumn()
                        cur2 = self.bloc[i][j].currentRow()
                        #print(i*y+j,cur,cur2,val)
                        grille.bloc(i*y+j)[cur2 * x + cur].set(int(val))
                        #print(grille)
                except AttributeError:  # sert lors de l'intialisation de l'ihm
                    pass


class Solver(QDialog, Ui_Solver):
    def __init__(self, parent=None):
        super(Solver, self).__init__(parent)
        self.setupUi(self, x, y)
        self.solve_btn.clicked.connect(self.solveClick)
        self.reset_btn.clicked.connect(self.tableWidget.clear)
        self.annuler_btn.clicked.connect(self.close)

    def solveClick(self):
        grille_ihm = []
        for i in range(x * y):
            row = []
            for j in range(x * y):
                item = self.tableWidget.item(i, j)
                if item is None:
                    item = 0
                else:
                    item = item.text()
                if int(item) not in range(0, x * y + 1):
                    item = 0
                row.append(int(item))
            grille_ihm.append(row[:])
        grille_backend = main.grille()
        grille_backend.importGrille(grille_ihm, x, y)
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
