from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

s = Service("C:/Users/Tőke Szonja/Desktop/UNI/pythonProject/LearningSelenium/chromedriver.exe")
driver = webdriver.Chrome(service=s)

# Oldal betöltése
driver.get("https://www.roksh.at/hofer/home")

time.sleep(5)

# Cookiek elfogadása
cookie = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[1]/div[5]/div[2]/a[3]'))
)
cookie.click()

time.sleep(5)

# Zöldségek kinyerése
# Zöldségek és gyümölcsök menüpontra való kattintás
vegetablefruit_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[1]'))
)
vegetablefruit_menu.click()

time.sleep(2)
# Zöldségek menüpontra való kattintás
vegetable_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[1]/div/ul/li[1]/div/a'))
)
vegetable_menu.click()

time.sleep(2)
driver.refresh()
time.sleep(2)

# Lefelé görgetés az oldalon
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Várakozás a zöldségek terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[itemprop="name"]'))
)
time.sleep(2)
product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[itemprop="price"]'))
)
time.sleep(2)
# Termékek neveinek és árainak kinyerése
product_name_vegetables = [element.text for element in product_name_elements]
product_price_vegetables = [element.text for element in product_price_elements]

time.sleep(2)

# Gyümölcsök kinyerése
# Gyümölcsök menüpontra való kattintás
fruit_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[1]/div/ul/li[2]/div/a'))
)
fruit_menu.click()

time.sleep(2)

# Lefelé görgetés az oldalon
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Várakozás a gyümölcsök terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[itemprop="name"]'))
)
time.sleep(2)
product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[itemprop="price"]'))
)
time.sleep(2)
# Termékek neveinek és árainak kinyerése
product_name_fruits = [element.text for element in product_name_elements]
product_price_fruits = [element.text for element in product_price_elements]

time.sleep(2)

# Tejek kinyerése
# Tejtermékek menüpontra való kattintás
milk_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[3]/a'))
)
milk_menu.click()

# A "Go to category" ra kattintás
milk_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-product-list-new/div/app-product-group[1]/div/div/div/div/div[1]/a[1]'))
)
milk_menu.click()

# A tejekre kattintás
milks_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-product-list-new/div/app-product-list-header/div[1]/div[2]/div[1]/app-category-card[5]/div/a'))
)
milks_menu.click()

time.sleep(2)

# Lefelé görgetés az oldalon
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Várakozás a tejek terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[itemprop="name"]'))
)
time.sleep(2)
product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[itemprop="price"]'))
)
time.sleep(2)
# Termékek neveinek és árainak kinyerése
product_name_milk = [element.text for element in product_name_elements]
product_price_milk = [element.text for element in product_price_elements]

time.sleep(2)


# Sajtok kinyerése
# A sajtokra kattintás
cheese_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[3]/div/ul/li[2]/div/a'))
)
cheese_menu.click()
time.sleep(2)

# Lefelé görgetés az oldalon
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Várakozás a sajtok terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[itemprop="name"]'))
)
time.sleep(2)
product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[itemprop="price"]'))
)
time.sleep(2)
# Termékek neveinek és árainak kinyerése
product_name_cheese = [element.text for element in product_name_elements]
product_price_cheese = [element.text for element in product_price_elements]
time.sleep(2)

# Vajak kinyerése
# A tejek és tejtermékekre kattintás
milk_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[3]/div/ul/li[1]/div/a'))
)
milk_menu.click()
time.sleep(2)

# A vajakra
butter_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-product-list-new/div/app-product-list-header/div[1]/div[2]/div[1]/app-category-card[5]/div/a/div/span'))
)
butter_menu.click()
time.sleep(2)

# Lefelé görgetés az oldalon
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Várakozás a vajak terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[itemprop="name"]'))
)
time.sleep(2)
product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[itemprop="price"]'))
)
time.sleep(2)
# Termékek neveinek és árainak kinyerése
product_name_butter = [element.text for element in product_name_elements]
product_price_butter = [element.text for element in product_price_elements]
time.sleep(2)

