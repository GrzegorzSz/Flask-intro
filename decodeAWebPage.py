"""
Use the BeautifulSoup and requests Python packages to
print out a list of all the article titles on the New York Times homepage.
"""
import requests, sys
from bs4 import BeautifulSoup

def parseNYT(destFile = sys.stdout):
    """Given file have to be open"""
    url = 'https://www.nytimes.com/'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    h3 = soup.find_all('h1')
    h2 = soup.find_all('h2')

    titles = h2 + h3
    for item in titles:
        print(item.get_text(), file = destFile)

if __name__ == '__main__':
    with open('NYTtitles.txt','w') as destFile:
        parseNYT(destFile)