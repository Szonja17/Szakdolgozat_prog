from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlparse
import pandas as pd
import time


s = Service("C:/Users/Tőke Szonja/Desktop/UNI/pythonProject/LearningSelenium/chromedriver.exe")
driver = webdriver.Chrome(service=s)
def kattintas(driver, xpath):
    gomb = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    gomb.click()
    time.sleep(2)

def mentes(driver, class_name, timeout=10):
        adatok = WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, class_name))
        )
        return adatok

def mentes_au(driver, itemprop_value, timeout=10):
    adatok = WebDriverWait(driver, timeout).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, f'[itemprop="{itemprop_value}"]'))
    )
    time.sleep(2)  # You may consider removing this line or adjusting the sleep duration
    return adatok
def legorgetes(driver):
    while True:
        # Az oldal jelenlegi magasságát lekérjük
        current_height = driver.execute_script(
            "return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")

        # Oldal lefelé görgetése
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Várakozás az új tartalom betöltésére
        time.sleep(2)

        # Az új magasság lekérdezése
        new_height = driver.execute_script(
            "return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")

        # Ha az oldal már nem változik, kilépünk a ciklusból
        if new_height == current_height:
            break

#MAGYARORSZAG
# Oldal betöltése
driver.get("https://www.kozertplusz.hu/")
time.sleep(2)

#Cookie elfogadása
xpath = '/html/body/div[10]/div/div[2]/button'
kattintas(driver, xpath)

# Zöldségek kinyerése
# Termékkínálatra való kattintás
xpath = '/html/body/div[9]/div[2]/div[3]/div/div[1]/span'
kattintas(driver, xpath)

# Zöldség menüpontra kattintás
xpath = '/html/body/div[9]/div[2]/div[3]/div/div[1]/ul/li[1]/a'
kattintas(driver, xpath)

# Zöldségek megnyitása
xpath = '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[3]/div[2]/div/div[1]/div/div/a'
kattintas(driver, xpath)

# Várakozás a zöldségek terméknevek és árak betöltésére
product_name_elements = mentes(driver, "product-title")
time.sleep(2)
product_price_elements = mentes(driver, "price.actual-price")

# Termékek neveinek és árainak kinyerése
product_name_vegetables_hu = [element.text for element in product_name_elements]
product_price_vegetables_hu = [element.text for element in product_price_elements]

time.sleep(2)
# Gyümölcsök kinyerése
# Várakozás a zöldségek, gyümölcsök menüpont betöltésére
xpath = '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[1]/ul/li[2]Weboldal /a'
kattintas(driver, xpath)

#Rákattintás a gyümölcsökre
xpath = '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[3]/div[2]/div/div[2]/div'
kattintas(driver, xpath)

# Várakozás a gyümölcsök terméknevek és árak betöltésére
product_name_elements = mentes(driver, "product-title")
time.sleep(2)
product_price_elements = mentes(driver, "price.actual-price")

# Termékek neveinek és árainak kinyerése
product_name_fruits_hu = [element.text for element in product_name_elements]
product_price_fruits_hu = [element.text for element in product_price_elements]
time.sleep(2)

# Tejek kinyerése
# Teermékkategóriákra kattintás
xpath = '/html/body/div[9]/div[2]/div[3]/div/div[1]/span'
kattintas(driver, xpath)

# Várakozás a "Tektermékek, sajt és tojás" menüpontra
xpath = '/html/body/div[9]/div[2]/div[3]/div/div[1]/ul/li[2]/a'
kattintas(driver, xpath)

# Tejek megnyitása
xpath = '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[3]/div[3]/div[1]/div[3]/a'
kattintas(driver, xpath)

# Várakozás a tejek terméknevek és árak betöltésére
product_name_elements = mentes(driver, "product-title")
time.sleep(2)
product_price_elements = mentes(driver, "base-price-pangv")

# Termékek neveinek és árainak kinyerése
product_name_milk_hu = [element.text for element in product_name_elements]
product_price_milk_hu = [element.text for element in product_price_elements]

time.sleep(2)

#Vajak
# Visszalépés a tejtermékek, sajtok és tojások menüpontra
xpath = '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[1]/ul/li[2]/a'
kattintas(driver, xpath)

# Vajak megnyitása
xpath = '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[3]/div[2]/div/div[6]/div'
kattintas(driver, xpath)

# Várakozás a vajak terméknevek és árak betöltésére
product_name_elements = mentes(driver, "product-title")
time.sleep(2)
product_price_elements = mentes(driver, "base-price-pangv")

product_name_butter_hu = [element.text for element in product_name_elements]
product_price_butter_hu = [element.text for element in product_price_elements]

#Tojás
# Visszalépés a tejtermékek, sajtok és tojások menüpontra
xpath = '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[1]/ul/li[2]/a'
kattintas(driver, xpath)

# Tojás megnyitása
search_box = driver.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[2]/form/span/input')
# Szöveg beírása a keresőmezőbe
search_box.send_keys("Tojás")

# Enter lenyomása
search_box.send_keys(Keys.ENTER)

# Várakozás a vajak terméknevek és árak betöltésére
product_name_elements = mentes(driver, "product-title")
time.sleep(2)
product_price_elements = mentes(driver, "price.actual-price")

# Termékek neveinek és árainak kinyerése
product_name_egg_hu = [element.text for element in product_name_elements]
product_price_egg_hu = [element.text for element in product_price_elements]

# Husok
# Termékkategóriák megnyitása
xpath = '/html/body/div[9]/div[2]/div[3]/div/div[1]/span'
kattintas(driver, xpath)

# Várakozás a "Húsok és halak" menüpontra
xpath = '/html/body/div[9]/div[2]/div[3]/div/div[1]/ul/li[3]'
kattintas(driver, xpath)

# Várakozás a "Fehér húsok" menüpontra
xpath = '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[3]/div[2]/div/div[14]/div'
kattintas(driver, xpath)

# Várakozás a húsok terméknevek és árak betöltésére
product_name_elements = mentes(driver, "product-title")
time.sleep(2)
product_price_elements = mentes(driver, "base-price-pangv")

# Termékek neveinek és árainak kinyerése
product_name_meat_hu = [element.text for element in product_name_elements]
product_price_meat_hu = [element.text for element in product_price_elements]

time.sleep(2)

# Kenyerek
# Termékkategóriák megnyitása
xpath = '/html/body/div[9]/div[2]/div[3]/div/div[1]/span'
kattintas(driver, xpath)

# Várakozás a "Pékáru" menüpontra
xpath = '/html/body/div[9]/div[2]/div[3]/div/div[1]/ul/li[4]'
kattintas(driver, xpath)

# Rákattintás a kenyerek menüpontra
xpath = '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[3]/div[3]/div[1]/div[3]/a'
kattintas(driver, xpath)

# Várakozás a kenyerek terméknevek és árak betöltésére
product_name_elements = mentes(driver, "product-title")
time.sleep(2)
product_price_elements = mentes(driver, "price.actual-price")

# Termékek neveinek és árainak kinyerése
product_name_bread_hu = [element.text for element in product_name_elements]
product_price_bread_hu = [element.text for element in product_price_elements]

time.sleep(2)

#Tesztak
# Menu megnyitása
xpath = '/html/body/div[9]/div[2]/div[3]/div/div[1]/span'
kattintas(driver, xpath)

# Várakozás a "Tartós termékek" menüpontra
xpath = '/html/body/div[9]/div[2]/div[3]/div/div[1]/ul/li[6]/a'
kattintas(driver, xpath)

# Várakozás a "Sütés-főzés" menüpontra
xpath = '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[3]/div[2]/div[2]/div[3]'
kattintas(driver, xpath)

