import rf_input as inp
import rf_processing as proc

graphdefs = ["AB5", "BC4", "CD8", "DC8", "DE6", "AD5", "CE2", "EB3", "AE7"]
rf = proc.Rfinder(graphdefs)
if True:
    print("______")
    print("Question 1:")
    bn = "A"  # A
    en = "C"  # C
    intern = ["B"]
    nodeorder = inp.make_nodeorder(bn, en, intern)
    # kwargs = {"intern": }
    print(rf.return_shortestdistance(nodeorder))
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

    nodeorder = inp.make_nodeorder(bn, en)
    print(rf.return_shortestdistance(nodeorder))
    # Question 2

    # xx

if True:
    print("______")
    print("Question 3:")
    # Question 3
    bn = "A"  # A
    en = "C"  # C
    # args = ["shortest"]
    intern = ["D"]
    nodeorder = inp.make_nodeorder(bn, en, intern)
    print(rf.return_shortestdistance(nodeorder))
    # findroute_extend(bn, en, graphdefs, *args, **kwargs)

if True:
    print("______")
    print("Question 4:")
    # Question 4
    bn = "A"  # A
    en = "D"  # C

    # args = ["shortest"]
    intern = ["E", "B", "C"]
    nodeorder = inp.make_nodeorder(bn, en, intern)
    # findroute_extend(bn, en, graphdefs, *args, **kwargs)
    print(rf.return_shortestdistance(nodeorder))
    # xx
if True:
    print("______")
    print("Question 5:")
    # Question 5
    bn = "A"  # A
    en = "D"  # D
    # args = ["shortest"]
    intern = ["E"]
    nodeorder = inp.make_nodeorder(bn, en, intern)
    print(rf.return_shortestdistance(nodeorder))
    # findroute_extend(bn, en, graphdefs, *args, **kwargs)

if True:
    print("______")
    print("Question 6:")
    bn = "C"  # C
    en = "C"  # C
    maxstops = 3

    # args = ["shortest"]
    nodeorder = inp.make_nodeorder(bn, en)
    print(rf.return_countmaxstops(nodeorder, maxstops))
    # findroute_extend(bn, en, graphdefs, **kwargs)
    # xx
if True:
    print("______")
    print("Question 7:")
    bn = "A"  # C
    en = "C"  # C
    nrstops = 4
    nodeorder = inp.make_nodeorder(bn, en)
    print(rf.return_countnrstops(nodeorder, nrstops))
    # findroute_extend(bn, en, graphdefs, **kwargs)

if True:
    print("______")
    print("Question 8:")

    bn = "A"  # A
    en = "C"  # C

    # args = ["shortest"]
    nodeorder = inp.make_nodeorder(bn, en)
    print(rf.return_shortestdistance(nodeorder))
    # findroute_extend(bn, en, graphdefs, *args)

if True:
    print("______")
    print("Question 9:")
    bn = "B"  # B
    en = "B"  # B
    args = ["shortest"]
    nodeorder = inp.make_nodeorder(bn, en)
    print(rf.return_shortestdistance(nodeorder))
    # findroute_extend(bn, en, graphdefs, *args)

if True:
    print("Question 10:")
    bn = "C"  # C
    en = "C"  # C
    maxdist = 30

    nodeorder = inp.make_nodeorder(bn, en)
    print(rf.return_countmaxdist(nodeorder, maxdist))
    # findroute_extend(bn, en, graphdefs, **kwargs)

if True:
    print("Question 11:")
    bn = "B"  # C
    en = "C"  # C
    nodeorder = inp.make_nodeorder(bn, en)
    # kwargs = {"maxdist": 70}
    print(rf.return_countmaxdist(nodeorder, maxdist))
    # findroute_extend(bn, en, graphdefs, **kwargs)

if True:
    print("______")
    print("Question 12:")
    bn = "A"  # C
    en = "C"  # C
    nrstops = 6
    nodeorder = inp.make_nodeorder(bn, en)
    print(rf.return_countnrstops(nodeorder, nrstops))
    # findroute_extend(bn, en, graphdefs, **kwargs)

# if True:
#     graphdefs.extend(["FG2"])
#     bn = "C"  # C
#     en = "G"  # C
#     args = ["shortest"]
#     findroute_extend(bn, en, graphdefs, *args)
#     kwargs = {"maxdist": 30}
#     findroute_extend(bn, en, graphdefs, **kwargs)
