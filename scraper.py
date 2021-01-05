import requests
import random
import time
from bs4 import BeautifulSoup


class Scraper(object):
    '''
    Scraper utility class to fetch recipes from TheKitchn
    '''

    def __init__(self):
        ''' Global variables '''
        self.sitemap = 'https://www.thekitchn.com/sitemap.xml'
        self.httpheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
        self.timeout = 0.5

    def get_soup(self, url):
        ''' Fetch html and parse to soup '''
        time.sleep(random.random() * self.timeout)

        page = requests.get(url, headers=self.httpheaders)
        soup = BeautifulSoup(page.text, 'html.parser')

        if page.status_code != 200:
            print('Error: {} status returned from {}'.format(
                page.status_code, url))
            raise Exception
        return soup

    def get_children(self):
        ''' Retrieve child xml sitemaps from root '''
        soup = self.get_soup(self.sitemap)
        children = list(map(lambda x: x.find(text=True), soup.find_all('loc')))
        children.pop(0)  # remove head containing sitemap
        return children

    def get_urls(self, page=None):
        ''' Retrieve urls from single or all sitemaps '''
        children = self.get_children()
        urls = []

        if page is not None:
            soup = self.get_soup(children[page])
            urls.extend(list(map(lambda x: x.find(text=True), soup.find_all('loc'))))
        else:
            for child in children:
                soup = self.get_soup(child)
                urls.extend(list(map(lambda x: x.find(text=True), soup.find_all('loc'))))

        return urls

    def get_recipe(self):
        return

    def get_ingredients(self):
        return

    def get_rating(self, url):
        return


if __name__ == '__main__':
    scraper = Scraper()
    urls = scraper.get_urls(page=0)
    print(urls)
