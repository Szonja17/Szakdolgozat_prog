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


# Oldal betöltése
driver.get("https://www.kozertplusz.hu/")
time.sleep(2)

# Várakozás az elfogadás gomb megjelenésére és kattintás rá
cookie_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[10]/div/div[2]/button'))
)
cookie_button.click()

time.sleep(2)

# Zöldségek kinyerése
# Várakozás a "Bevásárlókosár" ikon megjelenésére és kattintás rá
cart_icon = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[2]/div[3]/div/div[1]/span'))
)
cart_icon.click()

time.sleep(2)
# Várakozás a "Zöldség" menüpontra és kattintás az első lehetőségre
vegetable_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[2]/div[3]/div/div[1]/ul/li[1]/a'))
)
vegetable_menu.click()
time.sleep(2)
# zöldségek megnyitása
vegetable_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[3]/div[2]/div/div[1]/div/div/a'))
)
vegetable_menu.click()
time.sleep(2)
# Várakozás a zöldségek terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "product-title"))
)
time.sleep(2)
product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "price.actual-price"))
)
time.sleep(2)
# Termékek neveinek és árainak kinyerése
product_name_vegetables_hu = [element.text for element in product_name_elements]
product_price_vegetables_hu = [element.text for element in product_price_elements]

time.sleep(2)
# Gyümölcsök kinyerése
# Várakozás a zöldségek, gyümölcsök menüpont betöltésére
vegetable_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[1]/ul/li[2]/a'))
)
vegetable_menu.click()
time.sleep(2)
fruit_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[3]/div[2]/div/div[2]/div'))
)
fruit_menu.click()
time.sleep(2)
# Várakozás a gyümölcsök terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "product-title"))
)
time.sleep(2)
product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "price.actual-price"))
)
time.sleep(2)
# Termékek neveinek és árainak kinyerése
product_name_fruits_hu = [element.text for element in product_name_elements]
product_price_fruits_hu = [element.text for element in product_price_elements]
time.sleep(2)

# Tejek kinyerése
# Várakozás a "Bevásárlókosár" ikon megjelenésére és kattintás rá
cart_icon = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[2]/div[3]/div/div[1]/span'))
)
cart_icon.click()
time.sleep(2)
# Várakozás a "Tektermékek, sajt és tojás" menüpontra
milkprod_menu = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[2]/div[3]/div/div[1]/ul/li[2]/a'))
)
milkprod_menu.click()
time.sleep(2)
# Tejek megnyitása
milk_menu = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[3]/div[3]/div[1]/div[3]/a'))
)
milk_menu.click()
time.sleep(2)
# Várakozás a tejek terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "product-title"))
)
time.sleep(2)
product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "price.actual-price"))
)
time.sleep(2)
# Termékek neveinek és árainak kinyerése
product_name_milk_hu = [element.text for element in product_name_elements]
product_price_milk_hu = [element.text for element in product_price_elements]

time.sleep(2)
# Sajtok kinyerése
# Visszalépés a tejtermékek, sajtok és tojások menüpontra
milkprod_menu = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[1]/ul/li[2]/a'))
)
milkprod_menu.click()
time.sleep(3)
# Sajtok megnyitása
milk_menu = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[3]/div[2]/div/div[9]/div'))
)
milk_menu.click()
time.sleep(3)
# Várakozás a sajtok terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "product-title"))
)
time.sleep(2)
product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "price.actual-price"))
)
time.sleep(2)
# Termékek neveinek és árainak kinyerése
product_name_cheese_hu = [element.text for element in product_name_elements]
product_price_cheese_hu = [element.text for element in product_price_elements]

#Vajak
# Visszalépés a tejtermékek, sajtok és tojások menüpontra
milkprod_menu = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[1]/ul/li[2]/a'))
)
milkprod_menu.click()
time.sleep(3)
# Vajak megnyitása
butter_menu = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[3]/div[2]/div/div[6]/div'))
)
butter_menu.click()
# Várakozás a vajak terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "product-title"))
)
time.sleep(2)
product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "price.actual-price"))
)
time.sleep(2)
# Termékek neveinek és árainak kinyerése
product_name_butter_hu = [element.text for element in product_name_elements]
product_price_butter_hu = [element.text for element in product_price_elements]

