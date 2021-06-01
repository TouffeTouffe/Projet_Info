import random
from main import grille,case
from solv_func import SolvFunc



class Generator:

    def __init__(self,X,Y,level=1):
        self.x = X
        self.y = Y
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


        """gorigine = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [4, 5, 6, 7, 8, 9, 1, 2, 3], [7, 8, 9, 1, 2, 3, 4, 5, 6], 
                    [2, 3, 4, 5, 6, 7, 8, 9, 1], [3, 4, 5, 6, 7, 8, 9, 1, 2], [5, 6, 7, 8, 9, 1, 2, 3, 4], 
                    [6, 7, 8, 9, 1, 2, 3, 4, 5], [8, 9, 1, 2, 3, 4, 5, 6, 7], [9, 1, 2, 3, 4, 5, 6, 7, 8]]
        """



        for i in range(n):
            l.append(i+1)

        depart = random.choice(l)     #prend au hasard un chiffre pour le placer en haut à gauche
        for i in range(n):
            lignebase = []
            for j in range(n):
                if (depart + j + i%YY*XX+i//YY) % n == 0:    # génère à partir du chiffre de départ une grille cconstruite de la même manière que gorigine en commentaire ligne 34
                    lignebase.append(n)                      # en travaillant modulo n on remplace les 0 par n pour générer la grille pleine
                else:
                    lignebase.append((depart + j + i%YY*XX+i//YY) % n)
            gbase.append(lignebase)



        lN=range(n)
        lXX=range(XX)
        lYY=range(YY)

        for i in range(n):
            lcolonnes.append([])
        for i in range(10):
            a,b=random.choice(lN),random.choice(lYY)           # on choisit "a" un numéro de ligne et "b" un indice compris entre 0 et le (nombre de ligne par zone)-1 exemple pour un 3*3 b appartient a [0,1,2]

            gbase[a],gbase[a//YY*YY+b]=gbase[a//YY*YY+b],gbase[a]    # on échange les lignes d'indice "a" avec la ligne dont l'indice à l'intérieur de la zone de "a" et "b"

        for i in range(1):
            a, b = random.choice(lN), random.choice(lXX)       # même opération avec les colonnes
            for j in range(n):
                gbase[j][a], gbase[j][a//XX*XX+b]= gbase[j][a//XX*XX+b], gbase[j][a]









        nbtrous=0
        Ltrous=[]
        sauvegarde=0
        c=0
        d=0
        e=0
        f=0

        Lindices=range(n)

        if self.level==1:
            nbtrous=int((n**1.5))     # on détermine un nombre de trous en fonction du niveau de difficulté souhaité
                                      # pour le niveau un on aura par exemple 4 trous pour 16 cases pour un 2*2 et 27 trous pour 81 cases pour un 3*3

        cpt=0
        flag=True
        while cpt<nbtrous:
            c, d = random.choice(Lindices), random.choice(Lindices)        # je choisis au hasard un couple de coordonnées pour mettre un trou

            while [c,d] in Ltrous:
                c,d=random.choice(Lindices),random.choice(Lindices)        # cette boucle s'assure que l'on ne troue pas la grille deux fois au même endroit


            sauvegarde=gbase[c][d]
            gbase[c][d]=0
            try:
                Gbase=grille()
                solution=SolvFunc(Gbase.importGrille(gbase, XX, YY))       # on vérifie à chaque fois si la grille est toujours soluble, sinon on remet le terme enlevé et on reprend un nouveau trou
            except ValueError:
                flag=False
                gbase[c][d]=sauvegarde
                pass
            """for i in range(10):                                          # cette partie en commentaire avait pour but de vérifier l'unicité de la solution, mais étant donné le fait que l'on
                Gbase = grille()                                            # teste les solutions toujours avec le même solveur, qui résoud toujours avec la même logique, il nous renvoie toujours une seule solution.
                SolvFunc(Gbase.importGrille(gbase, XX, YY))                 # mais comme notre solveur se base sur des techniques "à la main" utilisées par des êtres humains, lors de la résolution d'un sudoku on remplie 
                Gsolution=Gbase.copy()                                      # case si et seulement si on est certain qu'il ne reste qu'une unique possibilité, partant de ce principe le solveur devrait être incapable
                if SolvFunc(Gbase.importGrille(gbase, XX, YY))==solution:   # de résoudre le problème s'il y avait plusieur solution. Ce qui n'était pas du tout le cas avec le backtracking
                    flag=flag and True
                else:
                    flag=flag and False"""


            if flag==True:
                cpt+=1
            else:
                flag=True





        Gfin=grille()
        Gfin.importGrille(gbase, XX, YY)   # je génère la grille et la retourne

        return Gfin

gene=Generator(3,3)
gene.generate()
