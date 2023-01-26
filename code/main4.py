import rf_input as inp
import rf_processing as proc
from typing import Tuple, Union


def __init(
    beginnode: str, endnode: str, connections: list, stopover: Union[list, str]
) -> Tuple[proc.Rfinder, list]:
    nodescoll = inp.Nodescoll(connections)
    nodeorder = inp.make_nodeorder(beginnode, endnode, nodescoll, stopover)
    rf = proc.Rfinder(connections)
    return rf, nodeorder


def print_distance_shortestroute(
    # Print distance shortest route between beginnode and endnode begin
    # eventually with stopovers
    beginnode: str,
    endnode: str,
    connections: list,
    stopover=None,
):
    rf, nodeorder = __init(beginnode, endnode, connections, stopover)
    print(rf.return_shortestdistance(nodeorder))


def print_countmaxstops(
    # Print number of routes between beginnode and endnode begin, with less than x stops
    # eventually with stopovers
    beginnode: str,
    endnode: str,
    connections: list,
    nrmaxstops: int,
    stopover=None,
):
    rf, nodeorder = __init(beginnode, endnode, connections, stopover)
    print(rf.return_countmaxstops(nodeorder, nrmaxstops))


def print_countnrstops(
    # Print number of routes between beginnode and endnode begin, that equals  x stops
    # eventually with stopovers
    beginnode: str,
    endnode: str,
    connections: list,
    nrstops: int,
    stopover=None,
):
    rf, nodeorder = __init(beginnode, endnode, connections, stopover)
    print(rf.return_countnrstops(nodeorder, nrstops))


def print_countmaxdist(
    # Print number of routes between beginnode and endnode begin,with maximum distance of x
    # eventually with stopovers
    beginnode: str,
    endnode: str,
    connections: list,
    maxdist: float,
    stopover=None,
):
    rf, nodeorder = __init(beginnode, endnode, connections, stopover)
    print(rf.return_countmaxdist(nodeorder, maxdist))


if __name__ == "__main__":
    graphfdefs = ["AB5", "BC4", "CD8", "DC8", "DE6", "AD5", "CE2", "EB3", "AE7"]
    print_distance_shortestroute("A", "C", graphfdefs, None)
    print_distance_shortestroute("A", "C", graphfdefs, ["B"])
    print_distance_shortestroute("A", "D", graphfdefs, "E")
    print_countmaxstops("C", "C", graphfdefs, 3)
    print_countnrstops("A", "C", graphfdefs, 4)
    print_countmaxdist("C", "C", graphfdefs, 30)
