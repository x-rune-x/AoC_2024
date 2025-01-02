def check_pages_are_in_order(update: list[int], order_rules: list[tuple[int]]) -> bool:    
    for rule in order_rules:
        first_num = rule[0]
        second_num = rule[1]
        if first_num in update and second_num in update and update.index(first_num) > update.index(second_num):
            return False

    return True


def part1(order_rules: list[tuple[int]], updates: list[int]) -> int:
    correctly_ordered_updates = [update for update in updates if check_pages_are_in_order(update, order_rules)]

    return sum([update[len(update) // 2] for update in correctly_ordered_updates])


def part2(order_rules: list[tuple[int]], updates: list[int]):
    incorrectly_ordered_updates = [update for update in updates if check_pages_are_in_order(update, order_rules) == False]

    for update in incorrectly_ordered_updates:
        for rule in order_rules:          
            if rule[0] in update and rule[1] in update and update.index(rule[0]) > update.index(rule[1]):
                num = update.pop(update.index(rule[1]))
                update.insert(update.index(rule[0]) + 1, num)
    
    return sum([update[len(update) // 2] for update in incorrectly_ordered_updates])


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
    input = process_input("05/test_05.txt")
    #print(part1(input[0], input[1]))
    print(part2(input[0], input[1]))

if __name__ == "__main__":
    main()