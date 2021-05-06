class backtrack:

    def __init__(self, g):
        self.grille = g

    def test_complet(self):
        n = self.grille.x * self.grille.y
        for i in range(n):
            for j in range(n):
                if self.grille[i][j].sol == 0:
                    return False
        return True

    def num_valide(self, num, x, y):
        if num in self.grille.colonne(x) or num in self.grille.ligne(y) or num in self.grille.bloc(
                self.grille.getBlocIndice(x, y)):
            return False
        return True

    def vide(self):
        n = self.grille.x * self.grille.y
        for i in range(n):
            for j in range(n):
                if self.grille[i][j].sol == 0:
                    return i,j
        return None

    def resoudre(self):
            case=self.vide
            if not case:
                return True
            i,j=case
            n = self.grille.x * self.grille.y
            for num in range(1,n+1):
                if self.num_valide(num,i,j):
                    self.grille[i][j].set(num)

                if self.resoudre():
                    return True

                self.grille[i][j].set(0) #ça pas marche
            return False