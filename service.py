import requests
from bs4 import BeautifulSoup
import tldextract


def get_links_from_url(url: str):
    response = requests.get(url)
    internal_links = set()
    root_domain_and_suffix = get_domain_and_suffix(url=url)

    response_html = BeautifulSoup(response.text, 'html.parser')
    all_link_tags = response_html.find_all('a')
    for link_tag in all_link_tags:
        link = link_tag.get('href')
        if is_link_internal(link=link, domain_and_suffix=root_domain_and_suffix):
            internal_links.add(link)
    return internal_links


def is_link_internal(link: str, domain_and_suffix: tuple):
    if link and (link.startswith('/') or get_domain_and_suffix(url=link) == domain_and_suffix):
        return True


def check_url():
    pass


def get_domain_and_suffix(url: str):
    extracted_data = tldextract.extract(url)
    return extracted_data.domain, extracted_data.suffix



