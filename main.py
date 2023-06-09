import requests
import csv
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
cards = soup.find_all('article', attrs={"class": "product_pod"})

def find_books_on_page(cards):
  books = []

  for card in cards:
    info = {
        "title": card.find('h3').find('a').get('title'),
        "link": url + card.find('h3').find('a').get('href'),
        "picture": url + card.find('img').get('src'),
        "price": card.find('p', attrs={"class": "price_color"}).get_text()[1:],
        "rating": card.find('p', attrs={"class": "star-rating"}).get('class')[1]
    }
    books.append(info)
  return books

books = find_books_on_page(cards)

while True:
  tag_next_link = soup.find('li', attrs={"class": "next"})
  if tag_next_link:
    next_link = tag_next_link.find('a').get('href')
    print(url + next_link)
    page = requests.get(url + next_link)
    url = 'https://books.toscrape.com/catalogue/'
    soup = BeautifulSoup(page.content, "html.parser")
    cards = soup.find_all('article', attrs={"class": "product_pod"})
    books = books + find_books_on_page(cards)
  else:
    break

#print(len(books))

with open("books.csv", "w", newline="") as fd:
    fieldnames = ["title", "link", "picture", "price", "rating"]
    writer = csv.DictWriter(fd, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(books)