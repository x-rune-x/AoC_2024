def part1(word_search: list[str], keyword: str) -> int:
    y_range = len(word_search)
    x_range = len(word_search[0])
    word_length = len(keyword)
    total = 0

    for i in range(y_range):
        for j in range(x_range):
            dist_to_north = i
            dist_to_east = x_range - j - 1
            dist_to_north_east = min(dist_to_north, dist_to_east)
            dist_to_south = y_range - i - 1
            dist_to_south_east = min(dist_to_south, dist_to_east)
            dist_to_west = j
            dist_to_south_west = min(dist_to_south, dist_to_west)
            dist_to_north_west = min(dist_to_north, dist_to_west)            

            if word_search[i][j] == "X":
                if dist_to_north >= word_length - 1:
                    total += 1 if ''.join([word_search[i - z][j] for z in range(word_length)]) == keyword else 0
                if dist_to_north_east >= word_length - 1:
                    total += 1 if ''.join([word_search[i - z][j + z] for z in range(word_length)]) == keyword else 0
                if dist_to_east >= word_length - 1:
                    total += 1 if ''.join([word_search[i][j + z] for z in range(word_length)]) == keyword else 0
                if dist_to_south_east >= word_length - 1:
                    total += 1 if ''.join([word_search[i + z][j + z] for z in range(word_length)]) == keyword else 0
                if dist_to_south >= word_length - 1:
                    total += 1 if ''.join([word_search[i + z][j] for z in range(word_length)]) == keyword else 0
                if dist_to_south_west >= word_length - 1:
                    total += 1 if ''.join([word_search[i + z][j - z] for z in range(word_length)]) == keyword else 0
                if dist_to_west >= word_length - 1:
                    total += 1 if ''.join([word_search[i][j - z] for z in range(word_length)]) == keyword else 0
                if dist_to_north_west >= word_length - 1:
                    total += 1 if ''.join([word_search[i - z][j - z] for z in range(word_length)]) == keyword else 0

    return total


def main():
    with open("04/input_04.txt") as f: lines = [line.strip() for line in f]
    print(part1(lines, "XMAS"))
    
if __name__ == "__main__":
    main()


