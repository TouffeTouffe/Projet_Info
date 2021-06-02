from solver import Solver


class Backtrack(Solver):

    def __init__(self,g):
        super().__init__(g)

    def test_complet(self):
        n = self.grille.x * self.grille.y
        for i in range(n):
            for j in range(n):
                if self.grille[i][j].sol == 0:
                    return False
        return True

    def num_valide(self, num, x, y):
        for i in self.grille.colonne(y):
            if i.sol == num:
                return False
        for i in self.grille.ligne(x):
            if i.sol == num:
                return False
        for i in self.grille.bloc(self.grille.getBlocIndice(x, y)):
            if i.sol == num:
                return False
        return True

    def vide(self):
        n = self.grille.x * self.grille.y
        for i in range(n):
            for j in range(n):
                if self.grille[i][j].sol == 0:
                    return i, j
        return None

    def solve(self):
        case = self.vide()
        if not case:
            return True
        i, j = case
        n = self.grille.x * self.grille.y
        for num in range(1, n + 1):
            if self.num_valide(num, i, j):
                self.grille[i][j].set(num)
                if self.solve():  # plus de cases vides
                    return True
                self.grille[i][j].set(0)  # ça pas marche
        return False

# https://www.techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/
