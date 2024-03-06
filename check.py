import re


PATTERN_STR = r'^https?:\/\/(.*\.)*(.*\.\w+)'


def check_url(url: str):
    if re.match(pattern=PATTERN_STR, string=url):
        return True


def is_link_internal(link: str, domain_name: str, root_domain_name: str):
    if link and (link.startswith('/') or root_domain_name == domain_name):
        return True


def is_link_equal_root_url(link: str, root_url: str):
    if link == root_url:
        return True

