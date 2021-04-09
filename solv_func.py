def sol(l):
    for cases in l:
        if len(cases.possibilites) == 1:
            cases.set(cases.possibilites[0])


def remove_pos(l):
    val = []
    for i in l:
        val.append(i.sol)
    for i in l:
        for v in val:
            if v in i.possiblites:
                i.possiblites.remove(v)


def celib(l):  # https://www.sudoku129.com/grilles/tips_1.php
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
    remove_pos(l)


def candidat_bloque(c):  # https://www.sudoku129.com/grilles/tips_2.php
    col, lig, blc = c.colonne, c.ligne, c.bloc
    for s in c.sol:
