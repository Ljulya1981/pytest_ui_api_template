import pytest
from selenium import webdriver


ui_url = "https://www.kinopoisk.ru/"
base_url = "https://kinopoiskapiunofficial.tech"
json = {
      "X-API-KEY": "693bc6bc-a1d8-476e-ba60-6d23ab3518b7"
    }


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(50)
    browser.maximize_window()
    yield browser

    browser.quit()