#Tojás
# Visszalépés a tejtermékek, sajtok és tojások menüpontra
milkprod_menu = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[1]/ul/li[2]/a'))
)
milkprod_menu.click()
time.sleep(3)

# Tojás megnyitása
egg_menu = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[3]/div[2]/div/div[10]/div'))
)
egg_menu.click()
# Várakozás a vajak terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "product-title"))
)
time.sleep(2)
product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "price.actual-price"))
)
time.sleep(2)
# Termékek neveinek és árainak kinyerése
product_name_egg_hu = [element.text for element in product_name_elements]
product_price_egg_hu = [element.text for element in product_price_elements]

# Husok
# Cart megnyitása
cart_icon = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[2]/div[3]/div/div[1]/span'))
)
cart_icon.click()
time.sleep(2)
# Várakozás a "Húsok és halak" menüpontra
meat_menu = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[2]/div[3]/div/div[1]/ul/li[3]'))
)
meat_menu.click()

time.sleep(3)
# Várakozás a húsok terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "product-title"))
)
time.sleep(2)
product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "price.actual-price"))
)
time.sleep(2)
# Termékek neveinek és árainak kinyerése
product_name_meat_hu = [element.text for element in product_name_elements]
product_price_meat_hu = [element.text for element in product_price_elements]

time.sleep(2)

# Kenyerek
# Cart megnyitása
cart_icon = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[2]/div[3]/div/div[1]/span'))
)
cart_icon.click()
time.sleep(2)
# Várakozás a "Pékáru" menüpontra
bread_menu = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[2]/div[3]/div/div[1]/ul/li[4]'))
)
bread_menu.click()
time.sleep(2)
# Rákattintás a kenyerek menüpontra
breads_menu = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[3]/div[3]/div[1]/div[3]/a'))
)
breads_menu.click()

time.sleep(3)
# Várakozás a kenyerek terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "product-title"))
)
time.sleep(2)
product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "price.actual-price"))
)
time.sleep(2)
# Termékek neveinek és árainak kinyerése
product_name_bread_hu = [element.text for element in product_name_elements]
product_price_bread_hu = [element.text for element in product_price_elements]

time.sleep(2)

#Tesztak
# Menu megnyitása
cart_icon = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[2]/div[3]/div/div[1]/span'))
)
cart_icon.click()
time.sleep(2)
# Várakozás a "Tartós termékek" menüpontra
food_menu = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[2]/div[3]/div/div[1]/ul/li[6]/a'))
)
food_menu.click()
time.sleep(3)
# Várakozás a "Sütés-főzés" menüpontra
cook_menu = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[3]/div[2]/div[2]/div[3]'))
)
cook_menu.click()
time.sleep(3)

# Várakozás a "Tészták" menüpontra
pasta_menu = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[3]/div[1]/div/div[8]/div'))
)
pasta_menu.click()
time.sleep(3)

# Várakozás a tészták terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "product-title"))
)
time.sleep(2)
product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "price.actual-price"))
)
time.sleep(2)
# Termékek neveinek és árainak kinyerése
product_name_pasta_hu = [element.text for element in product_name_elements]
product_price_pasta_hu = [element.text for element in product_price_elements]

time.sleep(2)

#Alkohol
# Menu megnyitása
cart_icon = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[2]/div[3]/div/div[1]/span'))
)
cart_icon.click()
time.sleep(2)
# Várakozás a "Italok" menüpontra
drink_menu = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[2]/div[3]/div/div[1]/ul/li[5]'))
)
drink_menu.click()
time.sleep(3)
# Várakozás a "Alkoholok" menüpontra
alcohol_menu = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[3]/div[1]/div/div[1]/div'))
)
alcohol_menu.click()
time.sleep(3)

# Várakozás a "Sörök" menüpontra
beer_menu = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[4]/div[5]/div[1]/div/div[3]/div[1]/div/div[2]'))
)
beer_menu.click()
time.sleep(3)

