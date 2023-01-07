from railroads import Node, Edge, Route
import time


def letter2node(letter, nodescoll):
    nodeobj = None
    i = 0
    while nodeobj == None:
        if letter == nodescoll[i].name:
            nodeobj = nodescoll[i]
        i += 1
    return nodeobj


def make_nodescoll(edgedefs):
    # make colllection (list) of Node-objects.
    # input: edgedefs=> list of strings containing 3 characters. example: 'AB4'
    # output: list of Nodeobjects.

    def decode_edge(text):

        edge1, edge2, dump = text
        weight = int(dump)
        return edge1, edge2, weight

    nodescoll = []
    nodesnames = []
    for temp in edgedefs:
        dump = decode_edge(temp)
        nodesnames.append(dump[0])
        nodesnames.append(dump[1])
    nodesnames = list(set(nodesnames))
    nodesnames.sort()
    for no in nodesnames:
        nodescoll.append(Node(no))

    for temp in edgedefs:
        dump = decode_edge(temp)
        e_1 = Edge(dump[0] + dump[1], dump[2])
        for i, no in enumerate(nodescoll):
            if no.name == dump[0]:
                no.add_edgeout(e_1)
                # break
        for i, no in enumerate(nodescoll):
            if no.name == dump[1]:
                no.add_edgein(e_1)
    return nodescoll


def routing(beginnode, endnode, nodes):
    # Make possible and impossible routes based on beginnode, endnode and collection of nodes
    # Input:
    #   beginnode: beginning node (Node-object)
    #   endnode: endnode           (Node-object)
    #   nodes: collection of nodes. list of nodes

    # Output:
    # routes list of lists
    #   routes[x]= routes[x][0] =>list nodes-edge;
    #   routes[x][1] => False= route continues; True = routes ends

    # initiate first route
    routes = []
    routes.append(Route([beginnode]))
    i = 0  # Route teller
    # for a in range(10):
    while i <= len(routes) - 1:
        route = routes[i]
        if type(route.route[-1]) is Edge:
            node = route.route[-1].find_node(nodes, "in")
            route.route.append(node)
            if node.name == endnode.name:
                route.end = True  # end of route at destination
                i += 1
                continue

        altroutes = route.add_edges()
        routes.extend([Route(ro) for ro in altroutes])
        edgein = route.route[-1]
        nodein = edgein.find_node(nodes, "in")
        # print(i)
        # print(nodein)
        route.route.append(nodein)

        if route.check_nodereaccurance():
            i += 1  # ends not at destination
            continue
            # route[1] = True
        if nodein.name == endnode.name:
            route.end = True  # end of route at destination
        if route.end:
            i += 1
        if len(routes) == i:
            # print(i)
            break
        if i == 20:
            break  # emergency break

    return routes


def findroutes(bn, en, edgedefs, **kwargs):
    nodescoll = make_nodescoll(edgedefs)
    bn = letter2node(bn, nodescoll)
    en = letter2node(en, nodescoll)

    routes1 = routing(bn, en, nodescoll)
    routes2 = routing(en, en, nodescoll)

    if "maxdist" in kwargs:
        route_u = []
        for route in routes1:
            if route.return_totdistance() < kwargs["maxdist"]:
                route_u.append([route, True])
        x1 = 0
        x2 = len(route_u)
        while x2 > x1:
            k = 0
            for a in range(x1, x2):
                for i, route in enumerate(routes2):
                    # if route_u[3 * a + i][1] == True:
                    routetest = route_u[a][0] + route
                    # print(routetest.return_totdistance())
                    if routetest.return_totdistance() < kwargs["maxdist"]:
                        route_u.append([routetest, True])
                        k += 1
            x1 = x2
            x2 = x1 + k
        print(len(route_u))
        output = len(route_u)

    else:
        result = 0
        for route1 in routes1:
            if "maxstops" in kwargs:
                if route1.return_nrstops() < kwargs["maxstops"] + 2:
                    result += 1
            elif "nrstops" in kwargs:
                if route1.return_nrstops() == kwargs["nrstops"] + 1:
                    result += 1

                # route1.print_stops()
                # print("______")
                # result += 1

            for route2 in routes2:
                temp_nrs = route1.return_nrstops() + route2.return_nrstops()
                if "maxstops" in kwargs:
                    if temp_nrs < kwargs["maxstops"] + 2:
                        # print("______")
                        result += 1
                elif "nrstops" in kwargs:
                    if temp_nrs == kwargs["nrstops"] + 2:
                        route1.print_stops()
                        route2.print_stops()
                        result += 1

                    # res = route.checknodesorder(nodeorder)
                    # print(res)
        print(result)
        output = result
        # time.sleep(1)  # xx
    return output


