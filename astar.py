import json
import pprint as pp
import math

class StarSolver():
    graph = {}

    def get_node_with_min_f_score(node_set):
        min_value = math.Inf
        best_node = None
        for n in node_set.values():
            if n.f_score < min_value:
                best_node = n
                min_value = n.f_score
        return best_node

    def solveTheMaze(self, start_node, goal_node):
        closed_set = {}
        open_set = {start_node}

        # gScore[start] := 0 
        start_node.exact_cost_to = math.inf

        # // For each node, the total cost of getting from the start node to the goal
        # // by passing by that node. That value is partly known, partly heuristic.
        # fScore := map with default value of Infinity
        # // For the first node, that value is completely heuristic.
        # fScore[start] := heuristic_cost_estimate(start, goal)
        start_node.f_score = heuristic_cost_estimate(start_node, goal_node)

        # while openSet is not empty
        while open_set != {}:
            current_node = get_node_with_min_f_score(open_set)
        #     current := the node in openSet having the lowest fScore[] value
            if current_node.id == goal_node.id:
                return reconstruct_path(current_node)
        #     if current = goal
        #         return reconstruct_path(cameFrom, current)

        #     openSet.Remove(current)
        #     closedSet.Add(current)
        #     for each neighbor of current
        #         if neighbor in closedSet
        #             continue		// Ignore the neighbor which is already evaluated.
        #         // The distance from start to a neighbor
        #         tentative_gScore := gScore[current] + dist_between(current, neighbor)
        #         if neighbor not in openSet	// Discover a new node
        #             openSet.Add(neighbor)
        #         else if tentative_gScore >= gScore[neighbor]
        #             continue		// This is not a better path.

        #         // This path is the best until now. Record it!
        #         cameFrom[neighbor] := current
        #         gScore[neighbor] := tentative_gScore
        #         fScore[neighbor] := gScore[neighbor] + heuristic_cost_estimate(neighbor, goal)

        # return failure


    def heuristic_cost_estimate(self, neighbor, goal):
        pass

    def read_maze_file(self, filename):
        with open(filename) as input:
            graph_json = json.load(input)
            for n in graph_json["nodes"]:
                self.graph[n["id"]] = GraphNode(n["id"], n["pos"][0], n["pos"][1], n["neighbors"])
    
    def print_graph_to_text(self):
        for node in self.graph.values():
            print("node %d: " % node.id)
            print("  x: %d, y: %d" % (node.x, node.y))
            print("  neighbors: ", end="")
            pp.pprint(node.neighbors)


class GraphNode:

    def __init__(self, id, x, y, neighbors):
        self.id = id
        self.x = x
        self.y = y
        self.neighbors = neighbors
        self.came_from = None
        self.exact_cost_to = math.inf
        self.f_cost = math.inf
    
    def set_came_from(self, came_from):
        self.came_from = came_from
    
    def set_exact_cost_to(self, exact_cost_to):
        self.exact_cost_to = exact_cost_to


if __name__ == "__main__":
    ss = StarSolver()
    ss.read_maze_file('input_1.json')
    ss.print_graph_to_text()
