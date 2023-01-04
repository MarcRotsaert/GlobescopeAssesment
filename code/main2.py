from main import Node, Edge


def make_nodescoll(edgedefs):
    # make colllection (list) of Node-objects.
    # input: edgedefs=> list of strings containing 3 characters.
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


class Route:
    def __init__(self, route):
        self.route = route
        self.end = False

    def return_nrstops(self):
        count = 0
        for elem in self.route:
            if type(elem) == Node:
                count += 1
        return count

    def print_stops(self):
        stops = []
        for elem in self.route:
            if type(elem) == Node:
                stops.append(elem.name)
        print(stops)

    def return_totdistance(self):
        dist = 0
        for elem in self.route:
            if type(elem) == Edge:
                dist += elem.weight
        return dist

    def check_nodereaccurance(self):
        # Check if last node in route already exists route
        # Input: Route-object
        # Output:  Bool
        checknode = self.route[-1]
        result = False
        for elem in self.route[:-1]:
            if elem == checknode:
                result = True
        return result

    def checknodesorder(self, nodenames):
        if self.return_nrstops() != len(nodenames):
            return False
        i = 0
        for elem in self.route:
            if type(elem) == Node:
                if elem.name == nodenames[i]:
                    i += 1
                else:
                    return False
        if i == len(nodenames):
            return True
        else:
            return False
        # return result

    def add_edges(self):
        # Add edge to last node in route
        # Input:  routes => list of routes
        #           i => route to add edges an
        # output: list of routes

        altroutes = []
        node = self.route[-1]
        # tempcopy = copy.deepcopy(routes[i])  # copie to start alternative route
        for j in range(len(node.edgeout)):
            if j < 1:
                self.route.append(node.edgeout[j])
            else:
                # start alternative route
                tempcopy = [elem for elem in self.route[:-1]]
                altroutes.append(tempcopy)
                altroutes[-1].append(node.edgeout[j])
        return altroutes


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
            if node == endnode:
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
        if nodein == endnode:
            route.end = True  # end of route at destination
        if route.end:
            i += 1
        if len(routes) == i:
            # print(i)
            break
        if i == 20:
            break  # emergency break

    return routes


if __name__ == "__main__":
    edgedefs = ["AB5", "BC4", "CD8", "DC8", "DE6", "AD5", "CE2", "EB3", "AE7"]
    nodescoll = make_nodescoll(edgedefs)
    # print(nodescoll)
    # for i in nodescoll:
    #    print(i.edgein)
    # print(len(nodescoll))

    if False:
        bn = nodescoll[0]
        en = nodescoll[2]

        de = routing(bn, en, nodescoll)
        print(de)
        for route in de:
            print(route.return_totdistance())
    if False:
        print("Question 1:")
        # Question 1
        bn = nodescoll[0]  # A
        en = nodescoll[2]  # C

        nodeorder = ["A", "B", "C"]
        routes = routing(bn, en, nodescoll)

        print(routes)
        for route in routes:
            res = route.checknodesorder(nodeorder)
            print(res)
            if res:
                print(route.return_totdistance())
                break
                # xx
    if False:
        print("Question 2:")
        # Question 2
        bn = nodescoll[0]  # A
        en = nodescoll[3]  # D

        routes = routing(bn, en, nodescoll)

        # print(routes)
        distance = 999
        for route in routes:
            temp = route.return_totdistance()
            distance = min(temp, distance)
        print(distance)

    if False:
        print("Question 3:")
        # Question 3
        bn = nodescoll[0]  # A
        en = nodescoll[2]  # C

        nodeorder = ["A", "D", "C"]
        routes = routing(bn, en, nodescoll)

        print(routes)
        for route in routes:
            res = route.checknodesorder(nodeorder)
            print(res)
            if res:
                print(route.return_totdistance())
                break

    if False:
        print("Question 4:")
        # Question 4
        bn = nodescoll[0]  # A
        en = nodescoll[3]  # D
        nodeorder = ["A", "E", "B", "C", "D"]
        routes = routing(bn, en, nodescoll)

        print(routes)
        for route in routes:
            res = route.checknodesorder(nodeorder)
            print(res)
            if res:
                print(route.return_totdistance())
                break

    if False:
        print("Question 5:")
        # Question 5
        bn = nodescoll[0]  # A
        en = nodescoll[3]  # D
        nodeorder = ["A", "E", "D"]
        routes = routing(bn, en, nodescoll)

        print(routes)
        for route in routes:
            route.print_stops()
            res = route.checknodesorder(nodeorder)
            print(res)
            if res:
                print(route.return_totdistance())
                break
        # Nog afmaken

    if False:
        print("Question 6:")
        bn = nodescoll[2]  # C
        en = nodescoll[2]  # C
        routes = routing(bn, en, nodescoll)

        # print(routes)
        result = 0
        for route in routes:
            route.print_stops()
            if route.return_nrstops() < 5:
                # res = route.checknodesorder(nodeorder)
                # print(res)
                result += 1
        print(result)

    if False:
        print("Question 7:")
        bn = nodescoll[0]  # A
        en = nodescoll[2]  # C
        routes1 = routing(bn, en, nodescoll)

        bn = nodescoll[2]  # C
        en = nodescoll[2]  # C
        routes2 = routing(bn, en, nodescoll)

        result = 0
        print("______")
        for route1 in routes1:
            if route1.return_nrstops() == 5:

                route1.print_stops()
                print("______")
                result += 1
            for route2 in routes2:
                temp_nrs = route1.return_nrstops() + route2.return_nrstops()
                if temp_nrs == 6:
                    route1.print_stops()
                    route2.print_stops()
                    print("______")
                    result += 1
                    # res = route.checknodesorder(nodeorder)
                    # print(res)
        print(result)

    if False:
        print("Question 8:")
        bn = nodescoll[0]  # A
        en = nodescoll[2]  # C
        routes = routing(bn, en, nodescoll)

        result = 0
        print("______")
        distance = 999
        for route in routes:
            temp = route.return_totdistance()
            distance = min(temp, distance)
        print(distance)

    if False:
        print("Question 9:")
        bn = nodescoll[1]  # B
        en = nodescoll[1]  # B
        routes = routing(bn, en, nodescoll)

        result = 0
        print("______")
        distance = 999
        for route in routes:
            temp = route.return_totdistance()
            distance = min(temp, distance)
        print(distance)

    if True:
        print("Question 10:")
        bn = nodescoll[2]  # B
        en = nodescoll[2]  # B

        routes = routing(bn, en, nodescoll)
        route_u30 = []
