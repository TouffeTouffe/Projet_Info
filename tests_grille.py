import unittest
from backtrack import Backtrack
from solv_func import SolvFunc
import main


class TestGrille(unittest.TestCase):
    """auteur: Léopold Poquillon"""
    def testCase(self):
        G = [[1, 0, 3, 0], [3, 0, 1, 2], [4, 0, 2, 3], [2, 0, 4, 1]]
        g = main.grille()
        g.importGrille(G, 2, 2)
        self.assertEqual(g[0][1].possibilites, [1, 2, 3, 4])
        self.assertEqual(g[3][3].possibilites, [])
        self.assertEqual(g[0][1].bloc_ap, 0)
        self.assertEqual(g[3][3].bloc_ap, 3)
        self.assertEqual(g[0][1].colonne_ap, 1)
        self.assertEqual(g[3][3].ligne_ap, 3)

    def testSelectGrille(self):
        G = [[1, 0, 3, 0], [3, 0, 1, 2], [4, 0, 2, 3], [2, 0, 4, 1]]
        g = main.grille()
        g.importGrille(G, 2, 2)
        self.assertEqual([i.sol for i in g.bloc(1)], [3, 0, 1, 2])
        self.assertEqual([i.sol for i in g.bloc(3)], [2, 3, 4, 1])
        self.assertEqual([i.sol for i in g.ligne(2)], [4, 0, 2, 3])
        self.assertEqual([i.sol for i in g.ligne(0)], [1, 0, 3, 0])
        self.assertEqual([i.sol for i in g.colonne(3)], [0, 2, 3, 1])
        self.assertEqual([i.sol for i in g.colonne(1)], [0, 0, 0, 0])

    def testSolverFunctions(self):
        G = [[1, 0, 3, 0], [3, 0, 1, 2], [4, 0, 2, 3], [2, 0, 4, 1]]
        C = [[1, 0, 3, 0], [3, 0, 1, 2], [4, 1, 2, 3], [2, 0, 4, 1]]
        g1 = main.grille()
        c = main.grille()
        g1.importGrille(G, 2, 2)
        c.importGrille(C, 2, 2)
        solv = SolvFunc(g1)
        solv.celib(g1.ligne(0))
        solv.celib(g1.ligne(2))
        solv.sol(g1.ligne(2))
        self.assertEqual(g1[0][1].possibilites, [2, 4])
        self.assertTrue(g1.compare(c))
        g2 = main.grille()
        g2.importGrille(G, 2, 2)
        solv = SolvFunc(g2)
        solv.remove_pos(g2.ligne(0))
        self.assertEqual(g2[0][1].possibilites, [2, 4])
        g3 = main.grille()
        g3.importGrille(G, 2, 2)
        solv = SolvFunc(g3)
        solv.candidat_bloque(g3[0][1])
        self.assertEqual(g3[0][1].possibilites, [2, 4])

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
        solv1.solve()
        solv2.solve()
        self.assertTrue(g1.compare(s))
        self.assertTrue(g2.compare(s))
        A = [[3, 4, 0, 2, 0, 6],
             [6, 0, 0, 0, 4, 3],
             [1, 2, 3, 6, 5, 0],
             [0, 0, 6, 3, 2, 0],
             [5, 6, 0, 4, 3, 2],
             [2, 3, 4, 1, 6, 0]]
        S2 = [[3, 4, 5, 2, 1, 6],
              [6, 1, 2, 5, 4, 3],
              [1, 2, 3, 6, 5, 4],
              [4, 5, 6, 3, 2, 1],
              [5, 6, 1, 4, 3, 2],
              [2, 3, 4, 1, 6, 5]]
        a1 = main.grille()
        a2 = main.grille()
        s2 = main.grille()
        a1.importGrille(A, 3, 2)
        a2.importGrille(A, 3, 2)
        s2.importGrille(S2, 3, 2)
        solv3 = Backtrack(a1)
        solv4 = SolvFunc(a2)
        solv3.solve()
        solv4.solve()
        self.assertTrue(a1.compare(s2))
        self.assertTrue(a2.compare(s2))


if __name__ == '__main__':
    unittest.main()
