import copy


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


def find_node(sel, nodes):
    node = (None,)
    tel = 0
    while node == None:
        if nodes[tel] == sel:
            sel = nodes[tel]
        tel += 1
    return node


def routing(beginnode, endnode, nodes):
    routes = []
    routes.append([[beginnode], False])

    i = 0  # Route teller
    node = beginnode
    # beginnode
    if node.edgeout == []:
        routes[0][1] = True

    tempcopy = copy.deepcopy(routes[i])
    # tempcopy = routes[i].copy()
    for j in range(len(node.edgeout)):
        if j < 1:
            routes[i][0].append(node.edgeout[j])
        else:
            routes.append(tempcopy)
            routes[-1][0].append(node.edgeout[j])

    edgein = routes[i][-1]
    for no in nodes:
        if edgein == no.edgein:
            routes[-1]

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


def main():
    edgedefs = ["AB5", "BC4", "CD8", "DC8", "DE6", "AD5", "CE2", "EB3", "AE7"]
    nodescoll = []
    for temp in edgedefs:
        dump = decode_edge(temp)
        e_1 = Edge(dump[0] + dump[1], dump[2])
        # e_1 = Edge(dump[0] + dump[1], dump[2])
        # dump = decode_edge(routes[1])
        # e_2 = Edge(dump[0] + dump[1], dump[2])
        if len(nodescoll) == 0:
            n1 = Node(dump[0])
            n1.add_edgeout(e_1)
            nodescoll.append(n1)
            n2 = Node(dump[1])
            n2.add_edgeout(e_1)
            nodescoll.append(n2)
            # nodescoll.append(Node(dump[1]))
        else:
            for i, no in enumerate(nodescoll):
                if no.name == dump[0]:
                    no.add_edgeout(e_1)
                    break
            for i, no in enumerate(nodescoll):
                if no.name == dump[1]:
                    no.add_edgein(e_1)
                    break
                if i == len(nodescoll) - 1:
                    no = Node(dump[1])
                    no.add_edgein(e_1)
                    nodescoll.append(Node(dump[1]))
            # print(nodescoll)
            print(nodescoll)
            # for i in nodescoll:
            #    print(i.edgeout)
            for i in nodescoll:
                print(i.edgein)
            print(len(nodescoll))

    # xx
    myroutes = routing(nodescoll[0], nodescoll[1], nodescoll)
    print(myroutes)
    xx
    # nA = Node("A")
    # nB = Node("B")
    # nC = Node("C")

    nA.add_edgeout(e_1)
    nB.add_edgein(e_1)
    nB.add_edgeout(e_2)
    nC.add_edgein(e_2)

    # e = Edge(dump[0] + dump[1], dump[2])
    # e.add_edgein(dump[0])
    # e.add_edgeout(dump[1])
    # print(e.edgein)
    # print(e.edgeout)

    if False:
        trein = Train(nA)
        trein.changeposition(nB)
        trein.changeposition(nC)
        trein.print_distance()

    ro = routing(nA, nC, [nA, nB, nC])
    print(ro)


if __name__ == "__main__":
    main()