# Várakozás a "Tészták" menüpontra
xpath = '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[3]/div[1]/div/div[8]/div'
kattintas(driver, xpath)

# Várakozás a tészták terméknevek és árak betöltésére
product_name_elements = mentes(driver, "product-title")
time.sleep(2)
product_price_elements = mentes(driver, "base-price-pangv")

# Termékek neveinek és árainak kinyerése
product_name_pasta_hu = [element.text for element in product_name_elements]
product_price_pasta_hu = [element.text for element in product_price_elements]

time.sleep(2)

#Alkohol
# Termékkategóriák megnyitása
xpath = '/html/body/div[9]/div[2]/div[3]/div/div[1]/span'
kattintas(driver, xpath)

# Várakozás a "Italok" menüpontra
xpath = '/html/body/div[9]/div[2]/div[3]/div/div[1]/ul/li[5]'
kattintas(driver, xpath)

# Várakozás a "Alkoholok" menüpontra
xpath = '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[3]/div[1]/div/div[1]/div'
kattintas(driver, xpath)

# Várakozás a "Sörök" menüpontra
xpath = '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[3]/div[1]/div/div[2]'
kattintas(driver, xpath)

# Várakozás a sörök terméknevek és árak betöltésére
product_name_elements = mentes(driver, "product-title")
time.sleep(2)
product_price_elements = mentes(driver, "base-price-pangv")

# Termékek neveinek és árainak kinyerése
product_name_beer_hu = [element.text for element in product_name_elements]
product_price_beer_hu = [element.text for element in product_price_elements]

time.sleep(2)

#Higéniás eszközök
# Menu megnyitása
cart_icon = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[2]/div[3]/div/div[1]/span'))
)
cart_icon.click()
time.sleep(2)

# Várakozás a "Szépségápolás" menüpontra
beauty_menu = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[2]/div[3]/div/div[1]/ul/li[8]'))
)
beauty_menu.click()
time.sleep(3)

legorgetes(driver)
time.sleep(5)
# Várakozás a beauty terméknevek és árak betöltésére
product_name_elements = mentes(driver, "product-title")
time.sleep(2)
product_price_elements = mentes(driver, "price.actual-price")

time.sleep(10)
# Termékek neveinek és árainak kinyerése
product_name_beauty_hu = [element.text for element in product_name_elements]
product_price_beauty_hu = [element.text for element in product_price_elements]

time.sleep(2)

# WebDriver leállítása
driver.quit()

#AUSZTRIA
s = Service("C:/Users/Tőke Szonja/Desktop/UNI/pythonProject/LearningSelenium/chromedriver.exe")
driver = webdriver.Chrome(service=s)

# Oldal betöltése
driver.get("https://www.roksh.at/hofer/home")

time.sleep(5)

# Cookiek elfogadása
xpath = '/html/body/div[3]/div[1]/div[5]/div[2]/a[3]'
kattintas(driver, xpath)

# Zöldségek kinyerése
# Zöldségek és gyümölcsök menüpontra való kattintás
xpath = '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[1]'
kattintas(driver, xpath)

# Zöldségek menüpontra való kattintás
xpath = '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[1]/div/ul/li[1]/div/a'
kattintas(driver, xpath)
driver.refresh()
time.sleep(2)
legorgetes(driver)

# Várakozás a zöldségek terméknevek és árak betöltésére
product_name_elements = mentes_au(driver, "name")
time.sleep(2)
product_price_elements = mentes_au(driver, "price")
time.sleep(2)

# Termékek neveinek és árainak kinyerése
product_name_vegetables_au = [element.text for element in product_name_elements]
product_price_vegetables_au = [element.text for element in product_price_elements]

time.sleep(2)
# Gyümölcsök kinyerése
# Gyümölcsök menüpontra való kattintás
xpath = '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[1]/div/ul/li[2]/div/a'
kattintas(driver, xpath)

legorgetes(driver)
# Várakozás a gyümölcsök terméknevek és árak betöltésére
product_name_elements = mentes_au(driver, "name")
time.sleep(2)
product_price_elements = mentes_au(driver, "price")
time.sleep(2)

# Termékek neveinek és árainak kinyerése
product_name_fruits_au = [element.text for element in product_name_elements]
product_price_fruits_au = [element.text for element in product_price_elements]

time.sleep(2)
# Tejek kinyerése
# Tejtermékek menüpontra való kattintás
xpath = '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[3]/a'
kattintas(driver, xpath)

# A "Go to category" ra kattintás
xpath = '/html/body/app-root/div/app-product-list-new/div/app-product-group[1]/div/div/div/div/div[1]/a[1]'
kattintas(driver, xpath)

# A tejekre kattintás
xpath = '/html/body/app-root/div/app-product-list-new/div/app-product-list-header/div[1]/div[2]/div[1]/app-category-card[5]/div/a'
kattintas(driver, xpath)
legorgetes(driver)

# Várakozás a tejek terméknevek és árak betöltésére
product_name_elements = mentes_au(driver, "name")
time.sleep(2)
product_price_elements = mentes_au(driver, "price")
time.sleep(2)

# Termékek neveinek és árainak kinyerése
product_name_milk_au = [element.text for element in product_name_elements]
product_price_milk_au = [element.text for element in product_price_elements]
time.sleep(2)

# Vajak kinyerése
# A tejek és tejtermékekre kattintás
xpath = '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[3]/div/ul/li[1]/div/a'
kattintas(driver, xpath)

# A vajakra
xpath = '/html/body/app-root/div/app-product-list-new/div/app-product-list-header/div[1]/div[2]/div[1]/app-category-card[5]/div/a/div/span'
kattintas(driver, xpath)
legorgetes(driver)

# Várakozás a vajak terméknevek és árak betöltésére
product_name_elements = mentes_au(driver, "name")
time.sleep(2)
product_price_elements = mentes_au(driver, "price")
time.sleep(2)

# Termékek neveinek és árainak kinyerése
product_name_butter_au = [element.text for element in product_name_elements]
product_price_butter_au = [element.text for element in product_price_elements]
time.sleep(2)

#Tojások kinyerése
# A tojásokra kattintás
xpath = '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[3]/div/ul/li[5]/div/a'
kattintas(driver, xpath)
legorgetes(driver)

# Várakozás a tojások terméknevek és árak betöltésére
product_name_elements = mentes_au(driver, "name")
time.sleep(2)
product_price_elements = mentes_au(driver, "price")
time.sleep(2)

# Termékek neveinek és árainak kinyerése
product_name_egg_au = [element.text for element in product_name_elements]
product_price_egg_au = [element.text for element in product_price_elements]
time.sleep(2)

#Tészta kinyerése
# A sütésre kattintás
xpath = '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[5]/a'
kattintas(driver, xpath)

# A tésztákra kattintás
xpath = '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[5]/div/ul/li[7]/div/a/span'
kattintas(driver, xpath)
legorgetes(driver)

# Várakozás a tészták terméknevek és árak betöltésére
product_name_elements = mentes_au(driver, "name")
time.sleep(2)
product_price_elements = mentes_au(driver, "price")
time.sleep(2)

# Termékek neveinek és árainak kinyerése
product_name_pasta_au = [element.text for element in product_name_elements]
product_price_pasta_au = [element.text for element in product_price_elements]
time.sleep(2)

# husok kinyerése
# A "Meat, sausages and fish" menüpontra kattintás
xpath = '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[4]/a'
kattintas(driver, xpath)

# Húsok menüpontra kattintás
xpath = '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[4]/div/ul/li[2]/div/a'
kattintas(driver, xpath)
legorgetes(driver)

