from sympy import sin, cos, pi

def find_initial_position_of_guard(area_map: list[list[str]]) -> tuple[int, int]:
    # Assuming guard always starts facing up.

    for i, row in enumerate(area_map):
        for j, position in enumerate(row):
            if position == "^":
                return (i, j)
    
    raise Exception("A guard was not present")


def part1(area_map):
    current_pos = find_initial_position_of_guard(area_map)
    current_direction = pi / 2
    count = 1

    while True:
        current_pos = (current_pos[0] - sin(current_direction), current_pos[1] + cos(current_direction))
        if current_pos[0] < 0 or current_pos[0] >= len(area_map) or current_pos[1] < 0 or current_pos[1] >= len(area_map[0]):
            break # The guard has exited the boundary of the mapped area.

        if area_map[current_pos[0]][current_pos[1]] == "#":
            current_pos = (current_pos[0] + sin(current_direction), current_pos[1] - cos(current_direction)) # Hit obstacle so have to go back
            current_direction -= (pi / 2) # Direction of guard rotates 90 degrees clockwise when they hit an obstacle.
        else:
            count += 1
    
    return count


def main():
    with open("06/test_06.txt") as f: area_map = [line.strip() for line in f]
    print(part1(area_map))



if __name__ == "__main__":
    main()