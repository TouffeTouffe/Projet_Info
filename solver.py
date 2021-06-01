from abc import ABC, abstractmethod


class Solver(ABC):
    def __init__(self, g):
        self.grille = g

    @abstractmethod
    def solve(self):
        ...