# Várakozás a husok terméknevek és árak betöltésére
product_name_elements = mentes_au(driver, "name")
time.sleep(2)
product_price_elements = mentes_au(driver, "price")
time.sleep(2)

# Termékek neveinek és árainak kinyerése
product_name_meat_au = [element.text for element in product_name_elements]
product_price_meat_au = [element.text for element in product_price_elements]
time.sleep(2)

# péksütemények kinyerése
# A "Bread and pastries" menüpontra kattintás
xpath = '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[2]/a'
kattintas(driver, xpath)

# Kenyerek menüpontra kattintás
xpath = '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[2]/div/ul/li[2]/div/a'
kattintas(driver, xpath)
legorgetes(driver)

# Várakozás a kenyerek terméknevek és árak betöltésére
product_name_elements = mentes_au(driver, "name")
time.sleep(2)
product_price_elements = mentes_au(driver, "price")
time.sleep(2)

# Termékek neveinek és árainak kinyerése
product_name_bread_au = [element.text for element in product_name_elements]
product_price_bread_au = [element.text for element in product_price_elements]
time.sleep(2)

# Alkoholok
# A "Italok" menüpontra kattintás
xpath = '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[9]/a'
kattintas(driver, xpath)

# Sörök menüpontra kattintás
xpath = '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[9]/div/ul/li[3]/div/a'
kattintas(driver, xpath)
legorgetes(driver)

# Várakozás a sörök terméknevek és árak betöltésére
product_name_elements = mentes_au(driver, "name")
time.sleep(2)
product_price_elements = mentes_au(driver, "price")
time.sleep(2)

# Termékek neveinek és árainak kinyerése
product_name_beer_au = [element.text for element in product_name_elements]
product_price_beer_au = [element.text for element in product_price_elements]
time.sleep(2)

# Higénia
# A "Italok" menüpontra kattintás
xpath = '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[10]/a'
kattintas(driver, xpath)

# Care menüpontra kattintás
xpath = '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[10]/div/ul/li[1]/div/a'
kattintas(driver, xpath)
legorgetes(driver)

# Várakozás a higéniás termékek terméknevek és árak betöltésére
product_name_elements = mentes_au(driver, "name")
time.sleep(2)
product_price_elements = mentes_au(driver, "price")
time.sleep(2)

# Termékek neveinek és árainak kinyerése
product_name_beauty_au = [element.text for element in product_name_elements]
product_price_beauty_au = [element.text for element in product_price_elements]
time.sleep(2)

driver.quit()

s = Service("C:/Users/Tőke Szonja/Desktop/UNI/pythonProject/LearningSelenium/chromedriver.exe")
driver = webdriver.Chrome(service=s)

# Oldal betöltése
driver.get("https://lunys.sk/")
time.sleep(2)

# Cookie elfogadása
xpath = '/html/body/div[1]/div/div[6]/button[1]'
kattintas(driver, xpath)

# Felugró fül kiikszelése
xpath = '/html/body/div[2]/div[1]/div/span'
kattintas(driver, xpath)

# Húsok
# Húsokra kattintás
xpath = '/html/body/div[2]/header/div[2]/nav/ul/li[4]/a/span/img'
kattintas(driver, xpath)

# Szárnyasok menüpont
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[1]/a'
kattintas(driver, xpath)

# Várakozás a szárnyasok terméknevek és árak betöltésére
product_name_elements = mentes(driver, "woodetail--title")
time.sleep(2)
ar = mentes(driver, "woocommerce-Price-amount.amount")
product_price_elements = mentes(driver, "product_price_per_kg.product_price_per_kg_short")

# Termékek neveinek és árainak kinyerése
product_name_meat_sk = [element.text for element in product_name_elements]
product_price_meat_sk = [element.text for element in product_price_elements]
time.sleep(2)

# Az aktuális oldal URL-jének elmentése
previous_url = urlparse(driver.current_url)

# A többi oldal megtekintése
while True:
    try:
        # Következő oldal gomb keresése
        next_page_button = driver.find_element(By.XPATH,'/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/nav/a[3]')
        next_page_button.click()
        # Várakozás a szárnyasok terméknevek és árak betöltésére
        product_name_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
        )

        product_price_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product_price_per_kg.product_price_per_kg_short"))
        )

        # Termékek neveinek és árainak kinyerése
        product_name_meat_sk += [element.text for element in product_name_elements]
        product_price_meat_sk += [element.text for element in product_price_elements]

        # Az aktuális oldal URL-jének lekérése
        current_url = urlparse(driver.current_url)

        # Az előző oldal URL-jének összehasonlítása a jelenlegivel
        if "page" in current_url.path and "page" in previous_url.path:
            # A számok kinyerése a "page" utáni részből (perjel eltávolításával)
            current_page_number = int(current_url.path.split("page/")[-1].rstrip('/'))
            previous_page_number = int(previous_url.path.split("page/")[-1].rstrip('/'))

            # Az oldalszámok összehasonlítása
            if current_page_number <= previous_page_number:
                # Ha a következő oldal URL-je kisebb vagy egyenlő az előzővel, kilépünk a ciklusból
                break

        # Az aktuális oldal URL-jének frissítése az új oldalra
        previous_url = current_url

    except NoSuchElementException:
        # Ha nincs következő oldal gomb, kilépünk a ciklusból
        break

#Tojás
# Tejtermékekre kattintás
xpath = '/html/body/div[2]/header/div[2]/nav/ul/li[5]/a/span/img'
kattintas(driver, xpath)

# Tojásokra kattintás
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[4]/a'
kattintas(driver, xpath)

# Várakozás a tojások terméknevek és árak betöltésére
product_name_elements = mentes(driver, "woodetail--title")
time.sleep(2)
product_price_elements = mentes(driver, "product_price_per_kg.product_price_per_kg_short")


# Termékek neveinek és árainak kinyerése
product_name_egg_sk = [element.text for element in product_name_elements]
product_price_egg_sk = [element.text for element in product_price_elements]
time.sleep(2)

# Tejek
# Visszalépés a tejtermékekre
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/a[2]'
kattintas(driver, xpath)
time.sleep(2)

#Tejekre való kattintás
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[2]/a'
kattintas(driver, xpath)

# Várakozás a tejek terméknevek és árak betöltésére
product_name_elements = mentes(driver, "woodetail--title")
time.sleep(2)
product_price_elements = mentes(driver, "product_price_per_kg.product_price_per_kg_short")

# Termékek neveinek és árainak kinyerése
product_name_milk_sk = [element.text for element in product_name_elements]
product_price_milk_sk = [element.text for element in product_price_elements]
time.sleep(2)

# Az aktuális oldal URL-jének elmentése
previous_url = urlparse(driver.current_url)

# A többi oldal megtekintése
while True:
    try:
        # Következő oldal gomb keresése
        next_page_button = driver.find_element(By.XPATH,'/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/nav/a[3]')
        next_page_button.click()
        # Várakozás a szárnyasok terméknevek és árak betöltésére
        product_name_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
        )

        product_price_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product_price_per_kg.product_price_per_kg_short"))
        )

        # Termékek neveinek és árainak kinyerése
        product_name_milk_sk += [element.text for element in product_name_elements]
        product_price_milk_sk += [element.text for element in product_price_elements]

        # Az aktuális oldal URL-jének lekérése
        current_url = urlparse(driver.current_url)

        # Az előző oldal URL-jének összehasonlítása a jelenlegivel
        if "page" in current_url.path and "page" in previous_url.path:
            # A számok kinyerése a "page" utáni részből (perjel eltávolításával)
            current_page_number = int(current_url.path.split("page/")[-1].rstrip('/'))
            previous_page_number = int(previous_url.path.split("page/")[-1].rstrip('/'))

            # Az oldalszámok összehasonlítása
            if current_page_number <= previous_page_number:
                # Ha a következő oldal URL-je kisebb vagy egyenlő az előzővel, kilépünk a ciklusból
                break

        # Az aktuális oldal URL-jének frissítése az új oldalra
        previous_url = current_url

    except NoSuchElementException:
        # Ha nincs következő oldal gomb, kilépünk a ciklusból
        break

