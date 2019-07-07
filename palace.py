from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class PalaceBot: 
    def __init__(self):
        self.bot = webdriver.Firefox()

    def add_item(self):
        bot = self.bot
        bot.get('https://shop-usa.palaceskateboards.com/')
        items = bot.find_elements_by_class_name('product-link')
        links = [elem.get_attribute('href') for elem in items]
        print(links)
        for link in links:
            bot.get(link)
            try:
                bot.find_element_by_class_name('cart-btn').click()
                time.sleep(10)
            except Exception as ex:
                time.sleep(60)


ed = PalaceBot()
ed.add_item()