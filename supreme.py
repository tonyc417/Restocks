from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class SupremeBot: 
    def __init__(self):
        self.bot = webdriver.Firefox()

    def shop(self):
        bot = self.bot
        bot.get('https://www.supremenewyork.com/shop/all/jackets')
        items = bot.find_elements_by_css_selector('a.name-link')
        links = [elem.get_attribute('href') for elem in items]
        print(links)

ed = SupremeBot()
ed.shop()
