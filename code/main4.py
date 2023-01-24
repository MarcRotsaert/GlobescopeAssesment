import rf_input as inp
import rf_processing as proc

graphdefs = ["AB5", "BC4", "CD8", "DC8", "DE6", "AD5", "CE2", "EB3", "AE7"]
if True:
    print("______")
    print("Question 1:")
    bn = "A"  # A
    en = "C"  # C
    args = ["B"]
    # kwargs = {"intern": }

    rf = proc.Rfinder(graphdefs)
    print(rf.return_shortestdistance(bn, en, args))
# xx
# nodescoll, nodeorder, bn, en = inp.init_findroute_extend(graphdefs, bn, en, *args)
# proc.Rfinder(nodeorder, nodescoll)

# print(nodescoll)
# print(nodeorder)
# print(bn)
# print(en)
# proc.findroute_extend(bn, en, graphdefs, *args)

if True:
    print("______")
    print("Question 2:")
    bn = "A"  # A
    en = "D"  # D
    print(rf.return_shortestdistance(bn, en))
    # Question 2

    # xx

if True:
    print("______")
    print("Question 3:")
    # Question 3
    bn = "A"  # A
    en = "C"  # C
    # args = ["shortest"]
    args = ["D"]
    print(rf.return_shortestdistance(bn, en, args))
    # findroute_extend(bn, en, graphdefs, *args, **kwargs)

if True:
    print("______")
    print("Question 4:")
    # Question 4
    bn = "A"  # A
    en = "D"  # C

    # args = ["shortest"]
    args = ["E", "B", "C"]
    # findroute_extend(bn, en, graphdefs, *args, **kwargs)
    print(rf.return_shortestdistance(bn, en, args))

if True:
    print("______")
    print("Question 5:")
    # Question 5
    bn = "A"  # A
    en = "D"  # D
    # args = ["shortest"]
    args = ["E"]
    print(rf.return_shortestdistance(bn, en, args))
    # findroute_extend(bn, en, graphdefs, *args, **kwargs)

if True:
    print("______")
    print("Question 6:")
    bn = "C"  # C
    en = "C"  # C

    # args = ["shortest"]
    maxstops = 3
    print(rf.return_countmaxdist(bn, en, maxstops))
    # findroute_extend(bn, en, graphdefs, **kwargs)

if True:
    print("______")
    print("Question 7:")
    bn = "A"  # C
    en = "C"  # C
    nrstops = 4
    print(rf.return_countmaxdist(bn, en, nrstops))
    # findroute_extend(bn, en, graphdefs, **kwargs)

if True:
    print("______")
    print("Question 8:")

    bn = "A"  # A
    en = "C"  # C

    # args = ["shortest"]
    print(rf.return_shortestdistance(bn, en))
    # findroute_extend(bn, en, graphdefs, *args)

if True:
    print("______")
    print("Question 9:")
    bn = "B"  # B
    en = "B"  # B
    args = ["shortest"]
    print(rf.return_shortestdistance(bn, en))
    # findroute_extend(bn, en, graphdefs, *args)

if True:
    print("Question 10:")
    bn = "C"  # C
    en = "C"  # C
    maxdist = 30
    print(rf.return_countmaxdist(bn, en, maxdist))
    # findroute_extend(bn, en, graphdefs, **kwargs)

if False:
    print("Question 11:")
    bn = "B"  # C
    en = "C"  # C
    kwargs = {"maxdist": 70}
    findroute_extend(bn, en, graphdefs, **kwargs)

if False:
    print("______")
    print("Question 12:")
    bn = "A"  # C
    en = "C"  # C
    kwargs = {"nrstops": 6}
    findroute_extend(bn, en, graphdefs, **kwargs)

if False:
    graphdefs.extend(["FG2"])
    bn = "C"  # C
    en = "G"  # C
    args = ["shortest"]
    findroute_extend(bn, en, graphdefs, *args)
    kwargs = {"maxdist": 30}
    findroute_extend(bn, en, graphdefs, **kwargs)