#Vajak
#Visszalépés a tejtermékekre
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/a[2]'
kattintas(driver, xpath)

#Vajakra kattintás
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[6]/a'
kattintas(driver, xpath)

# Várakozás a vajak terméknevek és árak betöltésére
product_name_elements = mentes(driver, "woodetail--title")
time.sleep(2)
product_price_elements = mentes(driver, "product_price_per_kg.product_price_per_kg_short")

# Termékek neveinek és árainak kinyerése
product_name_butter_sk = [element.text for element in product_name_elements]
product_price_butter_sk = [element.text for element in product_price_elements]
time.sleep(2)

# Az aktuális oldal URL-jének elmentése
previous_url = urlparse(driver.current_url)

# A többi oldal megtekintése
while True:
    try:
        # Következő oldal gomb keresése
        next_page_button = driver.find_element(By.XPATH,'/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/nav/a[3]')
        next_page_button.click()
        # Várakozás a szárnyasok terméknevek és árak betöltésére
        product_name_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
        )

        product_price_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product_price_per_kg.product_price_per_kg_short"))
        )

        # Termékek neveinek és árainak kinyerése
        product_name_butter_sk += [element.text for element in product_name_elements]
        product_price_butter_sk += [element.text for element in product_price_elements]

        # Az aktuális oldal URL-jének lekérése
        current_url = urlparse(driver.current_url)

        # Az előző oldal URL-jének összehasonlítása a jelenlegivel
        if "page" in current_url.path and "page" in previous_url.path:
            # A számok kinyerése a "page" utáni részből (perjel eltávolításával)
            current_page_number = int(current_url.path.split("page/")[-1].rstrip('/'))
            previous_page_number = int(previous_url.path.split("page/")[-1].rstrip('/'))

            # Az oldalszámok összehasonlítása
            if current_page_number <= previous_page_number:
                # Ha a következő oldal URL-je kisebb vagy egyenlő az előzővel, kilépünk a ciklusból
                break

        # Az aktuális oldal URL-jének frissítése az új oldalra
        previous_url = current_url

    except NoSuchElementException:
        # Ha nincs következő oldal gomb, kilépünk a ciklusból
        break

# Teszta
# Keresőmező kiválasztása
search_box = driver.find_element(By.XPATH, '/html/body/div[2]/header/div[2]/div[1]/section/div[2]/div/span/input')

# Spagetti keresése
# Szöveg beírása a keresőmezőbe
search_box.send_keys("Špagety 500")

# Enter lenyomása
search_box.send_keys(Keys.ENTER)

# Várakozás a keressé eredményének terméknevek és árak betöltésére
product_name_elements = mentes(driver, "woodetail--title")
time.sleep(2)
product_price_elements = mentes(driver, "product_price_per_kg.product_price_per_kg_short")
time.sleep(2)


# Termékek neveinek és árainak kinyerése
product_name_pasta_sk = [element.text for element in product_name_elements]
product_price_pasta_sk = [element.text for element in product_price_elements]
time.sleep(2)

#Zöldségek
#Zöldségek menüpontra kattintás
xpath = '/html/body/div[2]/header/div[2]/nav/ul/li[2]/a'
kattintas(driver, xpath)

#Saláta
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[1]/a'
kattintas(driver, xpath)

# Várakozás a terméknevek és árak betöltésére
product_name_elements = mentes(driver, "woodetail--title")
time.sleep(2)
product_price_elements = mentes(driver, "product_price_per_kg.product_price_per_kg_short")
time.sleep(2)

# Termékek neveinek és árainak kinyerése
product_name_vegetable_sk = [element.text for element in product_name_elements]
product_price_vegetable_sk = [element.text for element in product_price_elements]
time.sleep(2)

# Az aktuális oldal URL-jének elmentése
previous_url = urlparse(driver.current_url)

# A többi oldal megtekintése
while True:
    try:
        # Következő oldal gomb keresése
        next_page_button = driver.find_element(By.XPATH,'/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/nav/a[3]')
        next_page_button.click()
        # Várakozás a szárnyasok terméknevek és árak betöltésére
        product_name_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
        )

        product_price_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product_price_per_kg.product_price_per_kg_short"))
        )

        # Termékek neveinek és árainak kinyerése
        product_name_vegetable_sk += [element.text for element in product_name_elements]
        product_price_vegetable_sk += [element.text for element in product_price_elements]

        # Az aktuális oldal URL-jének lekérése
        current_url = urlparse(driver.current_url)

        # Az előző oldal URL-jének összehasonlítása a jelenlegivel
        if "page" in current_url.path and "page" in previous_url.path:
            # A számok kinyerése a "page" utáni részből (perjel eltávolításával)
            current_page_number = int(current_url.path.split("page/")[-1].rstrip('/'))
            previous_page_number = int(previous_url.path.split("page/")[-1].rstrip('/'))

            # Az oldalszámok összehasonlítása
            if current_page_number <= previous_page_number:
                # Ha a következő oldal URL-je kisebb vagy egyenlő az előzővel, kilépünk a ciklusból
                break

        # Az aktuális oldal URL-jének frissítése az új oldalra
        previous_url = current_url

    except NoSuchElementException:
        # Ha nincs következő oldal gomb, kilépünk a ciklusból
        break

#Hagyma
#Visszalépés a zöldségek menüpontra
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/a[2]'
kattintas(driver, xpath)

#Hagyma menüpontra lépés
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[4]/a'
kattintas(driver, xpath)

# Várakozás a terméknevek és árak betöltésére
product_name_elements = mentes(driver, "woodetail--title")
time.sleep(2)
product_price_elements = mentes(driver, "product_price_per_kg.product_price_per_kg_short")


# Termékek neveinek és árainak kinyerése
product_name_vegetable_sk += [element.text for element in product_name_elements]
product_price_vegetable_sk += [element.text for element in product_price_elements]
time.sleep(2)

#Répa
#Visszalépés a zöldségek menüpontra
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/a[2]'
kattintas(driver, xpath)

#Belépés a répákhoz
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[5]/a'
kattintas(driver, xpath)

# Várakozás a répák terméknevek és árak betöltésére
product_name_elements = mentes(driver, "woodetail--title")
time.sleep(2)
product_price_elements = mentes(driver, "product_price_per_kg.product_price_per_kg_short")
time.sleep(2)

# Termékek neveinek és árainak kinyerése
product_name_vegetable_sk += [element.text for element in product_name_elements]
product_price_vegetable_sk += [element.text for element in product_price_elements]
time.sleep(2)

# Az aktuális oldal URL-jének elmentése
previous_url = urlparse(driver.current_url)

