import copy


class SolvFunc:

    def __init__(self, g):
        self.grille = g

    def sol(self, l):
        for cases in l:
            if len(cases.possibilites) == 1:
                cases.set(cases.possibilites[0])

    def remove_pos(self, l):
        val = []
        for i in l:
            val.append(i.sol)
        for cases in l:
            for v in val:
                if v in cases.possibilites:
                    cases.possibilites.remove(v)

    def celib(self, l):  # https://www.sudoku129.com/grilles/tips_1.php
        pos_unique = []
        pos_totales = []
        for i in l:
            for j in i.possibilites:
                if j not in pos_totales:
                    pos_unique.append(j)
                    pos_totales.append(j)
                else:
                    pos_unique.remove(j)
        if pos_unique:  # s'il y a des célibataires
            for j in pos_unique:
                for i in l:
                    if j in i.possibilites:
                        i.set(j)
        self.remove_pos(l)

    def candidat_bloque(self, c):  # https://www.sudoku129.com/grilles/tips_2.php
        col, lig, blc = c.colonne_ap, c.ligne_ap, c.bloc_ap
        col_g = self.grille.colonne(col)
        lig_g = self.grille.ligne(lig)
        for p in c.possibilites:
            flag = True
            C = []
            for cases in col_g:
                if p in cases.possibilites and cases != c:
                    C.append(cases)  # les cases de la même colonne qui ont aussi cette possibilité
            b = []
            for cases in C:
                if cases.bloc_ap not in b:
                    b.append(cases.bloc_ap)
            if len(b) == 1:
                if b[0] != blc:
                    B = self.grille.bloc(b[0])
                    cases_autorisees = []
                    for case in B:
                        if p in case.possibilites:
                            cases_autorisees.append(case)
                    for case in cases_autorisees:
                        if case.colonne_ap != col_g:
                            flag = False
            if flag:
                c.possibilites.remove(p)
        for p in c.possibilites:
            flag = True
            C = []
            for cases in lig_g:
                if p in cases.possibilites and cases != c:
                    C.append(cases)  # les cases de la même ligne qui ont aussi cette possibilité
            b = []
            for cases in C:
                if cases.bloc_ap not in b:
                    b.append(cases.bloc_ap)
            if len(b) == 1:
                if b[0] != blc:
                    B = self.grille.bloc(b[0])
                    cases_autorisees = []
                    for case in B:
                        if p in case.possibilites:
                            cases_autorisees.append(case)
                    for case in cases_autorisees:
                        if case.ligne_ap != col_g:
                            flag = False
            if flag:
                c.possibilites.remove(p)

    def solve(self):
        init = True
        n = self.grille.x * self.grille.y
        controle = copy.copy(self.grille)
        while self.grille != controle or init:  # jusqu'à ce que l'on bloque (trop compliqué ou grille finie)
            controle = copy.copy(self.grille)
            for i in range(n):
                self.remove_pos(self.grille.ligne(i))
                self.remove_pos(self.grille.colonne(i))
                self.remove_pos(self.grille.bloc(i))
            for i in range(n):
                self.sol(self.grille.colonne(i))
                self.sol(self.grille.ligne(i))
                self.sol(self.grille.bloc(i))
            for i in range(n):
                self.celib(self.grille.colonne(i))
                self.celib(self.grille.ligne(i))
                self.celib(self.grille.bloc(i))
            for lignes in self.grille:
                for cases in lignes:
                    if cases.sol == 0:
                        self.candidat_bloque(cases)
            init = False
