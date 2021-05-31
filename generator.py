import random
from main import grille,case
import solv_func



class Generator:

    def __init__(self,X,Y,level=1):
        self.x=X
        self.y=Y
        self.level=level


    def generate(self):

        lvl=self.level
        XX=self.x
        YY=self.y
        n=XX*YY
        l=[]
        Grille=[]
        llignes=[]
        lcolonnes=[]
        colonnek=[]
        ligne=[]
        chiffe=0
        nbtry=0

        Gbase = grille()
        gbase=[]


        """gbase = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9, 1], [3, 4, 5, 6, 7, 8, 9, 1, 2],
                 [4, 5, 6, 7, 8, 9, 1, 2, 3], [5, 6, 7, 8, 9, 1, 2, 3, 4], [6, 7, 8, 9, 1, 2, 3, 4, 5],
                 [7, 8, 9, 1, 2, 3, 4, 5, 6], [8, 9, 1, 2, 3, 4, 5, 6, 7], [9, 1, 2, 3, 4, 5, 6, 7, 8]]
        """



        for i in range(n):
            l.append(i+1)

        depart = random.choice(l)
        for i in range(n):
            lignebase = []
            for j in range(n):
                if (depart + j + i) % n == 0:
                    lignebase.append(n)
                else:
                    lignebase.append((depart + j + i) % n)
            gbase.append(lignebase)


        print(gbase)


        for i in range(n):
            lcolonnes.append([])
        for i in range(10):
            a,b=random.choice(range(n)),random.choice(range(n))
            gbase[a],gbase[b]=gbase[b],gbase[a]
        for i in range(10):
            a, b = random.choice(range(n)), random.choice(range(n))
            for j in range(n):
                gbase[j][a], gbase[j][b]= gbase[j][b], gbase[j][a]

        print(gbase)




        print(Gbase)


        nbtrous=0
        Ltrous=[]
        sauvegarde=0
        i=0
        j=0
        l=[1,2,3,4,5,6,7,8,9]
        if self.level==1:
            nbtrous=30
        cpt=0
        flag=True
        while cpt<nbtrous:
            while [i,j] in Ltrous:
                i,j=random.choice(l),random.choice(l)
            sauvegarde=gbase[i][j]
            gbase[i][j]=0
            try:
                solution=solv_func.SolvFunc.solve(Gbase.importGrille(gbase, XX, YY))
            except ValueError:
                flag=False
                gbase[i][j]=sauvegarde
                pass
            for i in range(10):
                if solution!=solv_func.SolvFunc.solve(Gbase.importGrille(gbase, XX, YY)):
                    flag=False
            if flag==True:
                cpt+=1
            else:
                flag=True

        Gbase.importGrille(gbase, XX, YY)



gene=Generator(3,3)
gene.generate()