# A többi oldal megtekintése
while True:
    try:
        # Következő oldal gomb keresése
        next_page_button = driver.find_element(By.XPATH,'/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/nav/a[3]')
        next_page_button.click()
        # Várakozás a szárnyasok terméknevek és árak betöltésére
        product_name_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
        )

        product_price_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product_price_per_kg.product_price_per_kg_short"))
        )

        # Termékek neveinek és árainak kinyerése
        product_name_vegetable_sk += [element.text for element in product_name_elements]
        product_price_vegetable_sk += [element.text for element in product_price_elements]

        # Az aktuális oldal URL-jének lekérése
        current_url = urlparse(driver.current_url)

        # Az előző oldal URL-jének összehasonlítása a jelenlegivel
        if "page" in current_url.path and "page" in previous_url.path:
            # A számok kinyerése a "page" utáni részből (perjel eltávolításával)
            current_page_number = int(current_url.path.split("page/")[-1].rstrip('/'))
            previous_page_number = int(previous_url.path.split("page/")[-1].rstrip('/'))

            # Az oldalszámok összehasonlítása
            if current_page_number <= previous_page_number:
                # Ha a következő oldal URL-je kisebb vagy egyenlő az előzővel, kilépünk a ciklusból
                break

        # Az aktuális oldal URL-jének frissítése az új oldalra
        previous_url = current_url

    except NoSuchElementException:
        # Ha nincs következő oldal gomb, kilépünk a ciklusból
        break

#Paradicsom
#Visszalépés a zöldségek menüpontra
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/a[2]'
kattintas(driver, xpath)

#Belépés a paradicsomokhoz
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[3]/a'
kattintas(driver, xpath)

# Várakozás a paradicsomok terméknevek és árak betöltésére
product_name_elements = mentes(driver, "woodetail--title")
time.sleep(2)
product_price_elements = mentes(driver, "product_price_per_kg.product_price_per_kg_short")

# Termékek neveinek és árainak kinyerése
product_name_vegetable_sk += [element.text for element in product_name_elements]
product_price_vegetable_sk += [element.text for element in product_price_elements]
time.sleep(2)

# Az aktuális oldal URL-jének elmentése
previous_url = urlparse(driver.current_url)

# A többi oldal megtekintése
while True:
    try:
        # Következő oldal gomb keresése
        next_page_button = driver.find_element(By.XPATH,'/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/nav/a[3]')
        next_page_button.click()
        # Várakozás a szárnyasok terméknevek és árak betöltésére
        product_name_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
        )

        product_price_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product_price_per_kg.product_price_per_kg_short"))
        )

        # Termékek neveinek és árainak kinyerése
        product_name_vegetable_sk += [element.text for element in product_name_elements]
        product_price_vegetable_sk += [element.text for element in product_price_elements]

        # Az aktuális oldal URL-jének lekérése
        current_url = urlparse(driver.current_url)

        # Az előző oldal URL-jének összehasonlítása a jelenlegivel
        if "page" in current_url.path and "page" in previous_url.path:
            # A számok kinyerése a "page" utáni részből (perjel eltávolításával)
            current_page_number = int(current_url.path.split("page/")[-1].rstrip('/'))
            previous_page_number = int(previous_url.path.split("page/")[-1].rstrip('/'))

            # Az oldalszámok összehasonlítása
            if current_page_number <= previous_page_number:
                # Ha a következő oldal URL-je kisebb vagy egyenlő az előzővel, kilépünk a ciklusból
                break

        # Az aktuális oldal URL-jének frissítése az új oldalra
        previous_url = current_url

    except NoSuchElementException:
        # Ha nincs következő oldal gomb, kilépünk a ciklusból
        break

#Gyümölcs
xpath = '/html/body/div[2]/header/div[2]/nav/ul/li[1]/a'
kattintas(driver, xpath)

#Alma
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[1]/a'
kattintas(driver, xpath)

# Várakozás a terméknevek és árak betöltésére
product_name_elements = mentes(driver, "woodetail--title")
time.sleep(2)
product_price_elements = mentes(driver, "product_price_per_kg.product_price_per_kg_short")

# Termékek neveinek és árainak kinyerése
product_name_fruit_sk = [element.text for element in product_name_elements]
product_price_fruit_sk = [element.text for element in product_price_elements]
time.sleep(2)

#Szőlő
#Visszalépés a fő menübe
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/a[2]'
kattintas(driver, xpath)

#Szőlők menüpont
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[3]/a'
kattintas(driver, xpath)

# Várakozás a keressé eredményének terméknevek és árak betöltésére
product_name_elements = mentes(driver, "woodetail--title")
time.sleep(2)
product_price_elements = mentes(driver, "product_price_per_kg.product_price_per_kg_short")

# Termékek neveinek és árainak kinyerése
product_name_fruit_sk += [element.text for element in product_name_elements]
product_price_fruit_sk += [element.text for element in product_price_elements]
time.sleep(2)

#Banán
#Visszalépés a fő menübe
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/a[2]'
kattintas(driver, xpath)

#Belépés az egzotikus gyümölcsökbe
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[7]/a'
kattintas(driver, xpath)

# Várakozás a egzotikus gyumolcsok terméknevek és árak betöltésére
product_name_elements = mentes(driver, "woodetail--title")
time.sleep(2)
product_price_elements = mentes(driver, "product_price_per_kg.product_price_per_kg_short")

# Termékek neveinek és árainak kinyerése
product_name_fruit_sk += [element.text for element in product_name_elements]
product_price_fruit_sk += [element.text for element in product_price_elements]
time.sleep(2)

# Az aktuális oldal URL-jének elmentése
previous_url = urlparse(driver.current_url)

# A többi oldal megtekintése
while True:
    try:
        # Következő oldal gomb keresése
        next_page_button = driver.find_element(By.XPATH,'/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/nav/a[3]')
        next_page_button.click()
        # Várakozás a szárnyasok terméknevek és árak betöltésére
        product_name_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
        )

        product_price_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product_price_per_kg.product_price_per_kg_short"))
        )

        # Termékek neveinek és árainak kinyerése
        product_name_fruit_sk += [element.text for element in product_name_elements]
        product_price_fruit_sk += [element.text for element in product_price_elements]

        # Az aktuális oldal URL-jének lekérése
        current_url = urlparse(driver.current_url)

        # Az előző oldal URL-jének összehasonlítása a jelenlegivel
        if "page" in current_url.path and "page" in previous_url.path:
            # A számok kinyerése a "page" utáni részből (perjel eltávolításával)
            current_page_number = int(current_url.path.split("page/")[-1].rstrip('/'))
            previous_page_number = int(previous_url.path.split("page/")[-1].rstrip('/'))

            # Az oldalszámok összehasonlítása
            if current_page_number <= previous_page_number:
                # Ha a következő oldal URL-je kisebb vagy egyenlő az előzővel, kilépünk a ciklusból
                break

        # Az aktuális oldal URL-jének frissítése az új oldalra
        previous_url = current_url

    except NoSuchElementException:
        # Ha nincs következő oldal gomb, kilépünk a ciklusból
        break

#Citrom
#Visszalépés a fő menübe
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/a[2]'
kattintas(driver, xpath)

#Belépés a citrusokba
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[6]/a'
kattintas(driver, xpath)

# Várakozás a keressé eredményének terméknevek és árak betöltésére
product_name_elements = mentes(driver, "woodetail--title")
time.sleep(2)
product_price_elements = mentes(driver, "product_price_per_kg.product_price_per_kg_short")


# Termékek neveinek és árainak kinyerése
product_name_fruit_sk += [element.text for element in product_name_elements]
product_price_fruit_sk += [element.text for element in product_price_elements]
time.sleep(2)

#Péksütik
#Belépés a péksüteményekbe
xpath = '/html/body/div[2]/header/div[2]/nav/ul/li[3]/a'
kattintas(driver, xpath)

#Kenyerek
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[1]/a'
kattintas(driver, xpath)

# Várakozás a terméknevek és árak betöltésére
product_name_elements = mentes(driver, "woodetail--title")
time.sleep(2)
product_price_elements = mentes(driver, "product_price_per_kg.product_price_per_kg_short")

# Termékek neveinek és árainak kinyerése
product_name_bread_sk = [element.text for element in product_name_elements]
product_price_bread_sk = [element.text for element in product_price_elements]
time.sleep(2)

