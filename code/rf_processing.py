from typing import Tuple

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
        routecombined = Route(routeori + routeadd)
        return routecombined

    def return_nrstops(self) -> int:
        # return number of nodes in route.
        count = 0
        for elem in self.route[1:]:
            if isinstance(elem, Node):
                count += 1
        return count

    def return_totdistance(self) -> int:
        # return total distance of a route
        dist = 0
        for elem in self.route:
            if isinstance(elem, Edge):
                dist += elem.weight
        return dist

    def print_stops(self) -> None:
        # print name of nodes in route on screen
        stops = []
        for elem in self.route:
            if isinstance(elem, Node):
                stops.append(elem.name)
        print(stops)

    def check_nodereoccurance(self) -> bool:
        # Check if last node in route already exists route
        # Output:  Bool, True= last node is passed previous on route
        checknode = self.route[-1]
        result = False
        for elem in self.route[:-1]:
            if elem == checknode:
                result = True
        return result

    def check_nodesorder(self, nodeorder: list) -> bool:
        # Check if nodes in route are also present in input
        # input: nodesnames list of strings.
        if self.return_nrstops() != len(nodeorder) - 1:
            return False
        i = 0
        for elem in self.route:
            if isinstance(elem, Node):
                if elem.name == nodeorder[i].name:
                    i += 1
                else:
                    return False
        if i == len(nodeorder):
            return True
        else:
            return False


class Rfinder:
    # Several functions for answering questions about routes
    def __init__(self, graphdefs: list):
        # graphdefs: list
        self.nodescoll = Nodescoll(graphdefs)
        self.routes_d = None
        self.routes_e = None

    def _clean_routes(self):
        self.routes_d = None
        self.routes_e = None

    def _init_findroute_extend(self, nodeorder: list):
        self.routes_d = routing(nodeorder, self.nodescoll)
        en = nodeorder[-1]
        nodeorder_ext = [en, en]
        self.routes_e = routing(nodeorder_ext, self.nodescoll)

    def _nosuchroute(self, count) -> str:
        if count == 0:
            output = "No Such Route"
            self._clean_routes()
            # print("No Such Route")
        else:
            output = count
        return output

    def return_shortestdistance(self, nodeorder: list) -> float:
        # return distance of shortest route in nodeorder
        self._init_findroute_extend(nodeorder)
        output = self._nosuchroute(len(self.routes_d))
        if output != "No Such Route":
            distance = 999
            for route in self.routes_d:
                temp = route.return_totdistance()
                distance = min(temp, distance)
            output = distance
        return output

    def return_countmaxstops(self, nodeorder: list, maxstops: int) -> int:
        # return number of routes wich equals or less than maxstops in nodeorder
        self._init_findroute_extend(nodeorder)
        count = 0
        for route1 in self.routes_d:
            nrstop1 = route1.return_nrstops()
            if nrstop1 < maxstops + 1:
                count += 1
            for route2 in self.routes_e:
                nrstop12 = nrstop1 + route2.return_nrstops()
                if nrstop12 < maxstops + 1:
                    count += 1

        output = self._nosuchroute(count)
        return output

    def return_countnrstops(self, nodeorder: list, nrstops: int) -> int:
        # return number of routes that equals number of stops in nrstops in nodeorder
        self._init_findroute_extend(nodeorder)
        count = 0
        for route1 in self.routes_d:
            nrstop1 = route1.return_nrstops()
            if nrstop1 == nrstops:
                count += 1
            for route2 in self.routes_e:
                nrstop12 = nrstop1 + route2.return_nrstops()
                if nrstop12 == nrstops:
                    count += 1
        output = self._nosuchroute(count)
        return output

    def return_countmaxdist(self, nodeorder: list, maxdist: float) -> float:
        # return number of routes with distance less than maxdist in nodeorder
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

        count = len(route_u)
        output = self._nosuchroute(count)
        return output


def routing(nodeorder: list, nodescoll: Nodescoll, maxroutes=20) -> list:
    # Create possible routes based on beginnode, endnode out of collection of nodes-objects
    # Input:
    #   nodeorder: order of stops in route)
    #   nodescoll: collection of nodes. list of nodes

    # Output:
    # routes list of Route-objects
    #   routes[x]= routes[x][0] =>list nodes-edge;
    #   routes[x][1] => False= route continues; True = routes ends

    def addnode2route(route: Route) -> Tuple[Route, Node]:
        # add node to last edge in route and return
        node = route.route[-1].find_connectednode(nodes, "in")
        route.route.append(node)
        return route, node

    def check_endroute(node: Node, endnode: Node) -> bool:
        return node.name == endnode.name

    def add_toroute(route: Route) -> Tuple[Route, list]:
        # Add edge to last node in route or start alternative route
        # Output: altered route and alternative routes.
        altroutes = []
        node = route.route[-1]
        route.route.append(node.edgeout[0])
        for edge in node.edgeout[1:]:
            tempcopy = [elem for elem in route.route[:-1]]
            altroutes.append(tempcopy)
            altroutes[-1].append(edge)
        return route, altroutes

    def findcorrectroutes(routesin: list, nodeorder: list) -> list:
        # filter routes in list that contain correct order of stops.
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

    beginnode = nodeorder[0]
    endnode = nodeorder[-1]

    nodes = nodescoll.return_nodes()
    # initiate routes
    routes = []
    routes.append(Route([beginnode]))
    i = 0
    while i <= len(routes) - 1 or i == maxroutes:

        route = routes[i]
        if isinstance(route.route[-1], Edge):
            route, node = addnode2route(route)
            if check_endroute(node, endnode):
                route.end = True  # end of route at destination
                i += 1
                continue

        route, altroutes = add_toroute(route)
        routes.extend([Route(ro) for ro in altroutes])
        route, node = addnode2route(route)

        if route.check_nodereoccurance():
            i += 1  # ends not at destination
            continue
        if check_endroute(node, endnode):
            route.end = True  # end of route at destination
            i += 1

    if len(nodeorder) > 2:
        routes = findcorrectroutes(routes, nodeorder)

    return routes
