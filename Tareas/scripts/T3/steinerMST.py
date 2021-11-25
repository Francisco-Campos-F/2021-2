import os
import sys
from math import sqrt

class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.adjacent = []
        self.visited = False
    
    def add_edge(self, node):
        self.adjacent.append(node)
class MST:
    def __init__(self, max_size, target_cost, node_count):
        self.target_cost = target_cost
        self.max_size = max_size
        self.node_count = node_count
        self.edges = []
        self.nodes = []
        self.original_nodes = []
        self.visited_cost = 0

    def add_edge(self, node1, node2):
        self.edges.append((node1, node2))
        self.edges.append((node2, node1))
        node1.add_edge(node2)
        node2.add_edge(node1)
    
    def add_node(self, x, y):
        if x > self.max_size or y > self.max_size:
            print("Node out of bounds")
            sys.exit(1)
        node = Node(id, x, y)
        self.nodes.append(node)
        return node
    
    def add_original_node(self, x, y):
        self.original_nodes.append(Node(x, y))

    def get_node(self, x, y):
        for node in self.nodes:
            if node.x == x and node.y == y:
                return node
        return None
    
    def manhattan_distance(self, node1, node2):
        return abs(node1.x - node2.x) + abs(node1.y - node2.y)

    def iterative_dfs_with_costs(self):
        stack = []
        stack.append(self.nodes[0])
        self.nodes[0].visited = True
        self.visited_cost = 0
        while stack:
            node = stack.pop()
            for adjacent_node in node.adjacent:
                if not adjacent_node.visited:
                    stack.append(adjacent_node)
                    adjacent_node.visited = True
                    self.visited_cost += self.manhattan_distance(adjacent_node, node)
        return self.visited_cost
    
    def check_if_connected(self):
        for node in self.nodes:
            if not node.visited:
                return False
        return True

    def includes_original_nodes(self):
        original_nodes = set(self.original_nodes)
        visited_nodes = set(self.nodes)
        return original_nodes.issubset(visited_nodes)
    

def parse_input():
    if len(sys.argv) != 3:
        print("Usage: python3 steinerMST.py <input_file> <student_file>")
        exit(1)
    input_file = sys.argv[1]
    student_file = sys.argv[2]
    valid_files = os.path.isfile(input_file) and os.path.isfile(student_file)
    if not valid_files:
        print("Error: Input files are not valid")
        exit(1)
    return input_file, student_file

def main():
    input_file, student_file = parse_input()
    with open(input_file, "r") as f:
        data = f.readline().split()
        max_dimensions = int(data[0])
        node_count = int(data[1])
        target_cost = int(data[2])
        mst = MST(max_dimensions, target_cost, node_count)
        for i in range(node_count):
            data = f.readline().split()
            mst.add_original_node(i, int(data[0]), int(data[1]))

    # output file has instructions for every edge
    # but there new nodes
    with open(student_file, "w") as f:
        # format is a line with the number of edges
        # followed by the edges in format node1.row node1.col node2.row node2.col
        # where node1 and node2 are the nodes in the edge
        # and row and col are the coordinates of the node
        # the first line is the number of edges
        
        #read the number of edges
        num_edges = int(f.readline())
        for i in range(num_edges):
            data = f.readline().split()
            node1 = int(data[1]), int(data[2])
            node2 = int(data[3]), int(data[4])
        
            # add nodes to the mst
            if mst.get_node(node1) is None:
                node1 = mst.add_node(node1[1], node1[2])
                mst.add_node(node1[0], node1[1])
            if mst.get_node(node2) is None:
                mst.add_node(node2[0], node2[1])
            mst.add_edge(mst.get_node(node1), mst.get_node(node2))


            mst.add_edge(node1, node2)


