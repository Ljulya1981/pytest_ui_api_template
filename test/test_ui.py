from selenium.webdriver.common.by import By
import allure
from test.conftest import ui_url


@allure.title("Поиск фильма по названию на кириллице")
@allure.description("Тест позитивный проверяет поиск фильма по названию на кириллице")
@allure.severity("критический")
def test_by_valid_symbol_rus_positive(browser):
    with allure.step("Открытие страницы приложения"):
        browser.get(ui_url)
    with allure.step("Ввод в строку поиска названия фильма на кириллице"):
        browser.find_element(By.NAME, "kp_query").send_keys("Титаник")
    with allure.step("Нажатие на название фильма в выпадающем списка предложенных фильмов"):
        browser.find_element(By.ID, "suggest-item-film-2213").click()
    with allure.step("Проверка результата"):
        assert browser.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "Титаник (1997)"


@allure.title("Поиск фильма по названию из цифр")
@allure.description("Тест позитивный проверяет поиск фильма по названию из цифр")
@allure.severity("критический")
def test_by_valid_symbol_num_positive(browser):
    with allure.step("Открытие страницы приложения"):
        browser.get(ui_url)
    with allure.step("Ввод в строку поиска названия фильма из цифр"):
        browser.find_element(By.NAME, "kp_query").send_keys("2012")
    with allure.step("Нажатие на название фильма в выпадающем списка предложенных фильмов"):
        browser.find_element(By.ID, "suggest-item-film-413447").click()
    with allure.step("Проверка результата"):
        assert browser.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "2012 (2009)"


@allure.title("Поиск фильма по названию на латинице")
@allure.description("Тест позитивный проверяет поиск фильма по названию на латинице")
@allure.severity("критический")
def test_by_valid_symbol_ing_positive(browser):
    with allure.step("Открытие страницы приложения"):
        browser.get(ui_url)
    with allure.step("Ввод в строку поиска названия фильма на латинице"):
        browser.find_element(By.NAME, "kp_query").send_keys("Doom")
    with allure.step("Нажатие на название фильма в выпадающем списка предложенных фильмов"):
        browser.find_element(By.ID, "suggest-item-film-84140").click()
    with allure.step("Проверка результата"):
        assert browser.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "Doom (2005)"


@allure.title("Поиск фильма по несуществующему названию (рандомный набор цифр и латиницы)")
@allure.description("Тест негативный проверяет поиск фильма по несуществующему названию (рандомный набор цифр и латиницы)")
@allure.severity("критический")
def test_by_invalid_symbol_negative(browser):
    with allure.step("Открытие страницы приложения"):
        browser.get(ui_url)
    with allure.step("Ввод в строку поиска рандомного набора цифр и латиницы"):
        browser.find_element(By.NAME, "kp_query").send_keys("1эзен")
    with allure.step("Проверка результата"):
        assert browser.find_element(By.CSS_SELECTOR, ".styles_emptySuggest__XEkB0").text == "По вашему запросу ничего не найдено"


@allure.title("Поиск фильма по несуществующему названию (набор спецсимволов)")
@allure.description("Тест негативный проверяет поиск фильма по несуществующему названию (набор спецсимволов)")
@allure.severity("критический")
def test_by_invalid_symbol_negative_signs(browser):
    with allure.step("Открытие страницы приложения"):
        browser.get(ui_url)
    with allure.step("Ввод в строку поиска набора спецсиволов"):
        browser.find_element(By.NAME, "kp_query").send_keys("*****")
    with allure.step("Проверка результата"):
        assert browser.find_element(By.CSS_SELECTOR, ".styles_emptySuggest__XEkB0").text == "По вашему запросу ничего не найдено"
