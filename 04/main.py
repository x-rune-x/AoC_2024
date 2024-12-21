def part1(word_search: list[str], keyword: str) -> int:
    y_range = len(word_search)
    x_range = len(word_search[0])
    word_length = len(keyword)
    total = 0

    for i in range(y_range): # Move through the matrix, scanning for the word XMAS in all directions from each element.
        for j in range(x_range):
            dist_to_north = i
            dist_to_east = x_range - j - 1
            dist_to_north_east = min(dist_to_north, dist_to_east)
            dist_to_south = y_range - i - 1
            dist_to_south_east = min(dist_to_south, dist_to_east)
            dist_to_west = j
            dist_to_south_west = min(dist_to_south, dist_to_west)
            dist_to_north_west = min(dist_to_north, dist_to_west)            

            if word_search[i][j] == keyword[0]:
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


def part2(word_search: list[str], keyword: str) -> int:
    reversed_keyword = keyword[::-1]
    keyword_middle_index = int(len(keyword) / 2) # Assuming keyword has odd length.
    y_range = len(word_search) - keyword_middle_index # Restrict seraching the matrix to an inner boundary
    x_range = len(word_search[0]) - keyword_middle_index #  since it will be impossible for the X to be formed outsdie of this area.
    word_length = len(keyword)
    total = 0

    for i in range(keyword_middle_index, y_range):
        for j in range(keyword_middle_index, x_range):        
            if word_search[i][j] == keyword[keyword_middle_index]:
                x1 = ''.join([word_search[i - keyword_middle_index + z][j - keyword_middle_index + z] for z in range(word_length)])
                x2 = ''.join([word_search[i + keyword_middle_index - z][j - keyword_middle_index + z] for z in range(word_length)])

                if (x1 == keyword or x1 == reversed_keyword) and (x2 == keyword or x2 == reversed_keyword):
                    total += 1                

    return total


def main():
    with open("04/input_04.txt") as f: lines = [line.strip() for line in f]
    print(part1(lines, "XMAS"))
    print(part2(lines, "MAS"))
    
if __name__ == "__main__":
    main()
