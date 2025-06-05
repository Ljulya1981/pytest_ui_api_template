from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class AuthPage:

    def __init__(self, driver: WebDriver):
        self.__url = "https://www.kinopoisk.ru/"
        self.__driver = driver

    def go(self):
        self.__driver.get(self.__url)
