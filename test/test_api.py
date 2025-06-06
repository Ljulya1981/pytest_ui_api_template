import allure
import requests
import pytest
from conftest import base_url, json

@pytest.mark.api
@allure.title("Получение списка фильмов")
@allure.description("Тест позитивный проверяет получение списка фильмов")
@allure.severity("критический")
def test_get_films():
    with allure.step("Отправка запроса"):
        response = requests.get(base_url + "/api/v2.2/films", headers=json)
    with allure.step("Проверка результата"):
        assert response.status_code == 200


@pytest.mark.api
@allure.title("Поиск фильма по id")
@allure.description("Тест позитивный проверяет поиск фильма по id")
@allure.severity("критический")
def test_get_film_by_id():
    with allure.step("Отправка запроса "):
        response = requests.get(base_url + "/api/v2.2/films/674243", headers=json)
    with allure.step("Проверка результата"):
        assert response.status_code == 200


@pytest.mark.api
@allure.title("Поиск фактов о фильме по id")
@allure.description("Тест позитивный проверяет поиск фактов о фильме по id")
@allure.severity("критический")
def test_get_filmfact_by_id():
    with allure.step("Отправка запроса "):
        response = requests.get(base_url + "/api/v2.2/films/674243/facts", headers=json)
    with allure.step("Проверка результата"):
        assert response.status_code == 200


@pytest.mark.api
@allure.title("Получение списка фильмов без ключа")
@allure.description("Тест негативный проверяет получение списка фильмов без ключа")
@allure.severity("критический")
def test_get_films_negative():
    with allure.step("Отправка запроса "):
        response = requests.get(base_url + "/api/v2.2/films")
    with allure.step("Проверка результата"):
        assert response.status_code == 401


@pytest.mark.api
@allure.title("Поиск фильма по несуществующему id")
@allure.description("Тест негативный проверяет поиск фильма по несуществующему id")
@allure.severity("критический")
def test_get_film_by_id_negative():
    with allure.step("Отправка запроса "):
        response = requests.get(base_url + "/api/v2.2/films/6", headers=json)
    with allure.step("Проверка результата"):
        assert response.status_code == 404
