import unittest

# from main3 import findroute, findroute_extend

from rf_processing import Rfinder
from rf_input import make_nodeorder


class questionMethods(unittest.TestCase):
    graphdefs = ["AB5", "BC4", "CD8", "DC8", "DE6", "AD5", "CE2", "EB3", "AE7"]

    def test_q1(self):
        bn = "A"  # A6
        en = "C"  # C
        # args = ["shortest"]
        intern = ["B"]

        nodeorder = make_nodeorder(bn, en, intern)
        self.assertEqual(Rfinder(self.graphdefs).return_shortestdistance(nodeorder), 9)

    def test_q2(self):
        bn = "A"  # A
        en = "D"  # D
        # args = ["shortest"]
        nodeorder = make_nodeorder(bn, en)
        self.assertEqual(Rfinder(self.graphdefs).return_shortestdistance(nodeorder), 5)
        # self.assertEqual(findroute_extend(bn, en, self.graphdefs, *args), 5)

    def test_q3(self):
        bn = "A"  # A
        en = "C"  # C
        args = ["shortest"]
        intern = ["D"]
        nodeorder = make_nodeorder(bn, en, intern)
        self.assertEqual(Rfinder(self.graphdefs).return_shortestdistance(nodeorder), 13)

    def test_q4(self):
        bn = "A"  # A
        en = "D"  # C
        # args = ["shortest"]
        intern = ["E", "B", "C"]
        nodeorder = make_nodeorder(bn, en, intern)
        self.assertEqual(Rfinder(self.graphdefs).return_shortestdistance(nodeorder), 22)
        # self.assertEqual(findroute_extend(bn, en, self.graphdefs, *args, **kwargs), 22)

    def test_q5(self):
        bn = "A"  # A
        en = "D"  # D
        # args = ["shortest"]
        intern = ["E"]
        nodeorder = make_nodeorder(bn, en, intern)
        self.assertEqual(
            Rfinder(self.graphdefs).return_shortestdistance(nodeorder), "No Such Route"
        )
        # self.assertEqual(
        #    findroute_extend(bn, en, self.graphdefs, *args, **kwargs), "No Such Route"
        # )

    def test_q6(self):
        bn = "C"  # C
        en = "C"  # C
        # args = ["shortest"]
        maxstops = 3
        nodeorder = make_nodeorder(bn, en)
        self.assertEqual(
            Rfinder(self.graphdefs).return_countmaxstops(nodeorder, maxstops), 2
        )
        # self.assertEqual(findroute_extend(bn, en, self.graphdefs, **kwargs), 2)

    def test_q7(self):
        bn = "A"  # C
        en = "C"  # C
        # args = ["shortest"]
        nrstops = 4
        nodeorder = make_nodeorder(bn, en)
        self.assertEqual(
            Rfinder(self.graphdefs).return_countnrstops(nodeorder, nrstops), 3
        )
        # self.assertEqual(findroute_extend(bn, en, self.graphdefs, **kwargs), 3)

    def test_q8(self):
        bn = "A"  # A
        en = "C"  # C
        nodeorder = make_nodeorder(bn, en)
        self.assertEqual(Rfinder(self.graphdefs).return_shortestdistance(nodeorder), 9)
        # args = ["shortest"]
        # self.assertEqual(findroute_extend(bn, en, self.graphdefs, *args), 9)

    def test_q9(self):
        bn = "B"  # B
        en = "B"  # B
        # args = ["shortest"]
        nodeorder = make_nodeorder(bn, en)
        self.assertEqual(Rfinder(self.graphdefs).return_shortestdistance(nodeorder), 9)
        # self.assertEqual(findroute_extend(bn, en, self.graphdefs, *args), 9)

        self.assertEqual(Rfinder(self.graphdefs).return_shortestdistance(nodeorder), 9)

    def test_q10(self):
        bn = "C"  # C
        en = "C"  # C
        maxdist = 30
        nodeorder = make_nodeorder(bn, en)
        self.assertEqual(
            Rfinder(self.graphdefs).return_countmaxdist(nodeorder, maxdist), 7
        )
        # self.assertEqual(findroute_extend(bn, en, self.graphdefs, **kwargs), 7)


if __name__ == "__main__":
    unittest.main()
