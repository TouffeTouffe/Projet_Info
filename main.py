class case:
    def __init__(self,n):
        self.sol = 0
        self.possibilites = list(range(1,n+1))

    def __repr__(self):
        return str(self.sol)  # pour afficher la solution dans le print grille

    def set(self, i):
        self.sol = i
        self.possibilites = []


# on utilise les listes par simplicité mais surtout grâce au fait que plusieurs listes peuvent pointer le même objet (ie, une case)
class grille2(list):
    def __init__(self):
        super().__init__()

    def importGrille(self, g, X, Y):
        self.x = X
        self.y = Y
        n=X*Y
        for i in range(n):
            L = []
            for j in range(n):
                c = case(n)
                if g[i][j] != 0:
                    c.set(g[i][j])
                    if g[i][j] > X * Y:
                        raise ValueError("Nombre trop gros")  # on ne peut pas faire rentrer un nombre >n dans un carré à n cases
                L.append(c)
            self.append(L)

    def ligne(self,i):
        return [self[i]]

    def colonne(self,j):
        return [col[j] for col in self]

    def bloc(self,k):
        B=[]
        for i in range(self.y):
            for j in range(self.x):
                B.append()
        return B

g = grille2()
G = [[1, 0, 3, 4], [1, 2, 3, 0], [0, 2, 3, 4], [0, 2, 3, 4]]
g.importGrille(G, 2, 2)
