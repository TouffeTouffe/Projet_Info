class SolvFunc:

    def __init__(self,grille):
        self.g=grille


    def sol(self,l):
        for cases in l:
            if len(cases.possibilites) == 1:
                cases.set(cases.possibilites[0])


    def remove_pos(self,l):
        val = []
        for i in l:
            val.append(i.sol)
        for i in l:
            for v in val:
                if v in i.possiblites:
                    i.possiblites.remove(v)


    def celib(self,l):  # https://www.sudoku129.com/grilles/tips_1.php
        pos_unique = []
        for i in l:
            for j in i.possiblites:
                if j not in pos_unique:
                    pos_unique.append(j)
                else:
                    pos_unique.remove(j)
        if pos_unique:
            for j in pos_unique:
                for i in l:
                    if j in i.possiblites:
                        i.set(j)
        self.remove_pos(l)


    def candidat_bloque(self,c):  # https://www.sudoku129.com/grilles/tips_2.php
        col, lig, blc = c.colonne_ap, c.ligne_ap, c.bloc_ap
        col_g = self.g.collone(col)
        lig_g = self.g.ligne(lig)
        for p in c.possibilites:
            flag = True
            C=[]
            for cases in col_g:
                if p in cases.possibilites and cases != c:
                    C.append(cases)  # les cases de la même colonne qui ont aussi cette possibilité
            b=[]
            for cases in C:
                if cases.bloc_ap not in B:
                    b.append(cases.bloc_ap)
            if len(b)==1:
                if b[0] != blc:
                    B=self.bloc(b[0])
                    cases_autorisees=[]
                    for case in B:
                        if p in case.possibilites:
                            cases_autorisees.append(case)
                    for case in cases_autorisees:
                        if case.colonne_ap != col_g:
                            flag=False
            if flag:
                c.possibilites.remove(p)
        for p in c.possibilites:
            flag = True
            C=[]
            for cases in lig_g:
                if p in cases.possibilites and cases != c:
                    C.append(cases)  # les cases de la même ligne qui ont aussi cette possibilité
            b=[]
            for cases in C:
                if cases.bloc_ap not in B:
                    b.append(cases.bloc_ap)
            if len(b)==1:
                if b[0] != blc:
                    B=self.bloc(b[0])
                    cases_autorisees=[]
                    for case in B:
                        if p in case.possibilites:
                            cases_autorisees.append(case)
                    for case in cases_autorisees:
                        if case.ligne_ap != col_g:
                            flag=False
            if flag:
                c.possibilites.remove(p)


