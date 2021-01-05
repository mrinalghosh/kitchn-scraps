import requests
import random, time
from bs4 import BeautifulSoup


class Review(object):
    '''
    Review class with utility functions to parse recipes from TheKitchn
    '''

    def __init__(self):
        self.page_root = ''

    def get_recipe_urls(self):
        return

    def get_recipe(self):
        return

    def get_ingredients(self):
        return

    def get_rating(self):
        return


if __name__ == '__main__':
    sitemap = 'https://www.thekitchn.com/sitemap.xml'
    httpheaders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    html = requests.get(sitemap, headers=httpheaders)
    soup = BeautifulSoup(html.text, 'html.parser')
    
    """  extract all xml tags  """
    children = list(map(lambda x: x.find(text=True), soup.find_all('loc')))
    print(children)