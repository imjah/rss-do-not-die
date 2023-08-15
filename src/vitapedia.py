import requests

WEBSITE_URL="https://vitapedia.pl"

def get_rss():
    pass

def _fetch_sitemap():
    response = requests.get(f'{WEBSITE_URL}/sitemap.xml')

    if response.status_code != 200:
        raise ConnectionError(f'Invalid status [{response.status_code}]')

    return response.text

