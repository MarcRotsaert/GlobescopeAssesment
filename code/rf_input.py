# import copy
# import pprint as pp


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


class Route:
    def __init__(self, route: list):
        self.route = route
        self.end = False

    def __add__(self, route: list):
        # Extend route by adding extra route informatie at end of route attribute
        routeori = self.route
        routeadd = route.route[1:]
        r1 = Route(routeori + routeadd)
        return r1

    def return_nrstops(self) -> int:
        # return number of nodes in route.
        count = 0
        for elem in self.route[1:]:
            if type(elem) == Node:
                count += 1
        return count

    def return_totdistance(self) -> int:
        # return total distance of a route
        dist = 0
        for elem in self.route:
            if type(elem) == Edge:
                dist += elem.weight
        return dist

    def print_stops(self) -> None:
        # print name of nodes on screen
        stops = []
        for elem in self.route:
            if type(elem) == Node:
                stops.append(elem.name)
        print(stops)

    def check_nodereoccurance(self) -> bool:
        # Check if last node in route already exists route
        # Input: Route-object
        # Output:  Bool, True= last node is passed previous on route
        checknode = self.route[-1]
        result = False
        for elem in self.route[:-1]:
            if elem == checknode:
                result = True
        return result

    def check_nodesorder(self, nodenames: list) -> bool:
        # Check if nodes in route are also present in input
        # input: nodesnames list of strings.
        if self.return_nrstops() != len(nodenames) - 1:
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

    def add_toroute(self) -> list:
        # Add edge to last node in route or start alternative route
        # Input:  routes => list of routes
        altroutes = []
        node = self.route[-1]
        for j, edge in enumerate(node.edgeout):
            if j < 1:
                self.route.append(edge)
            else:
                # start alternative route
                tempcopy = [elem for elem in self.route[:-1]]
                altroutes.append(tempcopy)

                altroutes[-1].append(node.edgeout[j])
        return altroutes


class Nodescoll:
    def __init__(self, graphdefs):
        self.nodescoll = self._make_nodescoll(graphdefs)

    def return_nodes(self):
        return self.nodescoll

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
            for i, no in enumerate(nodescoll):
                if no.name == dump[0]:
                    no.add_edgeout(e_1)
                elif no.name == dump[1]:
                    no.add_edgein(e_1)
        return nodescoll

    def letter2node(self, letter: str) -> Node:
        # Return Node- object from a list of Node objects by letter
        # input: letter => letter from alphabet, str.
        #       nodescoll: list of nodeobjects
        # output: Nodeobject
        nodeobj = None
        i = 0
        while nodeobj == None:
            if letter == self.nodescoll[i].name:
                nodeobj = self.nodescoll[i]
            i += 1
        return nodeobj


def make_nodeorder(bn: str, en: str, args=[]) -> list:
    # make list of strings representing nodes
    # kwargs: 'intern': list of points

    nodeorder = [bn]

    if len(args) != 0:
        for nn in args[0]:
            nodeorder.append(nn)
    nodeorder.append(en)
    return nodeorder


# def init_findroute_extend(graphdefs: list, bn: str, en: str, *args):  ##kwargs: dict):
#     nodescoll = Nodescoll(graphdefs)
#     nodeorder = make_nodeorder(bn, en, args)
#     bn = nodescoll.letter2node(nodeorder[0])
#     en = nodescoll.letter2node(nodeorder[-1])
#     return nodescoll, nodeorder, bn, en


if __name__ == "__main__":
    print("niet uitgewerkt")