#Tortilla
search_box = driver.find_element(By.XPATH, '/html/body/div[2]/header/div[2]/div[1]/section/div[2]/div/span/input')
# Szöveg beírása a keresőmezőbe
search_box.send_keys("Tortilla")

# Enter lenyomása
search_box.send_keys(Keys.ENTER)

# Várakozás a keressé eredményének terméknevek és árak betöltésére
product_name_elements = mentes(driver, "woodetail--title")
time.sleep(2)
product_price_elements = mentes(driver, "product_price_per_kg.product_price_per_kg_short")

# Termékek neveinek és árainak kinyerése
product_name_bread_sk += [element.text for element in product_name_elements]
product_price_bread_sk += [element.text for element in product_price_elements]
time.sleep(2)

#Hamburger
search_box = driver.find_element(By.XPATH, '/html/body/div[2]/header/div[2]/div[1]/section/div[2]/div/span/input')
# Szöveg beírása a keresőmezőbe
search_box.send_keys("Hamburger")

# Enter lenyomása
search_box.send_keys(Keys.ENTER)

# Várakozás a keressé eredményének terméknevek és árak betöltésére
product_name_elements = mentes(driver, "woodetail--title")
time.sleep(2)
product_price_elements = mentes(driver, "product_price_per_kg.product_price_per_kg_short")


# Termékek neveinek és árainak kinyerése
product_name_bread_sk += [element.text for element in product_name_elements]
product_price_bread_sk += [element.text for element in product_price_elements]
time.sleep(2)

#Sörök
#Kattintás az italok menüpontra
xpath = '/html/body/div[2]/header/div[2]/nav/ul/li[8]/a'
kattintas(driver, xpath)

#Kattintás a sörök menüpontra
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[2]/a'
kattintas(driver, xpath)

# Várakozás a terméknevek és árak betöltésére
product_name_elements = mentes(driver, "woodetail--title")
time.sleep(2)
product_price_elements = mentes(driver, "product_price_per_kg.product_price_per_kg_short")

# Termékek neveinek és árainak kinyerése
product_name_beer_sk = [element.text for element in product_name_elements]
product_price_beer_sk = [element.text for element in product_price_elements]
time.sleep(2)

# Az aktuális oldal URL-jének elmentése
previous_url = urlparse(driver.current_url)

# A többi oldal megtekintése
while True:
    try:
        # Következő oldal gomb keresése
        next_page_button = driver.find_element(By.XPATH,'/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/nav/a[3]')
        next_page_button.click()
        # Várakozás a szárnyasok terméknevek és árak betöltésére
        product_name_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
        )

        product_price_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product_price_per_kg.product_price_per_kg_short"))
        )

        # Termékek neveinek és árainak kinyerése
        product_name_beer_sk += [element.text for element in product_name_elements]
        product_price_beer_sk += [element.text for element in product_price_elements]

        # Az aktuális oldal URL-jének lekérése
        current_url = urlparse(driver.current_url)

        # Az előző oldal URL-jének összehasonlítása a jelenlegivel
        if "page" in current_url.path and "page" in previous_url.path:
            # A számok kinyerése a "page" utáni részből (perjel eltávolításával)
            current_page_number = int(current_url.path.split("page/")[-1].rstrip('/'))
            previous_page_number = int(previous_url.path.split("page/")[-1].rstrip('/'))

            # Az oldalszámok összehasonlítása
            if current_page_number <= previous_page_number:
                # Ha a következő oldal URL-je kisebb vagy egyenlő az előzővel, kilépünk a ciklusból
                break

        # Az aktuális oldal URL-jének frissítése az új oldalra
        previous_url = current_url

    except NoSuchElementException:
        # Ha nincs következő oldal gomb, kilépünk a ciklusból
        break

#Higéniás eszközök
#Belépés a menüpontba
xpath = '/html/body/div[2]/header/div[2]/nav/ul/li[11]/a'
kattintas(driver, xpath)

#Intim higénia
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[8]/a'
kattintas(driver, xpath)

# Várakozás a terméknevek és árak betöltésére
product_name_elements = mentes(driver, "woodetail--title")
time.sleep(2)
product_price_elements = mentes(driver, "product_price_per_kg.product_price_per_kg_short")


# Termékek neveinek és árainak kinyerése
product_name_hygen_sk = [element.text for element in product_name_elements]
product_price_hygen_sk = [element.text for element in product_price_elements]
time.sleep(2)


# Az aktuális oldal URL-jének elmentése
previous_url = urlparse(driver.current_url)

# A többi oldal megtekintése
while True:
    try:
        # Következő oldal gomb keresése
        next_page_button = driver.find_element(By.XPATH,'/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/nav/a[3]')
        next_page_button.click()
        # Várakozás a szárnyasok terméknevek és árak betöltésére
        product_name_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
        )

        product_price_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product_price_per_kg.product_price_per_kg_short"))
        )

        # Termékek neveinek és árainak kinyerése
        product_name_hygen_sk += [element.text for element in product_name_elements]
        product_price_hygen_sk += [element.text for element in product_price_elements]

        # Az aktuális oldal URL-jének lekérése
        current_url = urlparse(driver.current_url)

        # Az előző oldal URL-jének összehasonlítása a jelenlegivel
        if "page" in current_url.path and "page" in previous_url.path:
            # A számok kinyerése a "page" utáni részből (perjel eltávolításával)
            current_page_number = int(current_url.path.split("page/")[-1].rstrip('/'))
            previous_page_number = int(previous_url.path.split("page/")[-1].rstrip('/'))

            # Az oldalszámok összehasonlítása
            if current_page_number <= previous_page_number:
                # Ha a következő oldal URL-je kisebb vagy egyenlő az előzővel, kilépünk a ciklusból
                break

        # Az aktuális oldal URL-jének frissítése az új oldalra
        previous_url = current_url

    except NoSuchElementException:
        # Ha nincs következő oldal gomb, kilépünk a ciklusból
        break

#Mosószer
#Visszalépés
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/a[2]'
kattintas(driver, xpath)

#Belépés a mosószer menübe
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[10]/a'
kattintas(driver, xpath)

# Várakozás a terméknevek és árak betöltésére
product_name_elements = mentes(driver, "woodetail--title")
time.sleep(2)
product_price_elements = mentes(driver, "product_price_per_kg.product_price_per_kg_short")

# Termékek neveinek és árainak kinyerése
product_name_hygen_sk += [element.text for element in product_name_elements]
product_price_hygen_sk += [element.text for element in product_price_elements]
time.sleep(2)


# Az aktuális oldal URL-jének elmentése
previous_url = urlparse(driver.current_url)

# A többi oldal megtekintése
while True:
    try:
        # Következő oldal gomb keresése
        next_page_button = driver.find_element(By.XPATH,'/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/nav/a[3]')
        next_page_button.click()
        # Várakozás a szárnyasok terméknevek és árak betöltésére
        product_name_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
        )

        product_price_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product_price_per_kg.product_price_per_kg_short"))
        )

        # Termékek neveinek és árainak kinyerése
        product_name_hygen_sk += [element.text for element in product_name_elements]
        product_price_hygen_sk += [element.text for element in product_price_elements]

        # Az aktuális oldal URL-jének lekérése
        current_url = urlparse(driver.current_url)

        # Az előző oldal URL-jének összehasonlítása a jelenlegivel
        if "page" in current_url.path and "page" in previous_url.path:
            # A számok kinyerése a "page" utáni részből (perjel eltávolításával)
            current_page_number = int(current_url.path.split("page/")[-1].rstrip('/'))
            previous_page_number = int(previous_url.path.split("page/")[-1].rstrip('/'))

            # Az oldalszámok összehasonlítása
            if current_page_number <= previous_page_number:
                # Ha a következő oldal URL-je kisebb vagy egyenlő az előzővel, kilépünk a ciklusból
                break

        # Az aktuális oldal URL-jének frissítése az új oldalra
        previous_url = current_url

    except NoSuchElementException:
        # Ha nincs következő oldal gomb, kilépünk a ciklusból
        break

