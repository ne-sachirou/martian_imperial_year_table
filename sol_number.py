import math


class SolNumber(object):
    "帝國火星暦の通算日"

    def __init__(self, sol_number):
        if isinstance(sol_number, SolNumber):
            sol_number = sol_number.sol_number
        self.sol_number = sol_number

    def __eq__(self, other):
        if not isinstance(other, SolNumber):
            return False
        return math.isclose(self.sol_number, other.sol_number, abs_tol = 0.00001)

    @property
    def date(self):
        return math.floor(self.sol_number)

    @property
    def time(self):
        return self.sol_number % 1
