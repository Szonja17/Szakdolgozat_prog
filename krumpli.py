import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.kozertplusz.hu/burgonya"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

# Keresd meg az összes h2 címet és a hozzájuk tartozó árat
all_h2 = soup.find_all("h2", class_="product-title")
all_divs = soup.find_all("div", class_="base-price-pangv")

# Ellenőrizd, hogy azonos számú cím és ár van-e
if len(all_h2) == len(all_divs):
    # Hozz létre egy üres DataFrame-t a pandas segítségével
    data = {"NÉV": [], "ÁR": []}

    for i in range(len(all_h2)):
        product_name = all_h2[i].string.strip()
        product_price = all_divs[i].text.strip()

        # Adj hozzá egy új sor az adatokhoz
        data["NÉV"].append(product_name)
        data["ÁR"].append(product_price)

    # Hozz létre egy DataFrame-t a pandas segítségével
    df = pd.DataFrame(data)

    # Mentés Excel-fájlba
    df.to_excel("termek_lista.xlsx", index=False)

    print("Az adatok el lettek mentve az 'termek_lista.xlsx' Excel-fájlba.")
else:
    print("Hiba: Az összes termék neve és ára nem egyezik meg.")