#Visszalépés
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/a[2]'
kattintas(driver, xpath)

#Száj higénia
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[2]/a'
kattintas(driver, xpath)

# Várakozás a terméknevek és árak betöltésére
product_name_elements = mentes(driver, "woodetail--title")
time.sleep(2)
product_price_elements = mentes(driver, "product_price_per_kg.product_price_per_kg_short")

# Termékek neveinek és árainak kinyerése
product_name_hygen_sk += [element.text for element in product_name_elements]
product_price_hygen_sk += [element.text for element in product_price_elements]
time.sleep(2)

# Az aktuális oldal URL-jének elmentése
previous_url = urlparse(driver.current_url)

# A többi oldal megtekintése
while True:
    try:
        # Következő oldal gomb keresése
        next_page_button = driver.find_element(By.XPATH,'/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/nav/a[3]')
        next_page_button.click()
        # Várakozás a szárnyasok terméknevek és árak betöltésére
        product_name_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
        )

        product_price_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product_price_per_kg.product_price_per_kg_short"))
        )

        # Termékek neveinek és árainak kinyerése
        product_name_hygen_sk += [element.text for element in product_name_elements]
        product_price_hygen_sk += [element.text for element in product_price_elements]

        # Az aktuális oldal URL-jének lekérése
        current_url = urlparse(driver.current_url)

        # Az előző oldal URL-jének összehasonlítása a jelenlegivel
        if "page" in current_url.path and "page" in previous_url.path:
            # A számok kinyerése a "page" utáni részből (perjel eltávolításával)
            current_page_number = int(current_url.path.split("page/")[-1].rstrip('/'))
            previous_page_number = int(previous_url.path.split("page/")[-1].rstrip('/'))

            # Az oldalszámok összehasonlítása
            if current_page_number <= previous_page_number:
                # Ha a következő oldal URL-je kisebb vagy egyenlő az előzővel, kilépünk a ciklusból
                break

        # Az aktuális oldal URL-jének frissítése az új oldalra
        previous_url = current_url

    except NoSuchElementException:
        # Ha nincs következő oldal gomb, kilépünk a ciklusból
        break

#Dezodor
#Visszalépés
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/a[2]'
kattintas(driver, xpath)

#Belépés a dezodor menübe
xpath = '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[6]/a'
kattintas(driver, xpath)

# Várakozás a terméknevek és árak betöltésére
product_name_elements = mentes(driver, "woodetail--title")
time.sleep(2)
product_price_elements = mentes(driver, "woodetail--price")

# Termékek neveinek és árainak kinyerése
product_name_hygen_sk += [element.text for element in product_name_elements]
product_price_hygen_sk += [element.text for element in product_price_elements]
time.sleep(2)


# Az aktuális oldal URL-jének elmentése
previous_url = urlparse(driver.current_url)

# A többi oldal megtekintése
while True:
    try:
        # Következő oldal gomb keresése
        next_page_button = driver.find_element(By.XPATH,'/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/nav/a[3]')
        next_page_button.click()
        # Várakozás a szárnyasok terméknevek és árak betöltésére
        product_name_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
        )

        product_price_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "cAdott gombokra való kattintás"
                                                                ""))
        )

        # Termékek neveinek és árainak kinyerése
        product_name_hygen_sk += [element.text for element in product_name_elements]
        product_price_hygen_sk += [element.text for element in product_price_elements]

        # Az aktuális oldal URL-jének lekérése
        current_url = urlparse(driver.current_url)

        # Az előző oldal URL-jének összehasonlítása a jelenlegivel
        if "page" in current_url.path and "page" in previous_url.path:
            # A számok kinyerése a "page" utáni részből (perjel eltávolításával)
            current_page_number = int(current_url.path.split("page/")[-1].rstrip('/'))
            previous_page_number = int(previous_url.path.split("page/")[-1].rstrip('/'))

            # Az oldalszámok összehasonlítása
            if current_page_number <= previous_page_number:
                # Ha a következő oldal URL-je kisebb vagy egyenlő az előzővel, kilépünk a ciklusból
                break

        # Az aktuális oldal URL-jének frissítése az új oldalra
        previous_url = current_url

    except NoSuchElementException:
        # Ha nincs következő oldal gomb, kilépünk a ciklusból
        break

# Kutatás
csirkemell_products_au = [(name, price) for name, price in zip(product_name_meat_au, product_price_meat_au) if 'hühnchen' and 'filets' in name.lower()]
vaj_products_au = [(name, price) for name, price in zip(product_name_butter_au, product_price_butter_au) if 'butter' in name.lower()]
tojas_products_au = [(name, price) for name, price in zip(product_name_egg_au, product_price_egg_au) if '10' in name]
tej_products_au = [(name, price) for name, price in zip(product_name_milk_au, product_price_milk_au) if 'milch' in name.lower()]
teszta_products_au = [(name, price) for name, price in zip(product_name_pasta_au, product_price_pasta_au) if 'spaghetti' in name.lower()]

csirkemell_products_hu = [(name, price) for name, price in zip(product_name_meat_hu, product_price_meat_hu) if 'csirkemell' in name.lower()]
butter_products_hu = [(name, price) for name, price in zip(product_name_butter_hu, product_price_butter_hu) if '200' in name]
egg_products_hu = [(name, price) for name, price in zip(product_name_egg_hu, product_price_egg_hu) if '10' in name]
milk_products_hu = [(name, price) for name, price in zip(product_name_milk_hu, product_price_milk_hu) if '2,8' in name]
pasta_products_hu = [(name, price) for name, price in zip(product_name_pasta_hu, product_price_pasta_hu) if 'spagetti' in name.lower()]

csirkemell_products_sk = [(name, price) for name, price in zip(product_name_meat_sk, product_price_meat_sk) if 'prsia' and '500' in name]
tojas_products_sk = [(name, price) for name, price in zip(product_name_egg_sk, product_price_egg_sk) if '10' in name]
vaj_products_sk = [(name, price) for name, price in zip(product_name_butter_sk, product_price_butter_sk) if '200' in name]
tej_products_sk = [(name, price) for name, price in zip(product_name_milk_sk, product_price_milk_sk) if 'mlieko' in name.lower()]
teszta_products_sk = [(name, price) for name, price in zip(product_name_pasta_sk, product_price_pasta_sk)]



