
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self,username,password):
     self.username = username
     self.password = password
     self.bot = webdriver.Firefox()

    def login(self):
     bot = self.bot
     bot.get('https://www.instagram.com/')
     time.sleep(3)

     username = bot.find_element_by_name('username')
     password = bot.find_element_by_name('password')
     username.clear()
     password.clear()

     username.send_keys(self.username)
     password.send_keys(self.password)
     password.send_keys(Keys.RETURN)
     time.sleep(3)
    
    
    def Message(self):
     bot = self.bot
     bot.get('https://www.instagram.com/direct/inbox/')
     time.sleep(3)
     bot.find_element_by_class_name('QOqBd qF0y9 Igw0E IwRSH eGOV_ acqo5 _4EzTm').click
     time.sleep(2)
     

     





ksp = InstagramBot( '_sannn_______','$aN151001')
ksp.login()