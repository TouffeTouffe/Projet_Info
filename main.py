class case:
    def __init__(self, n, l, c, k):
        self.sol = 0
        self.possibilites = list(range(1, n + 1))
        self.colonne_ap = c
        self.ligne_ap = l
        self.bloc_ap = k

    def __repr__(self):
        return str(self.sol)  # pour afficher la solution dans le print grille

    def set(self, i):
        self.sol = i
        self.possibilites = []


# on utilise les listes par simplicité mais surtout grâce au fait que plusieurs listes peuvent pointer le même objet (ie, une case)
class grille(list):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0

    def importGrille(self, g, X, Y):
        self.x = X
        self.y = Y
        n = X * Y
        for i in range(n):
            L = []
            for j in range(n):
                k = self.y * (i // self.y) + (j // self.x)
                c = case(n, i, j, k)
                if g[i][j] != 0:
                    c.set(g[i][j])
                    if g[i][j] > X * Y:
                        raise ValueError(
                            "Nombre trop gros")  # on ne peut pas faire rentrer un nombre >n dans un carré à n cases
                L.append(c)
            self.append(L)

    def ligne(self, i):
        return self[i]

    def colonne(self, j):
        return [col[j] for col in self]

    def getBlocIndice(self, i, j):
        return self[i][j].bloc_ap

    def bloc(self, k):
        B = []
        X = self.x
        Y = self.y
        n = X * Y
        for i in range(n):
            for j in range(n):
                if self.getBlocIndice(i, j) == k:
                    B.append(self[i][j])
        return B

    def compare(self,f):
        if type(f) != grille:
            raise TypeError("ce n'est pas une grille")
        X=self.x
        X1=f.x
        Y=self.y
        Y1=f.y
        if X != X1 or Y != Y1:
            return False
        n=X*Y
        for i in range(n):
            for j in range(n):
                if self[i][j].sol != f[i][j].sol:
                    return False
        return True


g = grille()
G = [[1, 0, 3, 0], [3, 0, 1, 2], [4, 0, 2, 3], [2, 0, 4, 1]]
g.importGrille(G, 2, 2)
from backtrack import backtrack
from solv_func import SolvFunc
solv=backtrack(g)
solv2=SolvFunc(g)
