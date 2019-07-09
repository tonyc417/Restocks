from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class FootLocker:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.footlocker.com/')
        bot.find_element_by_css_selector('button.c-header-ribbon__link').click()
        # email = bot.find_element_by_id('input_uid')

ed = FootLocker(' ', ' ')
ed.login()