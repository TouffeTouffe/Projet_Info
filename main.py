import numpy as np

class grille:
    def __init__(self):
        self.col = []

    def ajout_col(self):
        c=col()
        self.col.append(c)

    def import_grille(self,g,x,y):
        self.dimx=x #taille d'un bloc
        self.dimy=y
        for i in range(x*y):
            self.ajout_col()
        for c in self.col:
            for i in range(x*y):
                c.ajout_case()
        for i in range (x*y):
            for j in range(x*y):
                if g[i][j]!=0:
                    self.col[i].cases[j].sol=g[i][j]
                    self.col[i].cases[j].possibilites=[]

    def __str__(self):
        l=""
        for i in range(self.dimx):
            if i%self.dimy==0:
                l+="---------"
            l+="\n"
            l+="---------\n"
            for j in range(self.dimy):
                if j%self.dimx==0:
                    l += "|"
                l+="|"
                l+=str(self.blocs[self.dimx*j+self.dimy*i-1].cases[0].sol)
            l+="||"
        l+="---------"
        return l

class col:
    def __init__(self):
        self.cases=[]

    def ajout_case(self):
        c=case()
        self.cases.append(c)



class case:
    def __init__(self):
        self.sol=0
        self.possibilites=[1,2,3,4,5,6,7,8,9]

    def __int__(self):
        return self.sol

    def set(self,i):
        self.sol=i
        self.possibilites=[]

class grille2(list):
    def __init__(self):
        super().__init__()

    def importGrille(self,g,X,Y):
        self.x=X
        self.y=Y
        for i in range (X*Y):
            L=[]
            for j in range (X*Y):
                c=case()
                if g[i][j]!=0:
                    c.set(g[i][j])
                L.append(c)
            self.append(L)



g=grille2()
G=[[1,0,3,4],[1,2,3,0],[0,2,3,4],[0,2,3,4]]
g.importGrille(G,2,2)
