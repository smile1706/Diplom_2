import allure
import pytest

from generators import *
from methods import user_methods


@pytest.fixture()
@allure.title("Регистрация пользователя, передача данных пользователя в тест и последующее удаление пользователя")
def return_register_data():
    with allure.step("Получение email, password от генератора"):
        email, password = generate_credentials()
    with allure.step("Создание тела запроса для регистрации"):
        register_body = generate_register_body((email, password))
    with allure.step("Передача тела запроса в тест"):
        yield register_body
    with allure.step("Создание тела запроса для аутентификации"):
        auth_body = generate_auth_body((email, password))
    with allure.step("Выполнение запроса аутентификации"):
        auth_response = user_methods.UserMethods.auth_user(auth_body)
    with allure.step("Определение успешной аутентификации"):
        if auth_response.json()['success'] is True:
            with allure.step("Получение accessToken из ответа на запрос"):
                access_token = auth_response.json()['accessToken']
            with allure.step("Создание заголовка запроса с accessToken"):
                auth_header = generate_auth_header(access_token)
            with allure.step("Выполнение запроса на удаление пользователя с переданным accessToken"):
                delete_response = user_methods.UserMethods.delete_user(auth_header)
            with allure.step("Проверка успешного удаления пользователя"):
                assert delete_response.status_code == 202 and delete_response.json()['success'] == True  # проверка успешности запроса
        else:
            with allure.step("Проверка статус-кода ошибки и сообщения при неуспешной авторизации"):
                assert  auth_response.status_code == 401 and auth_response.json()['message'] == 'email or password are incorrect'

@pytest.fixture()
@allure.title("Регистрация пользователя, передача заголовка с accessToken в тест и последующее удаление пользователя")
def return_auth_header_and_create_delete_user_after_tests():
    with allure.step("Получение email, password от генератора"):
        email, password = generate_credentials()
    with allure.step("Создание тела запроса для регистрации"):
        register_body = generate_register_body((email, password)) #создали тело запроса для регистрации
    with allure.step("Выполнение запроса регистрации"):
        register_response = user_methods.UserMethods.register_user(register_body) #запрос для регистрации
    with allure.step("Проверка статус-кода и сообщения при успешной регистрации"):
        assert register_response.status_code == 200 and register_response.json()['success'] == True #проверка успешности запроса
    with allure.step("Получение accessToken из ответа на запрос"):
        access_token = register_response.json()['accessToken']
    with allure.step("Создание заголовка запроса с accessToken"):
        auth_header = generate_auth_header(access_token) #создали заголовок с accessToken
    with allure.step("Передача заголовка запроса в тест"):
        yield auth_header
    with allure.step("Выполнение запроса на удаления пользователя"):
        delete_response = user_methods.UserMethods.delete_user(auth_header) #запрос для удаления
    with allure.step("Проверка успешного удаления пользователя"):
        assert delete_response.status_code == 202 and delete_response.json()['success'] == True #проверка успешности запроса
