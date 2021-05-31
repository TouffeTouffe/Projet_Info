import random
from main import grille
from solv_func import SolvFunc


class Generator:

    def __init__(self, X, Y, level=1):
        self.x = X
        self.y = Y
        self.level = level

    def generate(self):

        lvl = self.level
        XX = self.x
        YY = self.y
        n = XX * YY
        l = []
        Grille = []
        llignes = []
        lcolonnes = []
        colonnek = []
        ligne = []
        chiffe = 0
        nbtry = 0

        Gbase = grille()
        gbase = []

        """gbase = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [4, 5, 6, 7, 8, 9, 1, 2, 3], [7, 8, 9, 1, 2, 3, 4, 5, 6], 
                    [2, 3, 4, 5, 6, 7, 8, 9, 1], [3, 4, 5, 6, 7, 8, 9, 1, 2], [5, 6, 7, 8, 9, 1, 2, 3, 4], 
                    [6, 7, 8, 9, 1, 2, 3, 4, 5], [8, 9, 1, 2, 3, 4, 5, 6, 7], [9, 1, 2, 3, 4, 5, 6, 7, 8]]
        """

        for i in range(n):
            l.append(i + 1)

        depart = random.choice(l)
        for i in range(n):
            lignebase = []
            for j in range(n):
                if (depart + j + i % YY * XX + i // YY) % n == 0:
                    lignebase.append(n)
                else:
                    lignebase.append((depart + j + i % YY * XX + i // YY) % n)
            gbase.append(lignebase)

        lN = range(n)
        lXX = range(XX)
        lYY = range(YY)

        for i in range(n):
            lcolonnes.append([])
        for i in range(10):
            a, b = random.choice(lN), random.choice(lYY)

            gbase[a], gbase[a // YY * YY + b] = gbase[a // YY * YY + b], gbase[a]

        for i in range(1):
            a, b = random.choice(lN), random.choice(lXX)
            for j in range(n):
                gbase[j][a], gbase[j][a // XX * XX + b] = gbase[j][a // XX * XX + b], gbase[j][a]

        nbtrous = 0
        Ltrous = []
        sauvegarde = 0
        c = 0
        d = 0
        e = 0
        f = 0

        Lindices = range(n)

        if self.level == 1:
            nbtrous = int((n ** 1.5))

        cpt = 0
        flag = True
        while cpt < nbtrous:
            c, d = random.choice(Lindices), random.choice(Lindices)
            e, f = 0, 0
            while [c, d] in Ltrous:
                c, d = random.choice(Lindices), random.choice(Lindices)

            sauvegarde = gbase[c][d]
            gbase[c][d] = 0
            try:
                Gbase = grille()
                solution = SolvFunc(Gbase.importGrille(gbase, XX, YY))
            except ValueError:
                flag = False
                gbase[c][d] = sauvegarde
                pass
            """for i in range(10):
                Gbase = grille()
                SolvFunc(Gbase.importGrille(gbase, XX, YY))
                Gsolution=Gbase.copy()
                if SolvFunc(Gbase.importGrille(gbase, XX, YY))==solution:
                    flag=flag and True
                else:
                    flag=flag and False"""

            if flag == True:
                cpt += 1
            else:
                flag = True

        Gfin = grille()
        Gfin.importGrille(gbase, XX, YY)
        Gfin = grille()
        Gfin.importGrille(gbase, XX, YY)

        return Gfin


gene = Generator(3, 3)
gene.generate()
