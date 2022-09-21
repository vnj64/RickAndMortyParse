import requests
from bs4 import BeautifulSoup as bs4

def fun(URL_TEMPLATE):
    response = requests.get(URL_TEMPLATE)
    soup = bs4(response.text, 'lxml')
    quotes = soup.find_all('div', class_='Lyrics__Container-sc-1ynbvzw-6 YYrds')

    text = open('SONG_LYRICS.txt', 'w')
    for quote in quotes:
        text.write(quote.text)
    text.close()


fun('https://genius.com/S-maksim-do-you-know-lyrics')


# name track