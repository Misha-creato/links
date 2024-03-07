import re
import requests
from bs4 import BeautifulSoup
import check


def get_links_from_url(url: str):
    response = requests.get(url)
    internal_links = set()
    root_domain_name = get_domain_name(url=url)

    response_html = BeautifulSoup(markup=response.text, features='html.parser')
    all_link_tags = response_html.find_all('a')
    for link_tag in all_link_tags:
        link = link_tag.get('href')

        full_link = check_and_return_link(
            link=link,
            root_domain_name=root_domain_name,
            root_url=url
        )

        if full_link:
            internal_links.add(full_link)
    return internal_links


def check_and_return_link(link: str, root_domain_name: str, root_url: str):
    if link and link.startswith('/'):
        link = make_link_from_path(path=link, root_url=root_url)
    if check.is_link_internal(link=link, root_domain_name=root_domain_name):
        if check.is_link_equal_root_url(link=link, root_url=root_url):
            return None
        return link


def get_domain_name(url: str):
    result = re.match(pattern=check.PATTERN_STR, string=url)
    if result:
        return result.group(2)


def make_link_from_path(path: str, root_url: str):
    pattern = f'({check.PATTERN_STR})'
    result = re.match(pattern=pattern, string=root_url)
    link = result.group(1) + path
    return link

