from dataclasses import dataclass
from sympy import sin, cos, pi, Expr


@dataclass(frozen=True)
class NavPoint:
    position: tuple[int, int]
    direction: Expr

def find_initial_position_of_guard(area_map: list[list[str]]) -> tuple[int, int]:
    # Assuming guard always starts facing up.

    for i, row in enumerate(area_map):
        for j, position in enumerate(row):
            if position == "^":
                return (i, j)
    
    raise Exception("A guard was not present")


def part1(area_map: list[list[str]]) -> int:
    current_pos = find_initial_position_of_guard(area_map)
    current_direction = pi/2
    visited_positions = {current_pos} # Use set to prevent from counting positions the guard has already been to twice. 

    while True:
        current_pos = (current_pos[0] - sin(current_direction), current_pos[1] + cos(current_direction))
        if current_pos[0] < 0 or current_pos[0] >= len(area_map) or current_pos[1] < 0 or current_pos[1] >= len(area_map[0]):
            break # The guard has exited the boundary of the mapped area.

        if area_map[current_pos[0]][current_pos[1]] == "#":
            current_pos = (current_pos[0] + sin(current_direction), current_pos[1] - cos(current_direction)) # Hit obstacle so have to go back one step.
            current_direction -= (pi/2) # Direction of guard rotates 90 degrees clockwise when they hit an obstacle.
        else:
            visited_positions.add(current_pos)
    
    return len(visited_positions)


def part2(area_map: list[list[str]]) -> int:
    number_of_obstacles_to_place = 0

    current_pos = find_initial_position_of_guard(area_map)
    current_dir = pi / 2
    visited_points = [NavPoint(current_pos, current_dir)]

    # Get all points on the initial path excluding points adjacent to an existing obstacle.
    while True:
        current_pos = (current_pos[0] - sin(current_dir), current_pos[1] + cos(current_dir))

        if current_pos[0] < 0 or current_pos[0] >= len(area_map) or current_pos[1] < 0 or current_pos[1] >= len(area_map[0]):
            break # The guard has exited the boundary of the mapped area.
        elif area_map[current_pos[0]][current_pos[1]] == "#":
            current_pos = (current_pos[0] + sin(current_dir), current_pos[1] - cos(current_dir)) # Hit obstacle so have to go back one step.
            current_dir = (current_dir - (pi / 2)) % (2 * pi) # Direction of guard rotates 90 degrees clockwise when they hit an obstacle.
            visited_points.pop() # Remove the previous visited point since there is no point placing an obstacle on an existing obstacle.
        else:
            visited_points.append(NavPoint(current_pos, current_dir))

    for point in visited_points:
        print(point.position, point.direction)

    for point in visited_points:
        print(point.position, point.direction, "------------------------------")
        current_pos = point.position
        current_dir = (point.direction - (pi / 2)) % (2 * pi)

        divergent_visited_points = []

        while True:           
            current_pos = (current_pos[0] - sin(current_dir), current_pos[1] + cos(current_dir))

            if NavPoint(current_pos, current_dir) == point or NavPoint(current_pos, current_dir) in divergent_visited_points:
                number_of_obstacles_to_place += 1
                break
            elif current_pos[0] < 0 or current_pos[0] >= len(area_map) or current_pos[1] < 0 or current_pos[1] >= len(area_map[0]):
                break
            elif area_map[current_pos[0]][current_pos[1]] == "#":
                current_pos = (current_pos[0] + sin(current_dir), current_pos[1] - cos(current_dir))
                current_dir = (current_dir - (pi / 2)) % (2 * pi)
            else:
                divergent_visited_points.append(NavPoint(current_pos, current_dir))

    return number_of_obstacles_to_place


def main():
    with open("06/input_06.txt") as f: area_map = [line.strip() for line in f]
    # print(part1(area_map))
    print(part2(area_map))


if __name__ == "__main__":
    main()