#Tojások kinyerése
# A tojásokra kattintás
egg_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[3]/div/ul/li[5]/div/a'))
)
egg_menu.click()
time.sleep(2)

# Lefelé görgetés az oldalon
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Várakozás a tojások terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[itemprop="name"]'))
)
time.sleep(2)
product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[itemprop="price"]'))
)
time.sleep(2)
# Termékek neveinek és árainak kinyerése
product_name_egg = [element.text for element in product_name_elements]
product_price_egg = [element.text for element in product_price_elements]
time.sleep(2)

#Tészta kinyerése
# A sütésre kattintás
bake_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[5]/a'))
)
bake_menu.click()
time.sleep(2)
# A tésztákra kattintás
pasta_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[5]/div/ul/li[7]/div/a/span'))
)
pasta_menu.click()
time.sleep(2)

# Lefelé görgetés az oldalon
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Várakozás a tészták terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[itemprop="name"]'))
)
time.sleep(2)
product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[itemprop="price"]'))
)
time.sleep(2)
# Termékek neveinek és árainak kinyerése
product_name_pasta = [element.text for element in product_name_elements]
product_price_pasta = [element.text for element in product_price_elements]
time.sleep(2)


# husok kinyerése
# A "Meat, sausages and fish" menüpontra kattintás
meat_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[4]/a'))
)
meat_menu.click()
time.sleep(2)

# Húsok menüpontra kattintás
meat_category_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[4]/div/ul/li[2]/div/a'))
)
meat_category_menu.click()
time.sleep(2)

# Lefelé görgetés az oldalon
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)


# Várakozás a husok terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span[itemprop="name"]'))
)
time.sleep(2)
product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span[itemprop="price"]'))
)
time.sleep(2)
# Termékek neveinek és árainak kinyerése
product_name_meat = [element.text for element in product_name_elements]
product_price_meat = [element.text for element in product_price_elements]
time.sleep(2)

# péksütemények kinyerése
# A "Bread and pastries" menüpontra kattintás
pastries_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[2]/a'))
)
pastries_menu.click()
time.sleep(2)

# Kenyerek menüpontra kattintás
bread_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[2]/div/ul/li[2]/div/a'))
)
bread_menu.click()
time.sleep(2)

# Lefelé görgetés az oldalon
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Lefelé görgetés az oldalon
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Várakozás a kenyerek terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span[itemprop="name"]'))
)
time.sleep(2)
product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span[itemprop="price"]'))
)
time.sleep(2)
# Termékek neveinek és árainak kinyerése
product_name_bread = [element.text for element in product_name_elements]
product_price_bread = [element.text for element in product_price_elements]
time.sleep(2)

# Alkoholok
# A "Italok" menüpontra kattintás
drinks_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[9]/a'))
)
drinks_menu.click()
time.sleep(2)

# Sörök menüpontra kattintás
beer_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[9]/div/ul/li[3]/div/a'))
)
beer_menu.click()
time.sleep(2)

# Lefelé görgetés az oldalon
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Várakozás a sörök terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span[itemprop="name"]'))
)
time.sleep(2)
product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span[itemprop="price"]'))
)
time.sleep(2)
# Termékek neveinek és árainak kinyerése
product_name_beer = [element.text for element in product_name_elements]
product_price_beer = [element.text for element in product_price_elements]
time.sleep(2)

# Higénia
# A "Italok" menüpontra kattintás
beauty_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[10]/a'))
)
beauty_menu.click()
time.sleep(2)

# Care menüpontra kattintás
care_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[10]/div/ul/li[1]/div/a'))
)
care_menu.click()
time.sleep(2)

