import unittest
from backtrack import Backtrack
from solv_func import SolvFunc
import main


class TestGrille(unittest.TestCase):

    def testPos(self):
        G = [[1, 0, 3, 0], [3, 0, 1, 2], [4, 0, 2, 3], [2, 0, 4, 1]]
        g = main.grille()
        g.importGrille(G, 2, 2)
        self.assertEqual(g[0][1].possibilites, [1, 2, 3, 4])
        self.assertEqual(g[0][0].possibilites, [])
        self.assertEqual(g[0][3].bloc_ap, 1)
        self.assertEqual(g[3][2].colonne_ap, 2)
        self.assertEqual(g[1][2].ligne_ap, 1)

    def testSolvFonctions(self):
        G = [[1, 0, 3, 0], [3, 0, 1, 2], [4, 0, 2, 3], [2, 0, 4, 1]]
        T = [[1, 0, 3, 0], [3, 0, 1, 2], [4, 1, 2, 3], [2, 0, 4, 1]]
        g = main.grille()
        t = main.grille()
        g.importGrille(G, 2, 2)
        t.importGrille(T, 2, 2)
        solv = SolvFunc(g)
        solv.celib(g.ligne(0))
        solv.celib(g.ligne(2))
        solv.sol(g.ligne(2))
        self.assertEqual(g[0][1].possibilites,[2,4])
        self.assertTrue(g.compare(t))

    def testSolv(self):
        G = [[1, 0, 3, 0], [3, 0, 1, 2], [4, 0, 2, 3], [2, 0, 4, 1]]
        S = [[1, 2, 3, 4], [3, 4, 1, 2], [4, 1, 2, 3], [2, 3, 4, 1]]
        g1 = main.grille()
        g2 = main.grille()
        s = main.grille()
        g1.importGrille(G, 2, 2)
        g2.importGrille(G, 2, 2)
        s.importGrille(S, 2, 2)
        solv1 = Backtrack(g1)
        solv2 = SolvFunc(g2)
        solv1.resoudre()
        solv2.solve()
        self.assertTrue(g1.compare(s))
        self.assertTrue(g2.compare(s))

    def testSelectGrille(self):
        G = [[1, 0, 3, 0], [3, 0, 1, 2], [4, 0, 2, 3], [2, 0, 4, 1]]
        g = main.grille()
        g.importGrille(G, 2, 2)
        self.assertEqual([i.sol for i in g.bloc(1)], [3, 0, 1, 2])
        self.assertEqual([i.sol for i in g.ligne(2)], [4, 0, 2, 3])
        self.assertEqual([i.sol for i in g.colonne(3)], [0, 2, 3, 1])


if __name__ == '__main__':
    unittest.main()
