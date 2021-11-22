import os
import sys
from math import sqrt

def check_enhance(input_file, output_file):

    with open(input_file, 'r') as file:
        input_points = set()
        for index,line in enumerate(file.readlines()):
            if index == 0:
                first_line = [int(i) for i in line.split(' ')]
                for n_index, n in enumerate(first_line):
                    if n_index == 2:
                        D = int(n)
            else:
                r,c = [int(i) for i in line.split(' ')]
                input_points.add((r,c))

    with open(output_file, 'r') as file:
        output_points = set()
        C = 0
        for index,line in enumerate(file.readlines()):
            if index == 0:
                try:
                    int(line)
                except:
                    return False
            else:
                try:
                    r1,c1,r2,c2 = [int(i) for i in line.split(' ')]
                    output_points.add((r1,c1))
                    output_points.add((r2,c2))
                    C += sqrt((r1 - r2)**2 + (c1 - c2)**2)
                except:
                    return False

    
    for point in input_points:
        if point not in output_points:
            return -1

    return (1 - C/D) # enhance percentage


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python3 minspan.py input_file output_file')
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    if not os.path.isfile(input_file):
        print('Error: input file not found')
        sys.exit(1)
    if not os.path.isfile(output_file):
        print('Error: output file not found')
        sys.exit(1)
    enhance = check_enhance(input_file, output_file)
    if enhance == -1:
        print('Error: Output no contiene los nodos originales')
        sys.exit(1)
    print(check_enhance(input_file, output_file))