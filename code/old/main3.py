from railroads import Node, Edge, Route

# import time


def make_nodescoll(graphdefs: list) -> list:
    # make colllection (list) of Node-objects
    # input: graphdefs=> list of strings containing 3 characters. example: 'AB4'
    # output: list of Nodeobjects.

    def decode_edge(text):
        edge1, edge2, dump = text
        weight = int(dump)
        return edge1, edge2, weight

    nodescoll = []
    nodesnames = []
    for temp in graphdefs:
        dump = decode_edge(temp)
        nodesnames.extend([dump[0], dump[1]])
    nodesnames = list(set(nodesnames))
    nodesnames.sort()

    nodescoll = [Node(no) for no in nodesnames]

    for temp in graphdefs:
        dump = decode_edge(temp)
        e_1 = Edge(dump[0] + dump[1], dump[2])
        for i, no in enumerate(nodescoll):
            if no.name == dump[0]:
                no.add_edgeout(e_1)
            elif no.name == dump[1]:
                no.add_edgein(e_1)
    return nodescoll


def letter2node(letter: str, nodescoll: list) -> Node:
    # Return Node- object from a list of Node objects by letter
    # input: letter => letter from alphabet, str.
    #       nodescoll: list of nodeobjects
    # output: Nodeobject
    nodeobj = None
    i = 0
    while nodeobj == None:
        if letter == nodescoll[i].name:
            nodeobj = nodescoll[i]
        i += 1
    return nodeobj


def routing(beginnode: Node, endnode: Node, nodes: list, maxroutes=20) -> list:
    # Make possible and impossible routes based on beginnode, endnode and collection of nodes
    # Input:
    #   beginnode: beginning node (Node-object)
    #   endnode: endnode           (Node-object)
    #   nodes: collection of nodes. list of nodes

    # Output:
    # routes list of lists
    #   routes[x]= routes[x][0] =>list nodes-edge;
    #   routes[x][1] => False= route continues; True = routes ends

    def addnode2route(route):
        node = route.route[-1].find_connectednode(nodes, "in")
        route.route.append(node)
        return route, node

    def check_endroute(node, endnode):
        # check
        return node.name == endnode.name

    # initiate routes
    routes = []
    routes.append(Route([beginnode]))

    i = 0  # Route teller
    while i <= len(routes) - 1:

        route = routes[i]
        if type(route.route[-1]) is Edge:
            route, node = addnode2route(route)
            if check_endroute(node, endnode):
                route.end = True  # end of route at destination
                i += 1
                continue

        altroutes = route.add_toroute()
        routes.extend([Route(ro) for ro in altroutes])
        route, node = addnode2route(route)

        if route.check_nodereoccurance():
            i += 1  # ends not at destination
            continue
        if check_endroute(node, endnode):
            route.end = True  # end of route at destination
            i += 1

        if len(routes) == i or i == maxroutes:
            print(i)
            break
    return routes


def make_nodeorder(nodescoll: list[Node], bn: str, en: str, kwargs: dict) -> list:
    # make list of strings representing nodes
    # kwargs: 'intern': list of points

    nodeorder = [bn]
    if "intern" in kwargs:
        for nn in kwargs["intern"]:
            nodeorder.append(nn)
    nodeorder.append(en)
    return nodeorder


def init_findroute_extend(graphdefs: list, bn: str, en: str, kwargs: dict):

    nodescoll = make_nodescoll(graphdefs)
    nodeorder = make_nodeorder(nodescoll, bn, en, kwargs)
    bn = letter2node(nodeorder[0], nodescoll)
    en = letter2node(nodeorder[-1], nodescoll)
    return nodescoll, nodeorder, bn, en


def findcorrectroutes(routesin: list, nodeorder: list) -> list:
    # filter routes in list that contain correct order of nodes.
    # input:    routesin => list of Route-objects
    #           nodeorder => list of nodes.
    # output:
    #           list of routes
    routesout = []
    for route in routesin:
        res = route.check_nodesorder(nodeorder)
        if res:
            routesout.append(route)
    return routesout


def count_routesmaxstop(routes_d: list, routes_e: list, maxstops: int) -> int:
    # count routes with maximum stops.
    # input:
    result = 0
    for route1 in routes_d:
        nrstop1 = route1.return_nrstops()
        if nrstop1 < maxstops + 1:
            result += 1
        for route2 in routes_e:
            nrstop12 = nrstop1 + route2.return_nrstops()
            if nrstop12 < maxstops + 1:
                result += 1
    return result