# Várakozás a sörök terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "product-title"))
)
time.sleep(2)
product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "price.actual-price"))
)
time.sleep(2)
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

def scroll_to_bottom(driver):
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

# Várakozás a beauty terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 30).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "product-title"))
)
time.sleep(2)
product_price_elements = WebDriverWait(driver, 30).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "price.actual-price"))
)
time.sleep(2)

# Termékek neveinek és árainak kinyerése
product_name_beauty_hu = [element.text for element in product_name_elements]
product_price_beauty_hu = [element.text for element in product_price_elements]

time.sleep(2)

# WebDriver leállítása
driver.quit()

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


def scroll_to_bottom(driver):
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


# Tesztelés
# Itt feltételezzük, hogy a "driver" egy Selenium WebDriver példány
scroll_to_bottom(driver)

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
product_name_vegetables_au = [element.text for element in product_name_elements]
product_price_vegetables_au = [element.text for element in product_price_elements]

time.sleep(2)

# Gyümölcsök kinyerése
# Gyümölcsök menüpontra való kattintás
fruit_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[1]/div/ul/li[2]/div/a'))
)
fruit_menu.click()

time.sleep(2)


def scroll_to_bottom(driver):
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


# Tesztelés
# Itt feltételezzük, hogy a "driver" egy Selenium WebDriver példány
scroll_to_bottom(driver)

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
product_name_fruits_au = [element.text for element in product_name_elements]
product_price_fruits_au = [element.text for element in product_price_elements]

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


def scroll_to_bottom(driver):
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


# Tesztelés
# Itt feltételezzük, hogy a "driver" egy Selenium WebDriver példány
scroll_to_bottom(driver)

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
product_name_milk_au = [element.text for element in product_name_elements]
product_price_milk_au = [element.text for element in product_price_elements]

time.sleep(2)


# Sajtok kinyerése
# A sajtokra kattintás
cheese_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[3]/div/ul/li[2]/div/a'))
)
cheese_menu.click()
time.sleep(2)


def scroll_to_bottom(driver):
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


# Tesztelés
# Itt feltételezzük, hogy a "driver" egy Selenium WebDriver példány
scroll_to_bottom(driver)

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
product_name_cheese_au = [element.text for element in product_name_elements]
product_price_cheese_au = [element.text for element in product_price_elements]
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


def scroll_to_bottom(driver):
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


# Tesztelés
# Itt feltételezzük, hogy a "driver" egy Selenium WebDriver példány
scroll_to_bottom(driver)

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
product_name_butter_au = [element.text for element in product_name_elements]
product_price_butter_au = [element.text for element in product_price_elements]
time.sleep(2)

#Tojások kinyerése
# A tojásokra kattintás
egg_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-category-menu/div/div[2]/div[3]/ul/li[3]/div/ul/li[5]/div/a'))
)
egg_menu.click()
time.sleep(2)


def scroll_to_bottom(driver):
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
# Tesztelés
# Itt feltételezzük, hogy a "driver" egy Selenium WebDriver példány
scroll_to_bottom(driver)

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
product_name_egg_au = [element.text for element in product_name_elements]
product_price_egg_au = [element.text for element in product_price_elements]
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


def scroll_to_bottom(driver):
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


# Tesztelés
# Itt feltételezzük, hogy a "driver" egy Selenium WebDriver példány
scroll_to_bottom(driver)

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
product_name_pasta_au = [element.text for element in product_name_elements]
product_price_pasta_au = [element.text for element in product_price_elements]
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


def scroll_to_bottom(driver):
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


# Tesztelés
# Itt feltételezzük, hogy a "driver" egy Selenium WebDriver példány
scroll_to_bottom(driver)


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
product_name_meat_au = [element.text for element in product_name_elements]
product_price_meat_au = [element.text for element in product_price_elements]
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


def scroll_to_bottom(driver):
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


