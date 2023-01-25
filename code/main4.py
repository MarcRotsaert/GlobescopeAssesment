import rf_input as inp
import rf_processing as proc


def init(beginnode, endnode, connections, stopover):
    nodescoll = inp.Nodescoll(connections)
    nodeorder = inp.make_nodeorder(beginnode, endnode, nodescoll, stopover)
    rf = proc.Rfinder(connections)
    return rf, nodeorder


def print_distance_shortestroute(beginnode, endnode, connections, stopover=[]):
    rf, nodeorder = init(beginnode, endnode, connections, stopover)
    print(rf.return_shortestdistance(nodeorder))


def print_countmaxstops(beginnode, endnode, connections, nrmaxstops, stopover=[]):
    rf, nodeorder = init(beginnode, endnode, connections, stopover)
    print(rf.return_countmaxstops(nodeorder, nrmaxstops))


def print_countnrstops(beginnode, endnode, connections, nrstops, stopover=[]):
    rf, nodeorder = init(beginnode, endnode, connections, stopover)
    print(rf.return_countnrstops(nodeorder, nrstops))


def print_countmaxdist(beginnode, endnode, connections, maxdist, stopover=[]):
    rf, nodeorder = init(beginnode, endnode, connections, stopover)
    print(rf.return_countmaxdist(nodeorder, maxdist))


connections = ["AB5", "BC4", "CD8", "DC8", "DE6", "AD5", "CE2", "EB3", "AE7"]
print_distance_shortestroute("A", "C", connections)
print_distance_shortestroute("A", "C", connections, ["B"])
print_distance_shortestroute("A", "D", connections, ["E"])
print_countmaxstops("C", "C", connections, 3)
print_countnrstops("A", "C", connections, 4)
print_countmaxdist("C", "C", connections, 30)
# distanceroute
