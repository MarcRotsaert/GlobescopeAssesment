from rf_input import (
    Node,
    Edge,
    Nodescoll,
)


# import time
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


class Rfinder:
    def __init__(self, graphdefs: list):
        # MAIN FUNCTION2
        # args
        # graphdefs: list
        self.nodescoll = Nodescoll(graphdefs)
        self.routes_d = None
        self.routes_e = None

        # nodescoll, nodeorder, bn, en = init_findroute_extend(graphdefs, bn, en, args)
        # self.nodescoll = nodescoll

    def clean_routes(self):
        self.routes_d = None
        self.routes_e = None

    # def _init_findroute_extend(self, bn: str, en: str, args=[]):  ##kwargs: dict):
    def _init_findroute_extend(self, nodeorder: list):

        bn = self.nodescoll.letter2node(nodeorder[0])
        en = self.nodescoll.letter2node(nodeorder[-1])

        routes_d = routing(bn, en, self.nodescoll)
        if len(nodeorder) > 2:
            self.routes_d = findcorrectroutes(routes_d, nodeorder)
        else:
            self.routes_d = routes_d

        self.routes_e = routing(en, en, self.nodescoll)

    def return_nosuchroute(self) -> str:
        output = "No Such Route"
        self.clean_routes()
        print("No Such Route")
        return output

    def return_shortestdistance(self, nodeorder: list) -> float:
        self._init_findroute_extend(nodeorder)
        if len(self.routes_d) == 0:
            output = self.return_nosuchroute()
        else:
            distance = 999
            for route in self.routes_d:
                temp = route.return_totdistance()
                distance = min(temp, distance)
            output = distance
        return output

    # def count_routesmaxstop(routes_d: list, routes_e: list, maxstops: int) -> int:
    def return_countmaxstops(self, nodeorder: list, maxstops: int) -> int:
        self._init_findroute_extend(nodeorder)
        if len(self.routes_d) == 0:
            output = self.return_nosuchroute()
        else:
            output = 0
            for route1 in self.routes_d:
                nrstop1 = route1.return_nrstops()
                if nrstop1 < maxstops + 1:
                    output += 1
                for route2 in self.routes_e:
                    nrstop12 = nrstop1 + route2.return_nrstops()
                    if nrstop12 < maxstops + 1:
                        output += 1
        return output

    # def count_routesnrstop(routes_d: list, routes_e: list, nrstops: int) -> int:
    def return_countnrstops(self, nodeorder: list, nrstops: int) -> int:
        self._init_findroute_extend(nodeorder)
        if len(self.routes_d) == 0:
            output = self.return_nosuchroute()
        else:
            output = 0
            for route1 in self.routes_d:
                nrstop1 = route1.return_nrstops()
                if nrstop1 == nrstops:
                    output += 1
                for route2 in self.routes_e:
                    nrstop12 = nrstop1 + route2.return_nrstops()
                    if nrstop12 == nrstops:
                        output += 1
            return output

    def return_countmaxdist(self, nodeorder: list, maxdist: float) -> float:
        self._init_findroute_extend(nodeorder)
        route_u = []
        for route in self.routes_d:
            if route.return_totdistance() < maxdist:
                route_u.append(route)

        x1 = 0
        x2 = len(route_u)
        while x2 > x1:
            k = 0
            for a in range(x1, x2):
                for route in self.routes_e:
                    routetest = route_u[a] + route
                    if routetest.return_totdistance() < maxdist:
                        route_u.append(routetest)
                        k += 1
            x1 = x2
            x2 = x1 + k
        output = len(route_u)
        return output


def routing(beginnode: Node, endnode: Node, nodescoll: Nodescoll, maxroutes=20) -> list:
    # Make possible and impossible routes based on beginnode, endnode and collection of nodes
    # Input:
    #   beginnode: beginning node (Node-object)
    #   endnode: endnode           (Node-object)
    #   nodes: collection of nodes. list of nodes

    # Output:
    # routes list of lists
    #   routes[x]= routes[x][0] =>list nodes-edge;
    #   routes[x][1] => False= route continues; True = routes ends

    def addnode2route(route: Route) -> (Route, Node):
        node = route.route[-1].find_connectednode(nodes, "in")
        route.route.append(node)
        return route, node

    def check_endroute(node: Node, endnode: Node) -> bool:
        return node.name == endnode.name

    nodes = nodescoll.return_nodes()
    # initiate routes
    routes = []
    routes.append(Route([beginnode]))

    i = 0  # Route teller
    while i <= len(routes) - 1:

        route = routes[i]
        if type(route.route[-1]) is Edge:
            route, node = addnode2route(route)
            if check_endroute(node, endnode):
                route.end = True  # end of route at destination
                i += 1
                continue

        altroutes = route.add_toroute()
        routes.extend([Route(ro) for ro in altroutes])
        route, node = addnode2route(route)

        if route.check_nodereoccurance():
            i += 1  # ends not at destination
            continue
        if check_endroute(node, endnode):
            route.end = True  # end of route at destination
            i += 1

        if len(routes) == i or i == maxroutes:
            print(i)
            break
    return routes


