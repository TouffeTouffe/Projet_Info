import unittest
import backtrack
import solv_func
import main

class TestGrilleComplete(unittest.TestCase):
    G = [[1, 0, 3, 0], [3, 0, 1, 2], [4, 0, 2, 3], [2, 0, 4, 1]]
    g=main.grille()
    g.importGrille(G, 2, 2)

    def testFoolProof(self):
        pass
