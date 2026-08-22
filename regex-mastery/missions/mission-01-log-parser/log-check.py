import re

def main():
    print(parse_log(input("Log -> ")))

def parse_log(s):
    match = re.fullmatch(r'\[(INFO|ERROR|WARNING)] (\d{4}-\d{2}-\d{2}) (.+$)', s)

    if not match:
        raise ValueError()

    return {
        "level": match.group(1),
        "date": match.group(2),
        "message": match.group(3)
    }

main()