# Tesztelés
# Itt feltételezzük, hogy a "driver" egy Selenium WebDriver példány
scroll_to_bottom(driver)


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
product_name_bread_au = [element.text for element in product_name_elements]
product_price_bread_au = [element.text for element in product_price_elements]
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


def scroll_to_bottom(driver):
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


# Tesztelés
# Itt feltételezzük, hogy a "driver" egy Selenium WebDriver példány
scroll_to_bottom(driver)

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
product_name_beer_au = [element.text for element in product_name_elements]
product_price_beer_au = [element.text for element in product_price_elements]
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
cart_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[6]/button[1]'))
)
cart_button.click()

time.sleep(2)

# Felugró fül kiikszelése
cart_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div/span'))
)
cart_button.click()

time.sleep(2)

# Húsok
# Húsokra kattintás
meat_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/header/div[2]/nav/ul/li[4]/a/span/img'))
)
meat_button.click()

time.sleep(2)

# Szárnyasok menüpont
winged_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[1]/a'))
)
winged_button.click()
time.sleep(2)


# Várakozás a szárnyasok terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
)
time.sleep(2)

product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
)
time.sleep(2)

# Termékek neveinek és árainak kinyerése
product_name_meat = [element.text for element in product_name_elements]
product_price_meat = [element.text for element in product_price_elements]
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
            EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
        )

        # Termékek neveinek és árainak kinyerése
        product_name_meat += [element.text for element in product_name_elements]
        product_price_meat += [element.text for element in product_price_elements]

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
milk_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/header/div[2]/nav/ul/li[5]/a/span/img'))
)
milk_button.click()
time.sleep(2)

# Tojásokra kattintás
egg_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[4]/a'))
)
egg_button.click()
time.sleep(2)

# Várakozás a tojások terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
)
time.sleep(2)

product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
)
time.sleep(2)

# Termékek neveinek és árainak kinyerése
product_name_egg = [element.text for element in product_name_elements]
product_price_egg = [element.text for element in product_price_elements]
time.sleep(2)

# Tejek
# Visszalépés a tejtermékekre
diary_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/a[2]'))
)
diary_button.click()
time.sleep(2)

#Tejekre való kattintás
milk_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[2]/a'))
)
milk_button.click()
time.sleep(2)

# Várakozás a tejek terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
)
time.sleep(2)

product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
)
time.sleep(2)

# Termékek neveinek és árainak kinyerése
product_name_milk = [element.text for element in product_name_elements]
product_price_milk = [element.text for element in product_price_elements]
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
            EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
        )

        # Termékek neveinek és árainak kinyerése
        product_name_milk += [element.text for element in product_name_elements]
        product_price_milk += [element.text for element in product_price_elements]

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
diary_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/a[2]'))
)
diary_button.click()
time.sleep(2)

#Vajakra kattintás
butter_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[6]/a'))
)
butter_button.click()
time.sleep(2)

# Várakozás a vajak terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
)
time.sleep(2)

product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
)
time.sleep(2)

# Termékek neveinek és árainak kinyerése
product_name_butter = [element.text for element in product_name_elements]
product_price_butter = [element.text for element in product_price_elements]
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
            EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
        )

        # Termékek neveinek és árainak kinyerése
        product_name_butter += [element.text for element in product_name_elements]
        product_price_butter += [element.text for element in product_price_elements]

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
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
)
time.sleep(2)

product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
)
time.sleep(2)

# Termékek neveinek és árainak kinyerése
product_name_pasta = [element.text for element in product_name_elements]
product_price_pasta = [element.text for element in product_price_elements]
time.sleep(2)

#Zöldségek
#Zöldségek menüpontra kattintás
vegetable_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/header/div[2]/nav/ul/li[2]/a'))
)
vegetable_button.click()
time.sleep(2)

#Saláta
salad_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[1]/a'))
)
salad_button.click()
time.sleep(2)

# Várakozás a vajak terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
)
time.sleep(2)

product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
)
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
            EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
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
salad_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/a[2]'))
)
salad_button.click()
time.sleep(2)

#Hagyma menüpontra lépés
onion_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[4]/a'))
)
onion_button.click()
time.sleep(2)

