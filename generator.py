import random
from main import grille,case
from solv_func import SolvFunc



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






        nbtrous=0
        Ltrous=[]
        sauvegarde=0
        c=0
        d=0

        Lindices=range(n)
        print("n",n)
        if self.level==1:
            nbtrous=int((n**1.5))
            print("nb",nbtrous)
        cpt=0
        flag=True
        while cpt<nbtrous:
            c, d = random.choice(Lindices), random.choice(Lindices)
            while [c,d] in Ltrous:
                c,d=random.choice(Lindices),random.choice(Lindices)
            print(c,d)
            sauvegarde=gbase[c][d]
            gbase[c][d]=0
            try:
                Gbase=grille()
                solution=SolvFunc(Gbase.importGrille(gbase, XX, YY))
            except ValueError:
                flag=False
                gbase[c][d]=sauvegarde
                pass
            for i in range(10):
                Gbase = grille()
                solution=SolvFunc(Gbase.importGrille(gbase, XX, YY))
                Gbase = grille()
                """if SolvFunc(Gbase.importGrille(gbase, XX, YY))==solution:
                    flag=flag and True
                else:
                    flag=flag and False"""

            print(flag)
            if flag==True:
                cpt+=1
            else:
                flag=True
            print(flag)

            print(cpt)
        print(gbase)
        Gfin=grille()
        Gfin.importGrille(gbase, XX, YY)
        Gfin=grille()
        Gfin.importGrille(gbase, XX, YY)
        print(Gfin)



gene=Generator(3,2)
gene.generate()



