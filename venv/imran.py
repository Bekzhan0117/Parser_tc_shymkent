import requests
from bs4 import BeautifulSoup
import csv

HOST = 'http://imran.kz/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}
URL = ["0 - Овощи", "1 - Фрукты", "2 - Напитки", "3 - Мясо и рыба", "4 - К Чаю", "5 - Бытовая химия", "6 - Молочные продукты"]
print(URL)
i = int(input())
if i == 0:
    URL = 'http://imran.kz/%D0%BE%D0%B2%D0%BE%D1%89%D0%B8/'
    CSV = 'Vegetable.csv'
if i == 1:
    URL = 'http://imran.kz/tablet/'
    CSV = 'Fruits.csv'
if i == 2:
    URL = 'http://imran.kz/software/'
    CSV = 'Juise.csv'
if i == 3:
    URL = 'http://imran.kz/%D0%BC%D1%8F%D1%81%D0%BE-%D1%80%D1%8B%D0%B1%D0%B0-%D1%88%D1%8B%D0%BC%D0%BA%D0%B5%D0%BD%D1%82/'
    CSV = 'Meats.csv'
if i == 4:
    URL = 'http://imran.kz/%D1%87%D0%B0%D0%B9-%D0%BA%D0%BE%D1%84%D0%B5-%D1%88%D0%BE%D0%BA%D0%BE%D0%BB%D0%B0%D0%B4/'
    CSV = 'Tea.csv'
if i == 5:
    URL = 'http://imran.kz/%D0%B1%D1%8B%D1%82%D0%BE%D0%B2%D0%B0%D1%8F-%D1%85%D0%B8%D0%BC%D0%B8%D1%8F-%D0%B3%D0%B8%D0%B3%D0%B8%D0%B5%D0%BD%D0%B0/'
    CSV = 'Hymia.csv'
if i == 6:
    URL = 'http://imran.kz/%D0%BC%D0%BE%D0%BB%D0%BE%D1%87%D0%BD%D1%8B%D0%B5-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D1%8B%D1%8F%D0%B9%D1%86%D0%B0/?page=1'
    CSV = 'Milk.csv'
if i >= 7:
    print("error")
def parse():
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 'products-item')
    products = []

    for item in items:
        products.append({
            'title': item.find('b', class_ = 'product-item_caption__product-name').get_text(strip = True),
            'price': item.find('p', class_ = 'product-item_prices__price').get_text(strip = True),
            'link':  item.find('div', class_ = 'product-item_image').find('a').get('href')
        })
        save_doc(products,CSV)
    return products

        # for product in products:
        #     print(f'{product["title"]} ; Price: {product["price"]} ; Link: {product["link"]}')
def get_html(url, params = ''):
    r = requests.get(url, headers = HEADERS, params = params)
    return r
def save_doc(items, path):
    with open(path, 'w', newline='', encoding='utf-16') as csvfile:
        writer = csv.writer(csvfile, delimiter = '|')
        writer.writerow(['Название', 'Цена', 'Ссылка'])
        for item in items:
            writer.writerow([item['title'], item['price'], item['link']])
parse()