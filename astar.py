import json
import pprint as pp
import math

#Authors: Evan Bluhm, Alex French, Elizabeth Gass, Samuel Gass, Margaret Yim

class StarSolver():
    graph = {}
    start_node = None
    goal_node = None

    def solve_the_maze(self, start_node, goal_node):
        #self.print_node_set(self.graph)
        closed_set = {} # nodes already evaluated
        open_set = {start_node.id: start_node} # discovered nodes, not yet evaluated
        
        # initial values for start node
        # cost from start to start is zero
        # cost from start to goal is completely heuristic
        start_node.cost_to = 0
        start_node.cost_thru = self.heuristic_cost_estimate(start_node, goal_node)
        
        while open_set:
        
            current_node = self.find_node_with_min_thru_cost(open_set)
            if current_node.id == goal_node.id:
                return self.reconstruct_path(current_node)

            open_set.pop(current_node.id, None)
            closed_set[current_node.id] = current_node
            
            for n in current_node.neighbors:
                if n in closed_set:
                    continue # ignore neighbor if already evaluted
                    
                neighbor = self.graph[n]
                tentative_n_to_cost = current_node.cost_to + current_node.neighbors[n]
                if n not in open_set:
                    open_set[n] = neighbor
                elif tentative_n_to_cost >= neighbor.cost_to:
                    continue # this is not a better path

                # this is the best path found so far!
                neighbor.came_from = current_node
                neighbor.cost_to = tentative_n_to_cost
                neighbor.cost_thru = neighbor.cost_to + self.heuristic_cost_estimate(neighbor, goal_node)

        pp.pprint("Error: No path from node %d to node %d." % (start_node.id, goal_node.id))

    def heuristic_cost_estimate(self, node, goal):
        return math.sqrt(math.pow(goal.x - node.x,2) + math.pow(goal.y - node.y,2))

    def find_node_with_min_thru_cost(self, node_set):
        min_value = math.inf
        min_node = None
        for n in node_set.values():
            if n.cost_thru < min_value:
                min_node = n
                min_value = n.cost_thru
        return min_node

    def reconstruct_path(self, node):
        path = str(node.id)
        while node != self.start_node:
            node = node.came_from
            path = str(node.id) + " -> " + path
        print(path)

    def read_maze_file(self, filename):
        with open(filename) as input:
            graph_json = json.load(input)
            for n in graph_json["nodes"]:
                new_node = GraphNode(n["id"], n["pos"][0], n["pos"][1], n["neighbors"])
                self.graph[str(n["id"])] = new_node
                if n["id"] == graph_json["start"]:
                    self.start_node = new_node
                if n["id"] == graph_json["goal"]:
                    self.goal_node = new_node
    
    def print_node_set(self, node_set):
        for node in node_set.values():
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
        self.cost_to = math.inf
        self.cost_thru = math.inf


if __name__ == "__main__":
    ss = StarSolver()
    ss.read_maze_file('input_1.json')
    ss.solve_the_maze(ss.start_node, ss.goal_node)
