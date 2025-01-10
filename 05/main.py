def check_pages_are_in_order(update: list[int], order_rules: list[tuple[int]], verbose: bool = False) -> bool:    
    for rule in order_rules:
        first_num = rule[0]
        second_num = rule[1]
        if first_num in update and second_num in update and update.index(first_num) > update.index(second_num):
            if verbose:
                print(rule)
            return False

    return True


def get_order(order_rules: list[tuple[int]]):
    rule_counts = {}    # Page number with the most rules specifying it has to be before other pages will be the first in the order.
    all_page_nums = []  # Use this to compare with the numbers in the rule counts to find the page number with no rules saying it must be first. 
                        # This will be the last in the order

    for rule in order_rules:
        if rule[0] in rule_counts:
            rule_counts[rule[0]] += 1
        else:
            rule_counts[rule[0]] = 1
        
        if rule[0] not in all_page_nums:
            all_page_nums.append(rule[0])
        if rule[1] not in all_page_nums:
            all_page_nums.append(rule[1])

    final_page = [page for page in all_page_nums if page not in rule_counts][0]
    rule_counts[final_page] = 0
    
    for rule in rule_counts:
        rule_counts[rule] = abs(rule_counts[rule] - (len(all_page_nums) - 1))

    nums = [0 for i in range(len(all_page_nums))]
    for rule in rule_counts:
        nums[rule_counts[rule]] = rule
    
    return nums


def part1(order_rules: list[tuple[int]], updates: list[list[int]]) -> int:
    correctly_ordered_updates = [update for update in updates if check_pages_are_in_order(update, order_rules)]

    return sum([update[len(update) // 2] for update in correctly_ordered_updates])


def part2(order_rules: list[tuple[int]], updates: list[list[int]]):
    order = get_order(order_rules)
    incorrectly_ordered_updates = [update for update in updates if check_pages_are_in_order(update, order_rules) == False]

    total = 0

    for update in incorrectly_ordered_updates:
        middle_page = [page for page in order if page in update][len(update) // 2]
        total += middle_page

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
    input = process_input("05/input_05.txt")
    #print(part1(input[0], input[1]))
    print(part2(input[0], input[1]))

if __name__ == "__main__":
    main()