def count_routesnrstop(routes_d: list, routes_e: list, nrstops: int) -> int:
    result = 0
    for route1 in routes_d:
        nrstop1 = route1.return_nrstops()
        if nrstop1 == nrstops:
            result += 1
        for route2 in routes_e:
            nrstop12 = nrstop1 + route2.return_nrstops()
            if nrstop12 == nrstops:
                result += 1
    return result


def count_routesmaxdist(routes_d: list, routes_e: list, maxdist: float) -> int:
    route_u = []
    for route in routes_d:
        if route.return_totdistance() < maxdist:
            # route_u.append([route, True])
            route_u.append(route)

    x1 = 0
    x2 = len(route_u)
    while x2 > x1:
        k = 0
        for a in range(x1, x2):
            for route in routes_e:
                routetest = route_u[a] + route
                if routetest.return_totdistance() < maxdist:
                    route_u.append(routetest)
                    k += 1
        x1 = x2
        x2 = x1 + k
    output = len(route_u)
    return output


def findroute_extend(
    bn: str, en: str, graphdefs: list, *args, **kwargs
) -> int | str | None:
    # MAIN FUNCTION2
    # args
    #   options, 'shortest'
    # kwargs options:
    #   'maxdist'|'maxstops'|'nrstops'
    nodescoll, nodeorder, bn, en = init_findroute_extend(graphdefs, bn, en, kwargs)

    routes_d = routing(bn, en, nodescoll)
    routes_e = routing(en, en, nodescoll)

    if "intern" in kwargs:
        routes = findcorrectroutes(routes_d, nodeorder)
    else:
        routes = routes_d

    if len(routes) == 0:
        output = "No Such Route"
        print("No Such Route")
        return output

    # Answering different questions
    if "shortest" in args:
        distance = 999
        for route in routes:
            temp = route.return_totdistance()
            distance = min(temp, distance)
        output = distance

    elif "maxdist" in kwargs:
        output = count_routesmaxdist(routes, routes_e, kwargs["maxdist"])
    else:
        if "maxstops" in kwargs:
            output = count_routesmaxstop(routes, routes_e, kwargs["maxstops"])
        elif "nrstops" in kwargs:
            output = count_routesnrstop(routes, routes_e, kwargs["nrstops"])
    return output


if __name__ == "__main__":
    graphdefs = ["AB5", "BC4", "CD8", "DC8", "DE6", "AD5", "CE2", "EB3", "AE7"]

    if True:
        print("______")
        print("Question 1:")
        bn = "A"  # A
        en = "C"  # C
        args = ["shortest"]
        kwargs = {"intern": ["B"]}
        findroute_extend(bn, en, graphdefs, *args, **kwargs)
        # xx
    if True:
        print("______")
        print("Question 2:")
        # Question 2

        bn = "A"  # A
        en = "D"  # D

        args = ["shortest"]
        findroute_extend(bn, en, graphdefs, *args)

    if True:
        print("______")
        print("Question 3:")
        # Question 3
        bn = "A"  # A
        en = "C"  # C
        args = ["shortest"]
        kwargs = {"intern": "D"}
        findroute_extend(bn, en, graphdefs, *args, **kwargs)

    if True:
        print("______")
        print("Question 4:")
        # Question 4
        bn = "A"  # A
        en = "D"  # C

        args = ["shortest"]
        kwargs = {"intern": ["E", "B", "C"]}
        findroute_extend(bn, en, graphdefs, *args, **kwargs)

    if True:
        print("______")
        print("Question 5:")
        # Question 5
        bn = "A"  # A
        en = "D"  # D
        args = ["shortest"]
        kwargs = {"intern": "E"}
        findroute_extend(bn, en, graphdefs, *args, **kwargs)

    if False:
        print("______")
        print("Question 6:")
        bn = "C"  # C
        en = "C"  # C

        args = ["shortest"]
        kwargs = {"maxstops": 3}
        findroute_extend(bn, en, graphdefs, **kwargs)

    if False:
        print("______")
        print("Question 7:")
        bn = "A"  # C
        en = "C"  # C
        kwargs = {"nrstops": 4}
        findroute_extend(bn, en, graphdefs, **kwargs)

    if False:
        print("______")
        print("Question 8:")

        bn = "A"  # A
        en = "C"  # C

        args = ["shortest"]
        findroute_extend(bn, en, graphdefs, *args)

    if False:
        print("______")
        print("Question 9:")
        bn = "B"  # B
        en = "B"  # B
        args = ["shortest"]
        findroute_extend(bn, en, graphdefs, *args)

    if False:
        print("Question 10:")
        bn = "C"  # C
        en = "C"  # C
        kwargs = {"maxdist": 30}
        findroute_extend(bn, en, graphdefs, **kwargs)

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