# Lefelé görgetés az oldalon
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Várakozás a higéniás termékek terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span[itemprop="name"]'))
)
time.sleep(2)
product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span[itemprop="price"]'))
)
time.sleep(2)
# Termékek neveinek és árainak kinyerése
product_name_beauty = [element.text for element in product_name_elements]
product_price_beauty = [element.text for element in product_price_elements]
time.sleep(2)




# Kutatás
csirkemell_products = [(name, price) for name, price in zip(product_name_meat, product_price_meat) if 'hühnchen' and 'filets' in name.lower()]
vaj_products = [(name, price) for name, price in zip(product_name_butter, product_price_butter) if 'butter' in name.lower()]
tojas_products = [(name, price) for name, price in zip(product_name_egg, product_price_egg) if '10' in name]
tej_products = [(name, price) for name, price in zip(product_name_milk, product_price_milk) if 'milch' in name.lower()]
teszta_products = [(name, price) for name, price in zip(product_name_pasta, product_price_pasta) if 'spaghetti' in name.lower()]



# Ha vannak megfelelo termekek, akkor mentés

csirkemell = pd.DataFrame({"Product Name": [item[0] for item in csirkemell_products],
                            "Product Price": [item[1] for item in csirkemell_products]})
vaj = pd.DataFrame({"Product Name": [item[0] for item in vaj_products],
                            "Product Price": [item[1] for item in vaj_products]})
tojas = pd.DataFrame({"Product Name": [item[0] for item in tojas_products],
                            "Product Price": [item[1] for item in tojas_products]})
tej = pd.DataFrame({"Product Name": [item[0] for item in tej_products],
                            "Product Price": [item[1] for item in tej_products]})
teszta = pd.DataFrame({"Product Name": [item[0] for item in teszta_products],
                            "Product Price": [item[1] for item in teszta_products]})

# Mentés külön munkalapra
with pd.ExcelWriter("kutatas_au.xlsx", engine="xlsxwriter") as writer:
    csirkemell.to_excel(writer, sheet_name="Chicken breast", index=False)
    vaj.to_excel(writer, sheet_name="Butter", index=False)
    tojas.to_excel(writer, sheet_name="Egg", index=False)
    tej.to_excel(writer, sheet_name="Milk", index=False)
    teszta.to_excel(writer, sheet_name="Pasta", index=False)

# WebDriver leállítása
driver.quit()

# Adatok összefűzése
product_name_all = (product_name_vegetables + product_name_fruits + product_name_bread + product_name_beer + product_name_beauty)
product_price_all = (product_price_vegetables + product_price_fruits + product_price_bread + product_price_beer + product_price_beauty)

# Ellenőrzés: azonos hosszúságú-e a termékek neveinek és árainak listája
if len(product_name_all) == len(product_price_all):
    # Adatkeretek létrehozása
    df_all = pd.DataFrame({"Product Name": product_name_all, "Product Price": product_price_all})

    # Adatkeretek mentése külön munkalapokra egyetlen Excel fájlban
    with pd.ExcelWriter("products_austria.xlsx", engine="xlsxwriter") as writer:
        df_vegetables = df_all[df_all["Product Name"].isin(product_name_vegetables)]
        df_fruits = df_all[df_all["Product Name"].isin(product_name_fruits)]
        df_bread = df_all[df_all["Product Name"].isin(product_name_bread)]
        df_beer = df_all[df_all["Product Name"].isin(product_name_beer)]
        df_beauty = df_all[df_all["Product Name"].isin(product_name_beauty)]

        df_vegetables.to_excel(writer, sheet_name="Vegetables", index=False)
        df_fruits.to_excel(writer, sheet_name="Fruits", index=False)
        df_bread.to_excel(writer, sheet_name="Bread", index=False)
        df_bread.to_excel(writer, sheet_name="Beer", index=False)
        df_beauty.to_excel(writer, sheet_name="Beauty", index=False)


else:

    print("Az árak és a termékek listái nem azonos hosszúságúak.")
