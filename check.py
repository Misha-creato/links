import re


PATTERN_STR = r'^https?:\/\/(.*\.)*(.*\.\w+)'


def check_url(url: str):
    if re.match(pattern=PATTERN_STR, string=url):
        return True
    return False


def is_link_internal(link: str, root_domain_name: str):
    if root_domain_name in link:
        return True
    return False


def is_link_equal_root_url(link: str, root_url: str):
    if link == root_url:
        return True
    return False
