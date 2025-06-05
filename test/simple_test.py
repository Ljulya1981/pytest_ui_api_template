from time import sleep
from AuthPage import AuthPage


def first_test(browser):
    auth_page = AuthPage(browser)
    auth_page.go()


    sleep(5)
