import unittest

# from main3 import findroute, findroute_extend
from main3 import findroute_extend


class questionMethods(unittest.TestCase):
    graphdefs = ["AB5", "BC4", "CD8", "DC8", "DE6", "AD5", "CE2", "EB3", "AE7"]

    def test_q1(self):
        bn = "A"  # A6
        en = "C"  # C
        args = ["shortest"]
        kwargs = {"intern": ["B"]}
        self.assertEqual(findroute_extend(bn, en, self.graphdefs, *args, **kwargs), 9)

    def test_q2(self):
        bn = "A"  # A
        en = "D"  # D
        args = ["shortest"]
        self.assertEqual(findroute_extend(bn, en, self.graphdefs, *args), 5)

    def test_q3(self):
        bn = "A"  # A
        en = "C"  # C
        args = ["shortest"]
        kwargs = {"intern": "D"}
        self.assertEqual(findroute_extend(bn, en, self.graphdefs, *args, **kwargs), 13)

    def test_q4(self):
        bn = "A"  # A
        en = "D"  # C
        args = ["shortest"]
        kwargs = {"intern": ["E", "B", "C"]}
        self.assertEqual(findroute_extend(bn, en, self.graphdefs, *args, **kwargs), 22)

    def test_q5(self):
        bn = "A"  # A
        en = "D"  # D
        args = ["shortest"]
        kwargs = {"intern": "E"}
        self.assertEqual(
            findroute_extend(bn, en, self.graphdefs, *args, **kwargs), "No Such Route"
        )

    def test_q6(self):
        bn = "C"  # C
        en = "C"  # C
        # args = ["shortest"]
        kwargs = {"maxstops": 3}
        self.assertEqual(findroute_extend(bn, en, self.graphdefs, **kwargs), 2)

    def test_q7(self):
        bn = "A"  # C
        en = "C"  # C
        # args = ["shortest"]
        kwargs = {"nrstops": 4}
        self.assertEqual(findroute_extend(bn, en, self.graphdefs, **kwargs), 3)

    def test_q8(self):
        bn = "A"  # A
        en = "C"  # C
        args = ["shortest"]
        self.assertEqual(findroute_extend(bn, en, self.graphdefs, *args), 9)

    def test_q9(self):
        bn = "B"  # B
        en = "B"  # B
        args = ["shortest"]
        self.assertEqual(findroute_extend(bn, en, self.graphdefs, *args), 9)

    def test_q10(self):
        bn = "C"  # C
        en = "C"  # C
        kwargs = {"maxdist": 30}
        self.assertEqual(findroute_extend(bn, en, self.graphdefs, **kwargs), 7)


if __name__ == "__main__":
    unittest.main()
