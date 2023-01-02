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
        pass

    def return_totdistance(self):
        pass

    def checknodesinroute(self):
        # Check if last node in route already exists route
        # Input: Route-object
        # Output:  Bool
        checknode = self.route[-1]
        result = False
        for elem in self.route[:-1]:
            if elem == checknode:
                result = True
        return result

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
                self.route[0].append(node.edgeout[j])
            else:
                # start alternative route
                tempcopy = [elem for elem in self.route[0][:-1]]
                altroutes.append(tempcopy)
                altroutes[-1][0].append(node.edgeout[j])
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
        routes.extend([Routes(ro) for ro in altroutes])
        edgein = route.route[-1]
        nodein = edgein.find_node(nodes, "in")
        # print(i)
        # print(nodein)
        route.route.append(nodein)

        if route.checknodesinroute():
            i += 1  # ends not at destination
            continue
            # route[1] = True
        if nodein == endnode:
            route.end = True  # end of route at destination
        if route.end:
            i += 1
        if len(routes) == i:
            print(i)
            break
        if i == 10:
            break  # emergency break

    return routes


if __name__ == "__main__":
    edgedefs = ["AB5", "BC4", "CD8", "DC8", "DE6", "AD5", "CE2", "EB3", "AE7"]
    nodescoll = make_nodescoll(edgedefs)
    # print(nodescoll)
    # for i in nodescoll:
    #    print(i.edgein)
    # print(len(nodescoll))

    bn = nodescoll[0]
    en = nodescoll[0]

    de = routing(bn, en, nodescoll)
