def check_report_is_safe(report: list) -> bool:
    increasing = True if report[0] < report[1] else False

    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]

        if (diff > 0) is not increasing:
            return False

        if not ( 0 < abs(diff) < 4):
            return False

    return True


def part1(reports: list):    
    return len([report for report in reports if check_report_is_safe(report)])


def clean_data(report: str):
    report_as_list = report.split(" ")

    return [int(x) for x in report_as_list]


def main():
    with open("02/test.txt") as f: lines = [line.strip() for line in f]
    reports = list(map(clean_data, lines))

    print(part1(reports))
    

if __name__ == "__main__":
    main()