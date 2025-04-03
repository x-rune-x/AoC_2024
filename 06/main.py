def find_initial_position_of_guard(area_map: list[list[str]]) -> tuple[int, int]:
    # Assuming guard always starts facing up.

    for i, row in enumerate(area_map):
        for j, position in enumerate(row):
            if position == "^":
                return (i, j)
    
    raise Exception("A guard was not present")

def part1(area_map):
    current_pos = find_initial_position_of_guard(area_map)
    count = 1

    while (current_pos[0] > -1 and current_pos[0] < len(area_map)) and (current_pos[1] > -1 and current_pos[1] < len(area_map[0])):
        x = 1
    
    return count


def load_input(input_path):
    with open(input_path) as f: area_map = [line for line in f]

    return area_map


def main():
    area_map = load_input("input.txt")



if __name__ == "__main__":
    main()