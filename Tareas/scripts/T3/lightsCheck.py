import sys

def check_correctness(output_file, original_positions):
    obtained_positions, cost = get_positions(output_file)
    for element in original_positions:
        if element not in obtained_positions:
            print(f"Error: {element} not in obtained_positions")
            return 0, False
    return cost, True

def get_positions(input_file):
    positions = set()
    cost = 0
    line = True
    with open(input_file, "r") as f:
        while line != "":
            line = f.readline()
            position_x, colour_x, position_y, colour_y = line.split(" ")
            position_x, position_y = int(position_x), int(position_y)
            positions.add(position_x)
            positions.add(position_y)
            cost += abs(position_y - position_x)
    return positions, cost

def fetch_without_colour(input_file, colour):
    positions = set()
    line = True
    with open(input_file, "r") as f:
        while line != "":
            line = f.readline()
            position_x, colour_x, position_y, colour_y = line.split(" ")
            position_x, position_y = int(position_x), int(position_y)
            if colour_x != colour and colour_x != colour:
                positions.add(position_x)
                positions.add(position_y)
    return positions

def check_valid(input_file):
    position_B = fetch_without_colour(input_file, "B")
    position_R = fetch_without_colour(input_file, "R")
    return position_B, position_R

def check_strong_connections(positionsR, positionsB, original_positions):
    for element in original_positions:
        if element not in positionsB and element not in positionsR:
            print(f"Error: {element} no esta conectado dada las condiciones del problema")
            return False
    return True

def fetch_original_positions(input_file):
    original_positions = set()
    line = True
    with open(input_file, "r") as f:
        while line != "":
            line = f.readline()
            position, colour = line.split(" ")
            position = int(position)
            original_positions.add(position)
    return original_positions

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    original_positions = fetch_original_positions(input_file)
    cost, output = check_correctness(output_file, original_positions)
    if output:
        print(f"Output pose los mismos elementos de input con costo: {cost}")
    else:
        print(f"Output pose diferentes elementos que el input")

    position_B, position_R = check_valid(output_file)
    if check_strong_connections(position_R, position_B, original_positions):
        print("Output es Correcto")
    else:
        print("Output es Incorrecto")
    return
    
def check_params():
    if len(sys.argv) < 3:
        print("Usage: python check_lights.py <input_file> <output_file>")
        sys.exit(1)

if __name__ == "__main__":
    check_params()
    # Falta añadir comparacion con target cost
    main()
