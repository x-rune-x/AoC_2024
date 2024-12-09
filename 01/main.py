def part1(location_ids1: list, location_ids2: list):  
    location_ids1.sort()
    location_ids2.sort()

    differences = [abs(i - j) for i, j in zip(location_ids1, location_ids2)]

    return sum(differences)


def part2(location_ids1: list, location_ids2: list):
    occurrences1 = get_number_of_occurences(location_ids1)
    occurrences2 = get_number_of_occurences(location_ids2)
    similarities = [num * occ * (occurrences2[num] if num in occurrences2 else 0) for num, occ in occurrences1.items()]

    return sum(similarities)


def get_number_of_occurences(locations: list) -> dict:
    number_of_occurences = {}

    for num in locations:
        if num in number_of_occurences:
           number_of_occurences[num] += 1
        else:
           number_of_occurences[num] = 1
    
    return number_of_occurences


def main():
    list1 = []
    list2 = []

    with open("input_01.txt") as f:
        for line in f:
            values = line.split("   ")
            list1.append(int(values[0]))
            list2.append(int(values[1]))
    
    print(part1(list1, list2))
    print(part2(list1, list2))


if __name__ == "__main__":
    main()