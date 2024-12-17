import re
import math


def sum_valid_multiples(corrupted_code: str) -> int:
    regex = r"mul\(([0-9]|[a1-9][0-9]|[a1-9][0-9][0-9]),([0-9]|[a1-9][0-9]|[a1-9][0-9][0-9])\)"
    valid_multiples = re.findall(regex, corrupted_code)
    total = 0

    for multiple in valid_multiples:      
        numbers = [int(num) for num in multiple]
        total += math.prod(numbers)

    return total


def find_enabled_code(corrupted_code: str) -> str:
    enabled = True
    enabled_code = ""

    for i, c in enumerate(corrupted_code):
        if corrupted_code[i:i + 4] == "do()":
            enabled = True
        elif corrupted_code[i:i + 7] == "don't()":
            enabled = False

        if enabled:
            enabled_code += c

    return enabled_code


def part2(corrupted_code: str) -> int:
    enabled_code = find_enabled_code(corrupted_code)

    return sum_valid_multiples(enabled_code)


def part1(corrupted_code: str) -> int:
    return sum_valid_multiples(corrupted_code)


def main():
    with open("03/input_03.txt") as f: memory_text = f.read()
    print(part1(memory_text))
    print(part2(memory_text))  


if __name__ == "__main__":
    main()
