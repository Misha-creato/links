from service import get_links_from_url


def main():
    links = get_links_from_url('https://en.wikipedia.org/wiki/Main_Page')
    print(links)


if __name__ == '__main__':
    main()

