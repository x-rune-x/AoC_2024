def order_pages(order_rules: list[tuple[int]]) -> list:
    page_order = []

    for rule in order_rules:
        if rule[0] not in page_order:
            page_order.append(rule[0])

        if rule[1] not in page_order:
            page_order.append(rule[1])

        index1 = page_order.index(rule[0])
        index2 = page_order.index(rule[1])
        if index1 > index2:
            section = page_order[index2 + 1:index1 + 1]
            del page_order[index2 + 1:index1 + 1]
            page_order = page_order[:index2] + section + page_order[index2:]

    return page_order


def check_pages_are_in_order(page_order: list, update_pages: list) -> bool:    
    page_order = [page for page in page_order if page in update_pages]
    for page in update_pages:
        if update_pages.index(page) > page_order.index(page):
            return False

    return True


def part1(order_rules: list, updates: list) -> int:
    page_order = order_pages(order_rules)
    correctly_ordered_updates = [update for update in updates if check_pages_are_in_order(page_order, update)] 

    return sum([update[len(update) // 2] for update in correctly_ordered_updates])


def process_input(input_path: str):
    with open(input_path) as f: lines = [line.strip() for line in f if line.strip()] # Skip the spare line separating the rules from the updates 

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
    print(part1(input[0], input[1]))

if __name__ == "__main__":
    main()