import unittest

# from main3 import fininpdroute, findroute_extend

from rf_processing import Rfinder
from rf_input import Nodescoll, make_nodeorder


class Questionmethods(unittest.TestCase):
    graphdefs = ["AB5", "BC4", "CD8", "DC8", "DE6", "AD5", "CE2", "EB3", "AE7"]
    nodescoll = Nodescoll(graphdefs)

    def test_q1(self):
        bn = "A"
        en = "C"
        intern = ["B"]
        nodeorder = make_nodeorder(bn, en, self.nodescoll, intern)
        self.assertEqual(Rfinder(self.graphdefs).return_shortestdistance(nodeorder), 9)

    def test_q2(self):
        bn = "A"  # A
        en = "D"  # D
        nodeorder = make_nodeorder(bn, en, self.nodescoll)
        self.assertEqual(Rfinder(self.graphdefs).return_shortestdistance(nodeorder), 5)

    def test_q3(self):
        bn = "A"  # A
        en = "C"  # C
        intern = ["D"]
        nodeorder = make_nodeorder(bn, en, self.nodescoll, intern)
        self.assertEqual(Rfinder(self.graphdefs).return_shortestdistance(nodeorder), 13)

    def test_q4(self):
        bn = "A"  # A
        en = "D"  # C
        intern = ["E", "B", "C"]
        nodeorder = make_nodeorder(bn, en, self.nodescoll, intern)
        self.assertEqual(Rfinder(self.graphdefs).return_shortestdistance(nodeorder), 22)

    def test_q5(self):
        bn = "A"  # A
        en = "D"  # D
        intern = ["E"]
        nodeorder = make_nodeorder(bn, en, self.nodescoll, intern)
        self.assertEqual(
            Rfinder(self.graphdefs).return_shortestdistance(nodeorder), "No Such Route"
        )

    def test_q6(self):
        bn = "C"  # C
        en = "C"  # C
        maxstops = 3
        nodeorder = make_nodeorder(bn, en, self.nodescoll)
        self.assertEqual(
            Rfinder(self.graphdefs).return_countmaxstops(nodeorder, maxstops), 2
        )

    def test_q7(self):
        bn = "A"  # C
        en = "C"  # C
        nrstops = 4
        nodeorder = make_nodeorder(bn, en, self.nodescoll)
        self.assertEqual(
            Rfinder(self.graphdefs).return_countnrstops(nodeorder, nrstops), 3
        )

    def test_q8(self):
        bn = "A"  # A
        en = "C"  # C
        nodeorder = make_nodeorder(bn, en, self.nodescoll)
        self.assertEqual(Rfinder(self.graphdefs).return_shortestdistance(nodeorder), 9)

    def test_q9(self):
        bn = "B"  # B
        en = "B"  # B
        nodeorder = make_nodeorder(bn, en, self.nodescoll)
        self.assertEqual(Rfinder(self.graphdefs).return_shortestdistance(nodeorder), 9)

    def test_q10(self):
        bn = "C"  # C
        en = "C"  # C
        maxdist = 30
        nodeorder = make_nodeorder(bn, en, self.nodescoll)
        self.assertEqual(
            Rfinder(self.graphdefs).return_countmaxdist(nodeorder, maxdist), 7
        )


if __name__ == "__main__":
    unittest.main()
