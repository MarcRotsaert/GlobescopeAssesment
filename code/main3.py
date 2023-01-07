from railroads import Node, Edge, Route
import time


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
    routes1 = routing(bn, en, nodescoll)
    routes2 = routing(en, en, nodescoll)
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
                    # route1.print_stops()
                    # route2.print_stops()
                    # print("______")
                    result += 1
            elif "nrstops" in kwargs:
                if temp_nrs == kwargs["nrstops"] + 2:
                    result += 1

                # res = route.checknodesorder(nodeorder)
                # print(res)
    print(result)
    time.sleep(1)  # xx


def findroute(bn, en, edgedefs, *args, **kwargs):
    nodescoll = make_nodescoll(edgedefs)
    routes = routing(bn, en, nodescoll)
    nodeorder = [bn.name]
    # if intern != None:

    if "intern" in kwargs:
        for nn in kwargs["intern"]:
            nodeorder.append(nn.name)
    nodeorder.append(en.name)

    # print(routes)
    routefound = False
    # if "shortest" in args:
    #    print("x")
    #    xx
    if "intern" in kwargs:
        for route in routes:
            res = route.checknodesorder(nodeorder)
            # print(res)
            if res:
                # print(route.return_totdistance())
                routefound = True
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
            print(distance)
        else:
            print("No Such Route")


# def print_routdist(route):


if __name__ == "__main__":
    edgedefs = ["AB5", "BC4", "CD8", "DC8", "DE6", "AD5", "CE2", "EB3", "AE7"]
    nodescoll = make_nodescoll(edgedefs)
    # for i in nodescoll:
    # print(nodescoll)
    #    print(i.edgein)
    # print(len(nodescoll))

    if True:
        print("______")
        print("Question 1:")
        bn = nodescoll[0]  # A
        en = nodescoll[2]  # C
        args = ["shortest"]
        kwargs = {"intern": [nodescoll[1]]}
        findroute(bn, en, edgedefs, *args, **kwargs)
    if True:

        print("______")
        print("Question 2:")
        # Question 2

        bn = nodescoll[0]  # A
        en = nodescoll[3]  # D

        args = ["shortest"]
        findroute(bn, en, edgedefs, *args)
    if True:
        print("______")
        print("Question 3:")
        # Question 3
        bn = nodescoll[0]  # A
        en = nodescoll[2]  # C
        args = ["shortest"]
        kwargs = {"intern": [nodescoll[3]]}
        findroute(bn, en, edgedefs, *args, **kwargs)

    if True:
        print("______")
        print("Question 4:")
        # Question 4
        bn = nodescoll[0]  # A
        en = nodescoll[3]  # C

        args = ["shortest"]
        kwargs = {"intern": [nodescoll[4], nodescoll[1], nodescoll[2]]}
        findroute(bn, en, edgedefs, *args, **kwargs)

    if True:
        print("______")
        print("Question 5:")
        # Question 5
        bn = nodescoll[0]  # A
        en = nodescoll[3]  # D
        args = ["shortest"]
        kwargs = {"intern": [nodescoll[4]]}
        findroute(bn, en, edgedefs, *args, **kwargs)

    if True:
        print("______")
        print("Question 6:")
        bn = nodescoll[2]  # C
        en = nodescoll[2]  # C

        args = ["shortest"]
        kwargs = {"maxstops": 3}
        findroutes(bn, en, edgedefs, **kwargs)

    if True:
        print("______")
        print("Question 7:")
        bn = nodescoll[0]  # C
        en = nodescoll[2]  # C
        args = ["shortest"]
        kwargs = {"nrstops": 4}
        findroutes(bn, en, edgedefs, **kwargs)

    if True:
        print("______")
        print("Question 8:")

        bn = nodescoll[0]  # A
        en = nodescoll[2]  # C

        args = ["shortest"]
        findroute(bn, en, edgedefs, *args)
        # xx
        # routes = routing(bn, en, nodescoll)

        # result = 0
        # distance = 999
        # for route in routes:
        #     temp = route.return_totdistance()
        #     distance = min(temp, distance)
        # print(distance)
        # time.sleep(1)  # xx

    if True:
        print("______")
        print("Question 9:")
        bn = nodescoll[1]  # B
        en = nodescoll[1]  # B
        args = ["shortest"]
        findroute(bn, en, edgedefs, *args)

    if True:
        print("Question 10:")
        bn = nodescoll[2]  # C
        en = nodescoll[2]  # C

        routes = routing(bn, en, nodescoll)
        route_u30 = []
        for route in routes:
            if route.return_totdistance() < 30:
                route_u30.append([route, True])

        x = len(route_u30)

        for a in range(3):
            for i, route in enumerate(routes):
                # if route_u30[3 * a + i][1] == True:
                routetest = route_u30[0][0] + route
                # print(routetest.return_totdistance())
                if routetest.return_totdistance() < 30:
                    route_u30.append([routetest, True])
                else:
                    route_u30.append([routetest, False])
                    x -= 1
            print(a)
            a = a + 1
        # print(route_u30)
        # print(len(routes))

        # print(route_u30)
        route_u30_2 = []
        for r in route_u30:
            if r[1] == True:
                # r[0].print_stops()
                route_u30_2.append(r)

        print(len(route_u30_2))
        time.sleep(1)  # xx

        # for range(3):
        #    for range(3)

        # route_u30 = []
