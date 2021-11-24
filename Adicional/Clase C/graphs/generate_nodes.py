from os import name
import random
import sys

def generate_nodes(num_nodes):
    """
    Generate random 2-D nodes
    """
    nodes = []
    for i in range(num_nodes):
        nodes.append((random.randint(0, 100), random.randint(0, 100)))
    return nodes

def save_nodes(nodes, output_file):
    with open(output_file, 'w') as f:
        f.write(f"{len(nodes)}\n")
        for node in nodes:
            f.write(f"{node[0]} {node[1]}\n")

def check_nodes():
    try:
        num_nodes = int(sys.argv[1])
    except ValueError:
        print("Number of nodes must be an integer")
        sys.exit(1)
    if num_nodes < 1:
        print("Number of nodes must be greater than 0")
        sys.exit(1)
    return num_nodes

def parse_input():
    """
    Check if program args are valid
    """
    if len(sys.argv) != 3:
        print("Usage: python generate_nodes.py <number of nodes> <output file>")
        sys.exit(1)
    num_nodes = check_nodes()
    return num_nodes, sys.argv[2]

def main():
    num_nodes, output_file = parse_input()
    nodes = generate_nodes(num_nodes)
    save_nodes(nodes, output_file)


if __name__ == "__main__":
    main()