def findroute(bn, en, edgedefs, *args, **kwargs):
    nodescoll = make_nodescoll(edgedefs)
    bn = letter2node(bn, nodescoll)
    en = letter2node(en, nodescoll)

    routes = routing(bn, en, nodescoll)
    nodeorder = [bn.name]
    # if intern != None:

    if "intern" in kwargs:
        for nn in kwargs["intern"]:
            nn = letter2node(nn, nodescoll)
            nodeorder.append(nn.name)
    nodeorder.append(en.name)

    # print(routes)
    routefound = False
    if "intern" in kwargs:
        for route in routes:
            res = route.checknodesorder(nodeorder)
            if res:
                routefound = True
                routes = [route]
                break
    else:
        if len(routes) > 0:
            routefound = True
    if "shortest" in args:
        if routefound:
            distance = 999
            for route in routes:
                temp = route.return_totdistance()
                distance = min(temp, distance)
            output = distance
            print(distance)
        else:
            output = "No Such Route"
            print("No Such Route")
    return output


# def print_routdist(route):


if __name__ == "__main__":
    edgedefs = ["AB5", "BC4", "CD8", "DC8", "DE6", "AD5", "CE2", "EB3", "AE7"]
    # nodescoll = make_nodescoll(edgedefs)
    # for i in nodescoll:
    # print(nodescoll)
    #    print(i.edgein)
    # print(len(nodescoll))

    if False:
        print("______")
        print("Question 1:")
        bn = "A"  # A
        en = "C"  # C
        args = ["shortest"]
        kwargs = {"intern": ["B"]}
        findroute(bn, en, edgedefs, *args, **kwargs)
        # xx
    if False:
        print("______")
        print("Question 2:")
        # Question 2

        bn = "A"  # A
        en = "D"  # D

        args = ["shortest"]
        findroute(bn, en, edgedefs, *args)
    if False:
        print("______")
        print("Question 3:")
        # Question 3
        bn = "A"  # A
        en = "C"  # C
        args = ["shortest"]
        kwargs = {"intern": "D"}
        findroute(bn, en, edgedefs, *args, **kwargs)

    if True:
        print("______")
        print("Question 4:")
        # Question 4
        bn = "A"  # A
        en = "D"  # C

        args = ["shortest"]
        kwargs = {"intern": ["E", "B", "C"]}
        findroute(bn, en, edgedefs, *args, **kwargs)

    if False:
        print("______")
        print("Question 5:")
        # Question 5
        bn = "A"  # A
        en = "D"  # D
        args = ["shortest"]
        kwargs = {"intern": "E"}
        findroute(bn, en, edgedefs, *args, **kwargs)

    if True:
        print("______")
        print("Question 6:")
        bn = "C"  # C
        en = "C"  # C

        args = ["shortest"]
        kwargs = {"maxstops": 3}
        findroutes(bn, en, edgedefs, **kwargs)

    if True:
        print("______")
        print("Question 7:")
        bn = "A"  # C
        en = "C"  # C
        args = ["shortest"]
        kwargs = {"nrstops": 4}
        findroutes(bn, en, edgedefs, **kwargs)

    if False:
        print("______")
        print("Question 8:")

        bn = "A"  # A
        en = "C"  # C

        args = ["shortest"]
        findroute(bn, en, edgedefs, *args)

    if False:
        print("______")
        print("Question 9:")
        bn = "B"  # B
        en = "B"  # B
        args = ["shortest"]
        findroute(bn, en, edgedefs, *args)

    if False:
        print("Question 10:")
        bn = "C"  # C
        en = "C"  # C
        kwargs = {"maxdist": 30}
        findroutes(bn, en, edgedefs, **kwargs)
