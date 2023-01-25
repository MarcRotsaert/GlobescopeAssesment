class Edge:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    def find_connectednode(self, nodes: list, inout: str):
        # search node-object, connected to this Edge-object
        # input: nodes  list of Node objects
        # inout: "in" or "out"
        for no in nodes:
            if inout == "in":
                for ed in no.edgein:
                    # print(ed.name)
                    if ed.name == self.name:
                        noderes = no
            if inout == "out":
                pass  # not yet implemented
        return noderes


class Node:
    def __init__(self, name: str):
        self.name = name
        self.edgein = []
        self.edgeout = []

    def add_edgein(self, edge: Edge) -> None:
        # add Edge to attribute edgein
        # input: Edge-Object
        self.edgein.append(edge)

    def add_edgeout(self, edge: Edge) -> None:
        # add Edge to attribute edgeout
        # input: Edge-Object
        self.edgeout.append(edge)


class Nodescoll:
    def __init__(self, graphdefs: list):
        self.nodescoll = self._make_nodescoll(graphdefs)

    def return_nodebyletter(self, letter):
        nodeobj = None
        for node in self.nodescoll:
            if node.name == letter:
                nodeobj = node
                break
        return nodeobj

    def _make_nodescoll(self, graphdefs: list) -> list:
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
            for no in nodescoll:
                if no.name == dump[0]:
                    no.add_edgeout(e_1)
                elif no.name == dump[1]:
                    no.add_edgein(e_1)
        return nodescoll

    def return_nodes(self):
        return self.nodescoll


def letter2node(letter: str, nodescoll: Nodescoll) -> Node:
    # Return Node- object from a nodescoll object by letter
    # input: letter => letter from alphabet, str.
    #       nodescoll: list of nodeobjects
    nodeobj = nodescoll.return_nodebyletter(letter)
    return nodeobj


def make_nodeorder(bn: str, en: str, nodescoll: Nodescoll, intern=None) -> list:
    # make list of nodeobjects representing stops in route
    nodeorder = [letter2node(bn, nodescoll)]
    # if len(args) != 0:
    if intern is not None:
        for nn in intern:
            nodeorder.append(letter2node(nn, nodescoll))
    nodeorder.append(letter2node(en, nodescoll))
    return nodeorder


if __name__ == "__main__":
    print("niet uitgewerkt")