# Várakozás a keressé eredményének terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
)
time.sleep(2)

product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
)
time.sleep(2)

# Termékek neveinek és árainak kinyerése
product_name_vegetable_sk += [element.text for element in product_name_elements]
product_price_vegetable_sk += [element.text for element in product_price_elements]
time.sleep(2)

#Répa
#Visszalépés a zöldségek menüpontra
salad_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/a[2]'))
)
salad_button.click()
time.sleep(2)

#Belépés a répákhoz
carrot_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[5]/a'))
)
carrot_button.click()
time.sleep(2)

# Várakozás a répák terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
)
time.sleep(2)

product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
)
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
            EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
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
salad_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/a[2]'))
)
salad_button.click()
time.sleep(2)

#Belépés a paradicsomokhoz
fresh_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[3]/a'))
)
fresh_button.click()
time.sleep(2)

# Várakozás a paradicsomok terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
)
time.sleep(2)

product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
)
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
            EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
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
fruit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/header/div[2]/nav/ul/li[1]/a'))
)
fruit_button.click()
time.sleep(2)

#Alma
fruit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[1]/a'))
)
fruit_button.click()
time.sleep(2)

# Várakozás a keressé eredményének terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
)
time.sleep(2)

product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
)
time.sleep(2)

# Termékek neveinek és árainak kinyerése
product_name_fruit_sk = [element.text for element in product_name_elements]
product_price_fruit_sk = [element.text for element in product_price_elements]
time.sleep(2)

#Szőlő
#Visszalépés a fő menübe
fruit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/a[2]'))
)
fruit_button.click()
time.sleep(2)

#Szőlők menüpont
grape_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[3]/a'))
)
grape_button.click()
time.sleep(2)

# Várakozás a keressé eredményének terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
)
time.sleep(2)

product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
)
time.sleep(2)

# Termékek neveinek és árainak kinyerése
product_name_fruit_sk += [element.text for element in product_name_elements]
product_price_fruit_sk += [element.text for element in product_price_elements]
time.sleep(2)

#Banán
#Visszalépés a fő menübe
fruit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/a[2]'))
)
fruit_button.click()
time.sleep(2)

#Belépés az egzotikus gyümölcsökbe
fruit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[7]/a'))
)
fruit_button.click()
time.sleep(2)

# Várakozás a paradicsomok terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
)
time.sleep(2)

product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
)
time.sleep(2)

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
            EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
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
fruit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/a[2]'))
)
fruit_button.click()
time.sleep(2)

#Belépés a citrusokba
fruit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[6]/a'))
)
fruit_button.click()
time.sleep(2)

# Várakozás a keressé eredményének terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
)
time.sleep(2)

product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
)
time.sleep(2)

# Termékek neveinek és árainak kinyerése
product_name_fruit_sk += [element.text for element in product_name_elements]
product_price_fruit_sk += [element.text for element in product_price_elements]
time.sleep(2)

#Péksütik
#Belépés a péksüteményekbe
bread_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/header/div[2]/nav/ul/li[3]/a'))
)
bread_button.click()
time.sleep(2)

bread_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[1]/a'))
)
bread_button.click()
time.sleep(2)

# Várakozás a keressé eredményének terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
)
time.sleep(2)

product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
)
time.sleep(2)

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
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
)
time.sleep(2)

product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
)
time.sleep(2)

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
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
)
time.sleep(2)

product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
)
time.sleep(2)

# Termékek neveinek és árainak kinyerése
product_name_bread_sk += [element.text for element in product_name_elements]
product_price_bread_sk += [element.text for element in product_price_elements]
time.sleep(2)

#Sörök
#Kattintás az italok menüpontra
drink_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/header/div[2]/nav/ul/li[8]/a'))
)
drink_button.click()
time.sleep(2)

#Kattintás a sörök menüpontra
beer_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[2]/a'))
)
beer_button.click()
time.sleep(2)

# Várakozás a terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
)
time.sleep(2)

product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
)
time.sleep(2)

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
            EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
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
hygen_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/header/div[2]/nav/ul/li[11]/a'))
)
hygen_button.click()
time.sleep(2)

