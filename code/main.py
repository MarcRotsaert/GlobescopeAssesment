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

    def changeposition(self, nieuwnode):
        self.node = nieuwnode
        self.distance += nieuwnode.edgein[0].weight
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


def main():
    routes = ["AB5", "BC4", "CD8", "DC8", "DE6", "AD5", "CE2", "EB3", "AE7"]
    dump = decode_edge(routes[0])

    e_1 = Edge(dump[0] + dump[1], dump[2])
    dump = decode_edge(routes[1])
    e_2 = Edge(dump[0] + dump[1], dump[2])

    nA = Node("A")
    nB = Node("B")
    nC = Node("C")

    nA.add_edgeout(e_1)
    nB.add_edgein(e_1)
    nB.add_edgeout(e_2)
    nC.add_edgein(e_2)

    # e = Edge(dump[0] + dump[1], dump[2])
    # e.add_edgein(dump[0])
    # e.add_edgeout(dump[1])
    # print(e.edgein)
    # print(e.edgeout)

    trein = Train(nA)
    trein.changeposition(nB)
    trein.changeposition(nC)
    trein.print_distance()


if __name__ == "__main__":
    main()
