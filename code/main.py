import copy
import pprint as pp


class Node:
    def __init__(self, name):
        self.name = name
        self.edgein = []
        self.edgeout = []

    def add_edgein(self, edge):
        self.edgein.append(edge)

    def add_edgeout(self, edge):
        self.edgeout.append(edge)


class Edge:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def find_node(self, nodes, inout):
        # nodesres = []
        print("_____________")
        print(self.name)
        print("|||||||||")

        for no in nodes:
            print(no.name)
            if inout == "in":
                for ed in no.edgein:
                    print(ed.name)
                    if ed == self:
                        noderes = no
                # if inout == "out":
                #     if no.edgeout == self:
                #         nodesres.append(no)
        return noderes


class Train:
    def __init__(self, startnode):
        self.node = startnode
        self.distance = 0

    def changeposition(self, nieuwnode, enr=0):
        self.node = nieuwnode
        self.distance += nieuwnode.edgein[enr].weight
        # edgein moet slimmer

    def print_distance(self):
        print(self.distance)


def decode_edge(text):
    edge1, edge2, dump = text
    weight = int(dump)
    return edge1, edge2, weight


def _add_edges(routes, i):
    # Add edge to last node in route
    # Input:  routes => list of routes
    #           i => route to add edges an
    # output: list of routes
    node = routes[i][0][-1]
    # tempcopy = copy.deepcopy(routes[i])  # copie to start alternative route
    for j in range(len(node.edgeout)):
        if j < 1:
            routes[i][0].append(node.edgeout[j])
        else:
            # start alternative route
            tempcopy = [[elem for elem in routes[i][0][:-1]], False]
            routes.append(tempcopy)
            routes[-1][0].append(node.edgeout[j])
    return routes


def checknodesinroute(route):
    # Check if last node in route already exists route
    # Input: Route-object
    # Output:  Bool
    checknode = route[0][-1]
    result = False
    for elem in route[0][:-1]:
        if elem == checknode:
            result = True
    return result


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
    routes.append([[beginnode], False])
    i = 0  # Route teller
    # for a in range(10):
    while i <= len(routes) - 1:
        if type(routes[i][0][-1]) is Edge:
            node = routes[i][0][-1].find_node(nodes, "in")
            routes[i][0].append(node)
            if node == endnode:
                routes[i][1] = True  # end of route at destination
                i += 1
                continue

        routes = _add_edges(routes, i)
        edgein = routes[i][0][-1]
        nodein = edgein.find_node(nodes, "in")
        print(i)
        print(nodein)
        routes[i][0].append(nodein)

        if checknodesinroute(routes[i]):
            routes[i][1] = True  # ends not at destination
        if nodein == endnode:
            routes[i][1] = True  # end of route at destination

        if routes[i][1]:
            i += 1
        if len(routes) == i:
            print(i)
            break
        if i == 10:
            break  # emergency break
    # for in e_out in node.edgeout:
    #    routes[0].append(node.edgeout[0])

    # routes[0][0].append(beginnode)

    # e_out = beginnode.edgeout[0]
    # for no in nodes:
    #     for e_out in no.edgeout:
    #         if e_out.name == e_in.name:
    #             routes[0][0].append(no)
    #             e_out = no.edgein[0]
    #             break

    # e_out = beginnode.edgeout
    # node = beginnode

    # for ed in e_out:
    #     for no in nodes:
    #         if no.edgein==ed
    #            break
    #     node= no
    #     print(node.name)

    return routes


def make_nodescoll(edgedefs):
    # make colllection (list) of Node-objects.
    # input: edgedefs=> list of strings containing 3 characters.
    # output: list of Nodeobjects.
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
                # break
                # if i == len(nodescoll) - 1:
                #    no = Node(dump[1])
                #    no.add_edgein(e_1)
                #    nodescoll.append(Node(dump[1]))
    return nodescoll


def main():
    edgedefs = ["AB5", "BC4", "CD8", "DC8", "DE6", "AD5", "CE2", "EB3", "AE7"]
    nodescoll = make_nodescoll(edgedefs)
    print(nodescoll)
    for i in nodescoll:
        print(i.edgein)
    print(len(nodescoll))

    myroutes = routing(nodescoll[0], nodescoll[1], nodescoll)
    #
    pp.pprint(myroutes)
    if False:
        trein = Train(nA)
        trein.changeposition(nB)
        trein.changeposition(nC)
        trein.print_distance()


if __name__ == "__main__":
    edgedefs = ["AB5", "BC4", "CD8", "DC8", "DE6", "AD5", "CE2", "EB3", "AE7"]
    nodescoll = make_nodescoll(edgedefs)
    # print(nodescoll)
    # for i in nodescoll:
    #    print(i.edgein)
    # print(len(nodescoll))
    if False:
        myroutes = routing(nodescoll[0], nodescoll[2], nodescoll)
        for route in myroutes:
            for elem in route[0]:
                print(elem.name)
            print("+++++++++++++++++++++++++++++++++++++++++")

    myroutes = routing(nodescoll[2], nodescoll[1], nodescoll)
    for route in myroutes:
        print("beginnode:")
        for elem in route[0]:
            print(elem.name)
        print("endnode")
        print("___________________________________________________")

    #
    # pp.pprint(myroutes)

    # main()
