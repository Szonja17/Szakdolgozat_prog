import requests
from bs4 import BeautifulSoup

url = "https://lunys.sk/drogeria-a-domacnost/deodoranty-a-telove-spreje/page/2/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    titles = [title.text.strip() for title in soup.select('.woodetail--title')]
    prices = [price.text.strip() for price in soup.select('.woodetail--price')]

    for title, price in zip(titles, prices):
        print(f"Title: {title}\tPrice: {price}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")