#Intim higénia
intim_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[8]/a'))
)
intim_button.click()
time.sleep(2)

# Várakozás a terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
)
time.sleep(2)

product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
)
time.sleep(2)

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
            EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
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
hygen_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/a[2]'))
)
hygen_button.click()
time.sleep(2)

#Belépés a mosószer menübe
hygen_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[10]/a'))
)
hygen_button.click()
time.sleep(2)

# Várakozás a terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
)
time.sleep(2)

product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
)
time.sleep(2)

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
            EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
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
hygen_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div/div/a[2]'))
)
hygen_button.click()
time.sleep(2)

#Száj higénia
hygen_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[2]/a'))
)
hygen_button.click()
time.sleep(2)

# Várakozás a terméknevek és árak betöltésére
product_name_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--title"))
)
time.sleep(2)

product_price_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
)
time.sleep(2)
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
            EC.presence_of_all_elements_located((By.CLASS_NAME, "woodetail--price"))
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

csirkemell_products = [(name, price) for name, price in zip(product_name_meat, product_price_meat) if 'prsia' and '500' in name]
tojas_products = [(name, price) for name, price in zip(product_name_egg, product_price_egg) if '10' in name]
vaj_products = [(name, price) for name, price in zip(product_name_butter, product_price_butter) if '200' in name]
tej_products = [(name, price) for name, price in zip(product_name_milk, product_price_milk) if 'mlieko' in name.lower()]
teszta_products = [(name, price) for name, price in zip(product_name_pasta, product_price_pasta)]



# Ha vannak megfelelo termekek, akkor mentés
if csirkemell_products_hu:
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

    csirkemell = pd.DataFrame({"Product Name": [item[0] for item in csirkemell_products],
                               "Product Price": [item[1] for item in csirkemell_products]})
    # Duplikációk eltávolítása
    csirkemell_sk = pd.DataFrame({"Product Name": [item[0] for item in csirkemell_products],
                               "Product Price": [item[1] for item in csirkemell_products]})

    csirkemell_sk.drop_duplicates(inplace=True)

    tojas_sk = pd.DataFrame({"Product Name": [item[0] for item in tojas_products],
                          "Product Price": [item[1] for item in tojas_products]})
    tojas_sk.drop_duplicates(inplace=True)

    vaj_sk = pd.DataFrame({"Product Name": [item[0] for item in vaj_products],
                        "Product Price": [item[1] for item in vaj_products]})
    vaj_sk.drop_duplicates(inplace=True)

    tej_sk = pd.DataFrame({"Product Name": [item[0] for item in tej_products],
                        "Product Price": [item[1] for item in tej_products]})
    tej_sk.drop_duplicates(inplace=True)

    teszta_sk = pd.DataFrame({"Product Name": [item[0] for item in teszta_products],
                           "Product Price": [item[1] for item in teszta_products]})
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
        df_bread_hu.to_excel(writer, sheet_name="Beer HU", index=False)
        df_beauty_hu.to_excel(writer, sheet_name="Beauty HU", index=False)

        df_vegetables_au.to_excel(writer, sheet_name="Vegetables AU", index=False)
        df_fruits_au.to_excel(writer, sheet_name="Fruits AU", index=False)
        df_bread_au.to_excel(writer, sheet_name="Bread AU", index=False)
        df_bread_au.to_excel(writer, sheet_name="Beer AU", index=False)
        df_beauty_au.to_excel(writer, sheet_name="Beauty AU", index=False)

        df_vegetables_sk.to_excel(writer, sheet_name="Vegetables SK", index=False)
        df_fruits_sk.to_excel(writer, sheet_name="Fruits SK", index=False)
        df_bread_sk.to_excel(writer, sheet_name="Bread SK", index=False)
        df_beer_sk.to_excel(writer, sheet_name="Beer SK", index=False)
        df_beauty_sk.to_excel(writer, sheet_name="Beauty SK", index=False)


else:

    print("Az árak és a termékek listái nem azonos hosszúságúak.")


