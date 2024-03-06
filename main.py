from service import get_links_from_url, get_domain_name


def print_links(links: set, indent: int):
    whitespace = ' '*indent
    for link in links:
        print(f'{whitespace}{link}')


# def main(url: str, depth: int = 3, indent: int = 0):
#     while depth > 1:
#         links = get_links_from_url(url=url)
#         whitespace = ' ' * indent
#         print(f'{whitespace}{url}: ')
#
#         depth -= 1
#         indent += 5
#
#         if not links or depth == 1:
#             print_links(links=links, indent=indent)
#             break
#
#         for link in links:
#             main(url=link, depth=depth, indent=indent)
#         depth = 1
#

def main(url: str, depth: int = 3, indent: int = 0):
    stack = [(url, depth, indent)]

    while stack:
        url, depth, indent = stack.pop()
        links = get_links_from_url(url=url)
        whitespace = ' ' * indent
        print(f'{whitespace}{url}: ')
        depth -= 1
        indent += 5

        if not links or depth == 1:
            print_links(links=links, indent=indent)
            continue

        for link in links:
            stack.append((link, depth, indent))


if __name__ == '__main__':
    main(url='https://transfonter.org/')
    main('https://avocode.com/')

