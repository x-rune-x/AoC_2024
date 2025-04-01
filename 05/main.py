def check_pages_are_in_order(update: list[int], order_rules: list[tuple[int]], verbose: bool = False) -> bool:    
    for rule in order_rules:
        first_num = rule[0]
        second_num = rule[1]
        if first_num in update and second_num in update and update.index(first_num) > update.index(second_num):
            if verbose:
                print(rule)
            return False

    return True


def get_order(order_rules: list[tuple[int]], update: list[int] = None) -> list[int]: 
    # For each number, find all the numbers that it has to go in fron of and put it in front of the first one in the update.
    for page in update:
        rules_with_page_as_first = [rule for rule in order_rules if rule[0] == page]
        minimum_position = update.index(page) if len(rules_with_page_as_first) < 1 else min([update.index(rule[1]) for rule in rules_with_page_as_first])
        
        pos_of_page = update.index(page)
        if pos_of_page > minimum_position:
            # Move the page to the position of the first rule it has to go in front of.
            update.pop(pos_of_page)
            update.insert(minimum_position, page)

    return update


def part1(order_rules: list[tuple[int]], updates: list[list[int]]) -> int:
    correctly_ordered_updates = [update for update in updates if check_pages_are_in_order(update, order_rules)]

    return sum([update[len(update) // 2] for update in correctly_ordered_updates])


def part2(order_rules: list[tuple[int]], updates: list[list[int]]):
    incorrectly_ordered_updates = [update for update in updates if check_pages_are_in_order(update, order_rules) == False]
    total = 0

    for update in incorrectly_ordered_updates:
        relevant_rules = [rule for rule in order_rules if rule[0] in update and rule[1] in update]
        page_order = get_order(relevant_rules, update)

        total += page_order[len(update) // 2]

    return total


def process_input(input_path: str):
    with open(input_path) as f: lines = [line.strip() for line in f if line.strip()] # Use second strip to skip the spare line separating the rules from the updates 

    order_rules, updates = [], []

    for line in lines:
        if "|" in line:
            page_nums  = line.split("|")
            order_rules.append((int(page_nums[0]), int(page_nums[1])))
        else:
            updates.append([int(i) for i in line.split(",")])

    return (order_rules, updates)


def main():
    input = process_input("2024/05/input_05.txt")
    print(part1(input[0], input[1]))
    print(part2(input[0], input[1]))

if __name__ == "__main__":
    main()