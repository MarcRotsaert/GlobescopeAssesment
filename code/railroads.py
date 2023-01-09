import copy
import pprint as pp


class Edge:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    def find_node(self, nodes: list, inout: str):
        # search node-object, connected to edge-object
        # input: nodes  list of Node objects
        # inout: "in" or "out"
        for no in nodes:
            if inout == "in":
                for ed in no.edgein:
                    # print(ed.name)
                    if ed.name == self.name:
                        noderes = no
            if inout == "out":
                pass
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
        # Extend route by adding extra rouappendextend_routete
        routeori = self.route
        routeadd = route.route[1:]
        # self.route.extend(routeadd)
        r1 = Route(routeori + routeadd)
        return r1

    def return_nrstops(self) -> int:
        # return number of nodes in route.
        count = 0
        for elem in self.route:
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

    def checknodesorder(self, nodenames: list) -> bool:
        # Check if nodes in route are also present in input
        # input: list of strings.
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

    def add_edges(self) -> list:
        # Add edge to last node in route
        # Input:  routes => list of routes
        #           i => route to add edges an
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
                # if node.edgeout[j].name == "G":
                #    xx
                altroutes[-1].append(node.edgeout[j])
        return altroutes


if __name__ == "__main__":
    print("niet uitgewerkt")
