from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from urllib.parse import urlparse
import pandas as pd
import time

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

#tortilla
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
csirkemell_products = [(name, price) for name, price in zip(product_name_meat, product_price_meat) if 'prsia' and '500' in name]
tojas_products = [(name, price) for name, price in zip(product_name_egg, product_price_egg) if '10' in name]
vaj_products = [(name, price) for name, price in zip(product_name_butter, product_price_butter) if '200' in name]
tej_products = [(name, price) for name, price in zip(product_name_milk, product_price_milk) if 'mlieko' in name.lower()]
teszta_products = [(name, price) for name, price in zip(product_name_pasta, product_price_pasta)]


# Ha vannak megfelelo termekek, akkor mentés
if csirkemell_products:
    csirkemell = pd.DataFrame({"Product Name": [item[0] for item in csirkemell_products],
                                "Product Price": [item[1] for item in csirkemell_products]})
    # Duplikációk eltávolítása
    csirkemell.drop_duplicates(inplace=True)

    tojas = pd.DataFrame({"Product Name": [item[0] for item in tojas_products],
                               "Product Price": [item[1] for item in tojas_products]})
    tojas.drop_duplicates(inplace=True)

    vaj = pd.DataFrame({"Product Name": [item[0] for item in vaj_products],
                               "Product Price": [item[1] for item in vaj_products]})
    vaj.drop_duplicates(inplace=True)

    tej = pd.DataFrame({"Product Name": [item[0] for item in tej_products],
                        "Product Price": [item[1] for item in tej_products]})
    tej.drop_duplicates(inplace=True)

    teszta = pd.DataFrame({"Product Name": [item[0] for item in teszta_products],
                        "Product Price": [item[1] for item in teszta_products]})
    teszta.drop_duplicates(inplace=True)

    # Mentés külön munkalapra
    with pd.ExcelWriter("kutatas_sk.xlsx", engine="xlsxwriter") as writer:
        csirkemell.to_excel(writer, sheet_name="Chicken breast", index=False)
        tojas.to_excel(writer, sheet_name="Egg", index=False)
        vaj.to_excel(writer, sheet_name="Butter", index=False)
        tej.to_excel(writer, sheet_name="Milk", index=False)
        teszta.to_excel(writer, sheet_name="Spaghetti", index=False)


# WebDriver leállítása
driver.quit()

# Adatok összefűzése
product_name_all = ( product_name_vegetable_sk + product_name_fruit_sk + product_name_bread_sk + product_name_hygen_sk
                     + product_name_beer_sk)
product_price_all = ( product_price_vegetable_sk + product_price_fruit_sk + product_price_bread_sk + product_price_hygen_sk
                      + product_name_beer_sk)

# Ellenőrzés: azonos hosszúságú-e a termékek neveinek és árainak listája
if len(product_name_all) == len(product_price_all):
    # Adatkeretek létrehozása
    df_all = pd.DataFrame({"Product Name": product_name_all, "Product Price": product_price_all})

    # Duplikációk eltávolítása
    df_all.drop_duplicates(inplace=True)

    # Adatkeretek mentése külön munkalapokra egyetlen Excel fájlban
    with pd.ExcelWriter("products_sk.xlsx", engine="xlsxwriter") as writer:

        df_vegetable_sk = df_all[df_all["Product Name"].isin(product_name_vegetable_sk)]
        df_fruit_sk = df_all[df_all["Product Name"].isin(product_name_fruit_sk)]
        df_bread_sk = df_all[df_all["Product Name"].isin(product_name_bread_sk)]
        df_beer_sk = df_all[df_all["Product Name"].isin(product_name_beer_sk)]
        df_hygen_sk = df_all[df_all["Product Name"].isin(product_name_hygen_sk)]


        df_vegetable_sk.to_excel(writer, sheet_name="Vegetables SK", index=False)
        df_fruit_sk.to_excel(writer, sheet_name="Fruits SK", index=False)
        df_bread_sk.to_excel(writer, sheet_name="Bread SK", index=False)
        df_beer_sk.to_excel(writer, sheet_name="Beer SK", index=False)
        df_hygen_sk.to_excel(writer, sheet_name="Beauty SK", index=False)


else:
    print("Az árak és a termékek listái nem azonos hosszúságúak.")







