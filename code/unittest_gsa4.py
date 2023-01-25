import unittest

# from main3 import fininpdroute, findroute_extend

from rf_processing import Rfinder
import rf_input as inp  # Node, Nodescoll, inp.make_nodeorder


class Inputmethods(unittest.TestCase):
    graphdefs = ["AB5", "BC4", "CD8", "DC8", "DE6", "AD5", "CE2", "EB3", "AE7"]
    nodescoll = inp.Nodescoll(graphdefs)

    def test_nodescoll(self):
        self.assertIsInstance(self.nodescoll.nodescoll[0], inp.Node)

    def test_letter2noded(self):
        node = inp.letter2node("A", self.nodescoll)
        self.assertIsInstance(node, inp.Node)
        self.assertEqual(node.name, "A")


class Questionmethods(unittest.TestCase):
    graphdefs = ["AB5", "BC4", "CD8", "DC8", "DE6", "AD5", "CE2", "EB3", "AE7"]
    nodescoll = inp.Nodescoll(graphdefs)

    def test_q1(self):
        bn = "A"
        en = "C"
        intern = ["B"]
        nodeorder = inp.make_nodeorder(bn, en, self.nodescoll, intern)
        self.assertEqual(Rfinder(self.graphdefs).return_shortestdistance(nodeorder), 9)

    def test_q2(self):
        bn = "A"  # A
        en = "D"  # D
        nodeorder = inp.make_nodeorder(bn, en, self.nodescoll)
        self.assertEqual(Rfinder(self.graphdefs).return_shortestdistance(nodeorder), 5)

    def test_q3(self):
        bn = "A"  # A
        en = "C"  # C
        intern = ["D"]
        nodeorder = inp.make_nodeorder(bn, en, self.nodescoll, intern)
        self.assertEqual(Rfinder(self.graphdefs).return_shortestdistance(nodeorder), 13)

    def test_q4(self):
        bn = "A"  # A
        en = "D"  # C
        intern = ["E", "B", "C"]
        nodeorder = inp.make_nodeorder(bn, en, self.nodescoll, intern)
        self.assertEqual(Rfinder(self.graphdefs).return_shortestdistance(nodeorder), 22)

    def test_q5(self):
        bn = "A"  # A
        en = "D"  # D
        intern = ["E"]
        nodeorder = inp.make_nodeorder(bn, en, self.nodescoll, intern)
        self.assertEqual(
            Rfinder(self.graphdefs).return_shortestdistance(nodeorder), "No Such Route"
        )

    def test_q6(self):
        bn = "C"  # C
        en = "C"  # C
        maxstops = 3
        nodeorder = inp.make_nodeorder(bn, en, self.nodescoll)
        self.assertEqual(
            Rfinder(self.graphdefs).return_countmaxstops(nodeorder, maxstops), 2
        )

    def test_q7(self):
        bn = "A"  # C
        en = "C"  # C
        nrstops = 4
        nodeorder = inp.make_nodeorder(bn, en, self.nodescoll)
        self.assertEqual(
            Rfinder(self.graphdefs).return_countnrstops(nodeorder, nrstops), 3
        )

    def test_q8(self):
        bn = "A"  # A
        en = "C"  # C
        nodeorder = inp.make_nodeorder(bn, en, self.nodescoll)
        self.assertEqual(Rfinder(self.graphdefs).return_shortestdistance(nodeorder), 9)

    def test_q9(self):
        bn = "B"  # B
        en = "B"  # B
        nodeorder = inp.make_nodeorder(bn, en, self.nodescoll)
        self.assertEqual(Rfinder(self.graphdefs).return_shortestdistance(nodeorder), 9)

    def test_q10(self):
        bn = "C"  # C
        en = "C"  # C
        maxdist = 30
        nodeorder = inp.make_nodeorder(bn, en, self.nodescoll)
        self.assertEqual(
            Rfinder(self.graphdefs).return_countmaxdist(nodeorder, maxdist), 7
        )


if __name__ == "__main__":
    unittest.main()
