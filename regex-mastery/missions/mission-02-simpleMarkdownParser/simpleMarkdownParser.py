import re

def main():
    print(parse_markdown(input("Inp -> ")))

def parse_markdown(text):
    match = re.fullmatch(r'(\*\*|__|\*|_)([^\*_]|[^\*_].*)\1', text)

    if not match:
        raise ValueError

    return match.group(2)

if __name__ == "__main__":
    main()