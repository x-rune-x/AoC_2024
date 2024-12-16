import re
import math


def part1(corrupted_code: str):
    regex = r"mul\(([0-9]|[a1-9][0-9]|[a1-9][0-9][0-9]),([0-9]|[a1-9][0-9]|[a1-9][0-9][0-9])\)"
    valid_multiples = re.findall(regex, corrupted_code)

    number_regex = r"\d{1,3}"
    total = 0

    for multiple in valid_multiples:      
        numbers = [int(num) for num in multiple]
        total += math.prod(numbers)

    return total


def main():
    with open("03/input_03.txt") as f: memory_text = f.read()
    print(part1(memory_text))    


if __name__ == "__main__":
    main()
