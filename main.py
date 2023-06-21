import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from telegram_bot import TelegramBot
from mongodb import MongoDB
chrome_driver = webdriver.Chrome()

bot = TelegramBot()
db = MongoDB()


chrome_driver.get("http://www.solominis.com.ec/")
print(chrome_driver.title)

topics = [
    "KIT PLUMAS CROMO",
    "JUEGO DE AROS DUNLOP",
    "RAMPAS DE TRACCION"
]

for t in topics:
    search_box = chrome_driver.find_element(By.ID, "shop_search_field")
    search_box.send_keys(t)
    search_button = chrome_driver.find_element(By.CSS_SELECTOR, '#ja-col1 > div > div:nth-child(1) > table > tbody > tr:nth-child(2) > td > form > input.button')
    search_button.click()

    content = chrome_driver.find_element(By.ID, "vmMainPage")
    print(content.text)
    text = content.text
    text = text[:4000]
    bot.send_tg_message(text)
    db.insert_solominis_text(title=t, text=text)
    time.sleep(2)
    chrome_driver.get("http://www.solominis.com.ec/")


print("fin")
chrome_driver.close()
