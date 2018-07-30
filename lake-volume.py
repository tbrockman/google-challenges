# https://techdevguide.withgoogle.com/paths/advanced/volume-of-water/#!

import sys

def calculate_forward_pass(heights):
    max = 0
    max_idx = 0
    potential_vol = 0
    aggregate_vol = 0

    for i, height in enumerate(heights):

        if (height < max):
            potential_vol += max - height

        if (height >= max):
            max = height
            max_idx = i
            aggregate_vol += potential_vol
            potential_vol = 0

    return aggregate_vol, max_idx

def calculate_lake_volume(heights):
    # perform one full forward pass, keeping track of the index of the maximal element
    forward_volume, max_idx = calculate_forward_pass(heights)
    # perform a pass on reverse list sliced to maximal element
    # trading some memory for readability and code reuse
    backward_volume, __ = calculate_forward_pass(reversed(heights[max_idx:]))
    return forward_volume + backward_volume

def process_height_input(input):
    heights = []

    for line in input:
        i = 0
        integer = 0

        while i < len(line):
            char = line[i]

            if char.isdigit():
                integer = integer * 10 + int(char)
            elif char == ',' or char == ']':
                heights.append(integer)
                integer = 0
            i += 1

    return heights

if __name__ == "__main__":
    heights = process_height_input(sys.stdin)
    volume = calculate_lake_volume(heights)
    print(volume)
