import requests
from bs4 import BeautifulSoup
import csv
CSV = 'Products.csv'
HOST = 'https://shymkent.instashop.kz//'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}
URL = ["0 - nonFood", "1 - Б-химия", "2 - Напитки", "3 - Овощи", "4 - Бакалея", "5 - Молочный", "6 - Акций"]
print(URL)
i = int(input())
if i == 0:
    URL = 'https://shymkent.instashop.kz/store/metro-sh/64176/'
    CSV = 'metro-nonfood'
if i == 1:
    URL = 'https://shymkent.instashop.kz/store/metro-sh/64195/'
    CSV = 'metro-himya.csv'
if i == 2:
    URL = 'https://shymkent.instashop.kz/store/metro-sh/64195/'
    CSV = 'Juise.csv'
if i == 3:
    URL = 'https://shymkent.instashop.kz/store/metro-sh/64255/'
    CSV = 'metro-vegetables.csv'
if i == 4:
    URL = 'https://shymkent.instashop.kz/store/metro-sh/64187/'
    CSV = 'metro-bakaleya.csv'
if i == 5:
    URL = 'https://shymkent.instashop.kz/store/metro-sh/64182/'
    CSV = 'metro-milk.csv'
if i == 6:
    URL = 'https://shymkent.instashop.kz/store/metro-sh/discount/'
    CSV = 'Discount.csv'
if i >= 7:
    print("error")
def parse():
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 'b-product-list__product-info')
    products = []

    for item in items:
        products.append({
            'title': item.find('div', class_ = 'b-product-list__product-name').get_text(strip = True),
            'price': item.find('div', class_ = 'b-product-list__price').get_text(strip = True)
            # 'link':  item.find('span', class_ = 'b-discount-info').get_text(strip = True)
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
        writer = csv.writer(csvfile, delimiter = ';')
        writer.writerow(['Название', 'Цена'])
        for item in items:
            writer.writerow([item['title'], item['price']])
parse()