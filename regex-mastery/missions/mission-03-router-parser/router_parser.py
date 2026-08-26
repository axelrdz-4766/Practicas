import re

def main():
    print(parse_route(input("Route -> ")))

def parse_route(route):
    match = re.fullmatch(r'(GET|POST|PUT|DELETE) /([a-z]+)(?:/([0-9]+))?', route)

    if not match:
        raise ValueError
    
    dic_route = {
        "method": match.group(1),
        "resource": match.group(2),
        "id": match.group(3)
        }
    return dic_route

if __name__ == "__main__":
    main()