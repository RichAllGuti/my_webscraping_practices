#
import requests 
#
from bs4 import BeautifulSoup
#
target_url = "https://subslikescript.com/movies"

"""
Using the main function here, is for organize the code into logical sections to establish a entry point to the program
and for be the responsable of calling the other functions in a correct order.
"""
def main():
    #
    page = get_page(target_url)
    soup = parse_page(page)
    text_list = find_text_list(soup)
    
    extract_text(text_list)


"""
The use of get_page function is for raise exceptions to the requests.get() method, if there is a HTTP error.
To handle the possibles errors is the call of the method raise_for_status() after the requests.
The raise_for_status() method will raise an exception if the response code is in the 200 to 299 range, which indicates a successful requests.
"""
def get_page(url):
    #
    response = requests.get(url)
    response.raise_for_status()
    
    return response.text

# Just to parse the page information
def parse_page(page):
    #
    return BeautifulSoup(page, 'html.parser')

# This function is for mapping the elements that we want of the url page.
def find_text_list(soup):
    #
    return soup.find('ul', class_ = 'scripts-list')

# Iterate over the text_list elements to extract the information and print it.
def extract_text(text_list):
    #
    for element in text_list.find_all('a'):
        print(f"This is the scripts name: {element.text}")


"""
Wrapping the code in this guard, ensure that the 'main()' function is
only called when the script is run directly as a standalone program.

This is a common convention in python, and is used to make it easier to reuse code across multiple modules.
"""
if __name__ == '__main__':
    main()

