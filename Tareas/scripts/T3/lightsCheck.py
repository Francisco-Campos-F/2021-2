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
    with open(input_file, "r") as f:
        ammount = int(f.readline().strip("\n"))
        for i in range(ammount):
            line = f.readline()
            if line != "":
                position_x, colour_x, position_y, colour_y = line.split(" ")[0], line.split(" ")[1].strip("\n"), line.split(" ")[2], line.split(" ")[3].strip("\n")
                position_x, position_y = int(position_x), int(position_y)
                positions.add(position_x)
                positions.add(position_y)
                cost += abs(position_y - position_x)
    return positions, cost

def fetch_without_colour(input_file, colour):
    positions = set()
    with open(input_file, "r") as f:
        ammount = int(f.readline().strip("\n"))
        for i in range(ammount):
            line = f.readline()
            if line != "":
                position_x, colour_x, position_y, colour_y = line.split(" ")[0], line.split(" ")[1].strip("\n"), line.split(" ")[2], line.split(" ")[3].strip("\n")
                position_x, position_y = int(position_x), int(position_y)
                if colour_x != colour and colour_y != colour:
                    positions.add(position_x)
                    positions.add(position_y)
    return positions

def check_valid(input_file):
    position_R = fetch_without_colour(input_file, "b")
    position_B = fetch_without_colour(input_file, "r")
    return position_B, position_R

def get_original_positions_by_colour(input_file, colour):
    positions = set()
    with open(input_file, "r") as f:
        ammount = int(f.readline().strip("\n"))
        for i in range(ammount):
            line = f.readline()
            if line != "":
                position_x, colour_x = line.split(" ")[0], line.split(" ")[1].strip("\n")
                position_x = int(position_x)
                if colour_x == colour:
                    positions.add(position_x)
    return positions    
                
def check_strong_connections(positionsR, positionsB, original_positions, input_file):
    positionsr = get_original_positions_by_colour(input_file, "r")
    positionsg = get_original_positions_by_colour(input_file, "g")
    positionsb = get_original_positions_by_colour(input_file, "b")

    positionsb = positionsb.union(positionsg)
    positionsr = positionsr.union(positionsg)

    positionsBb = positionsB.intersection(positionsb)
    positionsRr = positionsR.intersection(positionsr)

    positionr_equal = positionsRr == positionsR
    positionb_equal = positionsBb == positionsB

    if positionr_equal and positionb_equal:
        return True
    print(f"Error: no esta conectado dada las condiciones del problema")
    return False

def fetch_original_positions(input_file):
    original_positions = set()
    line = True
    with open(input_file, "r") as f:
        ammount = int(f.readline().strip("\n"))
        for i in range(ammount):
            line = f.readline()
            if line != "":
                position, colour = line.split(" ")[0], line.split(" ")[1].strip("\n")
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
        return

    position_B, position_R = check_valid(output_file)
    if check_strong_connections(position_R, position_B, original_positions, input_file):
        print("Output es Correcto")
        print("Puntaje NA")
    else:
        print("Output es Incorrecto")
        print("Puntaje 0")
    return
    
def check_params():
    if len(sys.argv) < 3:
        print("Usage: python check_lights.py <input_file> <output_file>")
        sys.exit(1)

if __name__ == "__main__":
    check_params()
    main()
