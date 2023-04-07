#
import requests 

from bs4 import BeautifulSoup

target_url = "https://subslikescript.com/movies"

def main():
    page = get_page(target_url)
    soup = parse_page(page)
    text_list = find_text_list(soup)
    extract_text(text_list)

def get_page(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_page(page):
    return BeautifulSoup(page, 'html.parser')

def find_text_list(soup):
    return soup.find('ul', class_ = 'scripts-list')

def extract_text(text_list):
    for element in text_list.find_all('a'):
        print(f"This is the scripts name: {element.text}")

if __name__ == '__main__':
    main()