def findcorrectroutes(routesin: list, nodeorder: list) -> list:
    # filter routes in list that contain correct order of nodes.
    # input:    routesin => list of Route-objects
    #           nodeorder => list of Nodes-objects.
    # output:
    #           list of Routes
    routesout = []
    for route in routesin:
        res = route.check_nodesorder(nodeorder)
        if res:
            routesout.append(route)
    return routesout


if __name__ == "__main__":
    graphdefs = ["AB5", "BC4", "CD8", "DC8", "DE6", "AD5", "CE2", "EB3", "AE7"]

    if True:
        print("______")
        print("Question 1:")
        bn = "A"  # A
        en = "C"  # C
        kwargs = {"intern": ["B"]}
        args = ["shortest"]
        init_findroute_extend
        Rfinder()

        findroute_extend(bn, en, graphdefs, *args, **kwargs)
        xx
    if True:
        print("______")
        print("Question 2:")
        # Question 2

        bn = "A"  # A
        en = "D"  # D

        args = ["shortest"]
        findroute_extend(bn, en, graphdefs, *args)

    if True:
        print("______")
        print("Question 3:")
        # Question 3
        bn = "A"  # A
        en = "C"  # C
        args = ["shortest"]
        kwargs = {"intern": "D"}
        findroute_extend(bn, en, graphdefs, *args, **kwargs)

    if True:
        print("______")
        print("Question 4:")
        # Question 4
        bn = "A"  # A
        en = "D"  # C

        args = ["shortest"]
        kwargs = {"intern": ["E", "B", "C"]}
        findroute_extend(bn, en, graphdefs, *args, **kwargs)

    if True:
        print("______")
        print("Question 5:")
        # Question 5
        bn = "A"  # A
        en = "D"  # D
        args = ["shortest"]
        kwargs = {"intern": "E"}
        findroute_extend(bn, en, graphdefs, *args, **kwargs)

    if False:
        print("______")
        print("Question 6:")
        bn = "C"  # C
        en = "C"  # C

        args = ["shortest"]
        kwargs = {"maxstops": 3}
        findroute_extend(bn, en, graphdefs, **kwargs)

    if False:
        print("______")
        print("Question 7:")
        bn = "A"  # C
        en = "C"  # C
        kwargs = {"nrstops": 4}
        findroute_extend(bn, en, graphdefs, **kwargs)

    if False:
        print("______")
        print("Question 8:")

        bn = "A"  # A
        en = "C"  # C

        args = ["shortest"]
        findroute_extend(bn, en, graphdefs, *args)

    if False:
        print("______")
        print("Question 9:")
        bn = "B"  # B
        en = "B"  # B
        args = ["shortest"]
        findroute_extend(bn, en, graphdefs, *args)

    if False:
        print("Question 10:")
        bn = "C"  # C
        en = "C"  # C
        kwargs = {"maxdist": 30}
        findroute_extend(bn, en, graphdefs, **kwargs)

    if False:
        print("Question 11:")
        bn = "B"  # C
        en = "C"  # C
        kwargs = {"maxdist": 70}
        findroute_extend(bn, en, graphdefs, **kwargs)

    if False:
        print("______")
        print("Question 12:")
        bn = "A"  # C
        en = "C"  # C
        kwargs = {"nrstops": 6}
        findroute_extend(bn, en, graphdefs, **kwargs)

    if False:
        graphdefs.extend(["FG2"])
        bn = "C"  # C
        en = "G"  # C
        args = ["shortest"]
        findroute_extend(bn, en, graphdefs, *args)
        kwargs = {"maxdist": 30}
        findroute_extend(bn, en, graphdefs, **kwargs)
