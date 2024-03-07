from service import get_links_from_url
import argparse
from check import check_url


def get_arguments():
    parser = argparse.ArgumentParser(description='Links tree')
    parser.add_argument(
        'url',
        type=str,
        help='Input url'
    )
    parser.add_argument(
        'depth',
        type=int,
        default=3,
        nargs='?',
        help='Input depth'
    )
    args = parser.parse_args()
    return args.url, args.depth


def print_links(links: set, indent: int):
    whitespace = ' ' * indent
    for link in links:
        print(f'{whitespace}{link}')


def main_loop(url: str, depth: int, links_black_list: set = None, indent: int = 0):
    if links_black_list is None:
        links_black_list = set()
    while depth > 1:
        links_black_list.add(url)
        links = get_links_from_url(url=url)
        links.difference_update(links_black_list)
        links_black_list.update(links)

        whitespace = ' ' * indent
        print(f'{whitespace}{url}: ')

        depth -= 1
        indent += 5

        if not links or depth == 1:
            print_links(links=links, indent=indent)
            break

        for link in links:
            main_loop(url=link, depth=depth, indent=indent, links_black_list=links_black_list)
        depth = 1


def main(url: str, depth: int):
    if check_url(url):
        main_loop(url=url, depth=depth)
    else:
        print('Invalid url')


if __name__ == '__main__':
    url, depth = get_arguments()
    main(url=url, depth=depth)

