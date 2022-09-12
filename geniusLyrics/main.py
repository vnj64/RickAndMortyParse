import requests
from bs4 import BeautifulSoup as bs4

def fun(URL_TEMPLATE):
    big_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    small_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    response = requests.get(URL_TEMPLATE)
    soup = bs4(response.text, 'lxml')
    quotes = soup.find_all('div', class_='Lyrics__Container-sc-1ynbvzw-6 YYrds')

    text = open('DOMINO.txt', 'w')
    for quote in quotes:
        text.write(quote.text)
    text.close()


    with open('DOMINO.txt', 'r') as file:
        for line in file:
            for letter in range(len(line)):
                if (line[letter] in small_alphabet) and (line[letter + 1] in big_alphabet):
                    space = ' '
                    line = line.replace(line[letter], line[letter] + space)
                else:
                    return None
    file.close()

fun('https://genius.com/Face-dominoes-lyrics')