# Ha vannak megfelelo termekek, akkor mentés
if csirkemell_products_au:
    csirkemell_hu = pd.DataFrame({"Product Name": [item[0] for item in csirkemell_products_hu],
                                "Product Price": [item[1] for item in csirkemell_products_hu]})
    vaj_hu = pd.DataFrame({"Product Name": [item[0] for item in butter_products_hu],
                                  "Product Price": [item[1] for item in butter_products_hu]})
    tojas_hu = pd.DataFrame({"Product Name": [item[0] for item in egg_products_hu],
                                 "Product Price": [item[1] for item in egg_products_hu]})
    tej_hu = pd.DataFrame({"Product Name": [item[0] for item in milk_products_hu],
                          "Product Price": [item[1] for item in milk_products_hu]})
    teszta_hu = pd.DataFrame({"Product Name": [item[0] for item in pasta_products_hu],
                        "Product Price": [item[1] for item in pasta_products_hu]})

    csirkemell_au = pd.DataFrame({"Product Name": [item[0] for item in csirkemell_products_au],
                            "Product Price": [item[1] for item in csirkemell_products_au]})
    vaj_au = pd.DataFrame({"Product Name": [item[0] for item in vaj_products_au],
                            "Product Price": [item[1] for item in vaj_products_au]})
    tojas_au = pd.DataFrame({"Product Name": [item[0] for item in tojas_products_au],
                            "Product Price": [item[1] for item in tojas_products_au]})
    tej_au = pd.DataFrame({"Product Name": [item[0] for item in tej_products_au],
                            "Product Price": [item[1] for item in tej_products_au]})
    teszta_au = pd.DataFrame({"Product Name": [item[0] for item in teszta_products_au],
                            "Product Price": [item[1] for item in teszta_products_au]})

    # Duplikációk eltávolítása
    csirkemell_sk = pd.DataFrame({"Product Name": [item[0] for item in csirkemell_products_sk],
                               "Product Price": [item[1] for item in csirkemell_products_sk]})

    csirkemell_sk.drop_duplicates(inplace=True)

    tojas_sk = pd.DataFrame({"Product Name": [item[0] for item in tojas_products_sk],
                          "Product Price": [item[1] for item in tojas_products_sk]})
    tojas_sk.drop_duplicates(inplace=True)

    vaj_sk = pd.DataFrame({"Product Name": [item[0] for item in vaj_products_sk],
                        "Product Price": [item[1] for item in vaj_products_sk]})
    vaj_sk.drop_duplicates(inplace=True)

    tej_sk = pd.DataFrame({"Product Name": [item[0] for item in tej_products_sk],
                        "Product Price": [item[1] for item in tej_products_sk]})
    tej_sk.drop_duplicates(inplace=True)

    teszta_sk = pd.DataFrame({"Product Name": [item[0] for item in teszta_products_sk],
                           "Product Price": [item[1] for item in teszta_products_sk]})
    teszta_sk.drop_duplicates(inplace=True)

    # Mentés külön munkalapra
    with pd.ExcelWriter("kutatas.xlsx", engine="xlsxwriter") as writer:
        csirkemell_hu.to_excel(writer, sheet_name="Chicken breast HU", index=False)
        vaj_hu.to_excel(writer, sheet_name="Butter HU", index=False)
        tojas_hu.to_excel(writer, sheet_name="Egg HU", index=False)
        tej_hu.to_excel(writer, sheet_name="Milk HU", index=False)
        teszta_hu.to_excel(writer, sheet_name="Pasta HU", index=False)

        csirkemell_au.to_excel(writer, sheet_name="Chicken breast AU", index=False)
        vaj_au.to_excel(writer, sheet_name="Butter AU", index=False)
        tojas_au.to_excel(writer, sheet_name="Egg AU", index=False)
        tej_au.to_excel(writer, sheet_name="Milk AU", index=False)
        teszta_au.to_excel(writer, sheet_name="Pasta AU", index=False)

        csirkemell_sk.to_excel(writer, sheet_name="Chicken breast SK", index=False)
        tojas_sk.to_excel(writer, sheet_name="Egg SK", index=False)
        vaj_sk.to_excel(writer, sheet_name="Butter SK", index=False)
        tej_sk.to_excel(writer, sheet_name="Milk SK", index=False)
        teszta_sk.to_excel(writer, sheet_name="Spaghetti SK", index=False)

# WebDriver leállítása
driver.quit()

# Adatok összefűzése
product_name_all = (product_name_vegetables_hu + product_name_fruits_hu + product_name_bread_hu + product_name_beer_hu + product_name_beauty_hu
                    + product_name_vegetables_au + product_name_fruits_au + product_name_bread_au + product_name_beer_au + product_name_beauty_au
                    + product_name_vegetable_sk + product_name_fruit_sk + product_name_bread_sk + product_name_beer_sk + product_name_hygen_sk)
product_price_all = (product_price_vegetables_hu + product_price_fruits_hu + product_price_bread_hu + product_price_beer_hu + product_price_beauty_hu +
                     product_price_vegetables_au + product_price_fruits_au + product_price_bread_au + product_price_beer_au + product_price_beauty_au
                     + product_price_vegetable_sk + product_price_fruit_sk + product_price_bread_sk + product_price_beer_sk + product_price_hygen_sk)

# Ellenőrzés: azonos hosszúságú-e a termékek neveinek és árainak listája
if len(product_name_all) == len(product_price_all):
    # Adatkeretek létrehozása
    df_all = pd.DataFrame({"Product Name": product_name_all, "Product Price": product_price_all})

    # Adatkeretek mentése külön munkalapokra egyetlen Excel fájlban
    with pd.ExcelWriter("products.xlsx", engine="xlsxwriter") as writer:
        df_vegetables_hu = df_all[df_all["Product Name"].isin(product_name_vegetables_hu)]
        df_fruits_hu = df_all[df_all["Product Name"].isin(product_name_fruits_hu)]
        df_bread_hu = df_all[df_all["Product Name"].isin(product_name_bread_hu)]
        df_beer_hu = df_all[df_all["Product Name"].isin(product_name_beer_hu)]
        df_beauty_hu = df_all[df_all["Product Name"].isin(product_name_beauty_hu)]

        df_vegetables_au = df_all[df_all["Product Name"].isin(product_name_vegetables_au)]
        df_fruits_au = df_all[df_all["Product Name"].isin(product_name_fruits_au)]
        df_bread_au = df_all[df_all["Product Name"].isin(product_name_bread_au)]
        df_beer_au = df_all[df_all["Product Name"].isin(product_name_beer_au)]
        df_beauty_au = df_all[df_all["Product Name"].isin(product_name_beauty_au)]

        df_vegetables_sk = df_all[df_all["Product Name"].isin(product_name_vegetable_sk)]
        df_fruits_sk = df_all[df_all["Product Name"].isin(product_name_fruit_sk)]
        df_bread_sk = df_all[df_all["Product Name"].isin(product_name_bread_sk)]
        df_beer_sk = df_all[df_all["Product Name"].isin(product_name_beer_sk)]
        df_beauty_sk = df_all[df_all["Product Name"].isin(product_name_hygen_sk)]

        df_vegetables_hu.to_excel(writer, sheet_name="Vegetables HU", index=False)
        df_fruits_hu.to_excel(writer, sheet_name="Fruits HU", index=False)
        df_bread_hu.to_excel(writer, sheet_name="Bread HU", index=False)
        df_beer_hu.to_excel(writer, sheet_name="Beer HU", index=False)
        df_beauty_hu.to_excel(writer, sheet_name="Beauty HU", index=False)

        df_vegetables_au.to_excel(writer, sheet_name="Vegetables AU", index=False)
        df_fruits_au.to_excel(writer, sheet_name="Fruits AU", index=False)
        df_bread_au.to_excel(writer, sheet_name="Bread AU", index=False)
        df_beer_au.to_excel(writer, sheet_name="Beer AU", index=False)
        df_beauty_au.to_excel(writer, sheet_name="Beauty AU", index=False)

        df_vegetables_sk.to_excel(writer, sheet_name="Vegetables SK", index=False)
        df_fruits_sk.to_excel(writer, sheet_name="Fruits SK", index=False)
        df_bread_sk.to_excel(writer, sheet_name="Bread SK", index=False)
        df_beer_sk.to_excel(writer, sheet_name="Beer SK", index=False)
        df_beauty_sk.to_excel(writer, sheet_name="Beauty SK", index=False)

else:

    print("Az árak és a termékek listái nem azonos hosszúságúak.")


