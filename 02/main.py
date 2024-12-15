def check_report_is_safe(report: list) -> bool:
    increasing = True if report[0] < report[1] else False

    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]

        if (diff > 0) is not increasing:
            return False

        if not ( 0 < abs(diff) < 4):
            return False

    return True


def check_report_with_error_is_safe(report: list) -> bool:
    for i in range(len(report)):
        levels = report.copy()
        levels.pop(i)

        if check_report_is_safe(levels):
            return True
    
    return False       


def part1(reports: list):    
    return len([report for report in reports if check_report_is_safe(report)])

def part2(reports: list):
    reports_with_no_error, reports_with_errors = [], []

    for report in reports:
        if check_report_is_safe(report):
            reports_with_no_error.append(report)
        else:
            reports_with_errors.append(report)

    reports_with_one_error = [report for report in reports_with_errors if check_report_with_error_is_safe(report)]

    return len(reports_with_no_error) + len(reports_with_one_error)


def get_reports(report: str):
    report_as_list = report.split(" ")

    return [int(x) for x in report_as_list]


def main():
    with open("input_02.txt") as f: lines = [line.strip() for line in f]
    reports = list(map(get_reports, lines))

    print(part1(reports))
    print(part2(reports))
    

if __name__ == "__main__":
    main()
