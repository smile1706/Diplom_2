import allure
import pytest

from methods import user_methods


@allure.epic("Создание пользователя")
class TestRegisterUser:
    @allure.title("Проверка регистрации уникального пользователя")
    def test_register_new_user_successful(self,return_register_data):
        with allure.step("Регистрация пользователя"):
            response = user_methods.UserMethods.register_user(return_register_data)
        with allure.step("Проверка статус-кода и сообщения"):
            assert response.status_code == 200 and (response.json()['success'] == True)

    @allure.title("Проверка регистрации пользователя, который уже зарегистрирован")
    def test_register_existing_user_fails(self,return_register_data):
        with allure.step("Регистрация пользователя"):
            user_methods.UserMethods.register_user(return_register_data)
        with allure.step("Повторная регистрация пользователя с теми же данными"):
            response = user_methods.UserMethods.register_user(return_register_data)
        with allure.step("Проверка статус-кода ошибки и сообщения"):
            assert response.status_code == 403 and (response.json()['success'] == False) and (response.json()['message'] == 'User already exists')

    @pytest.mark.parametrize('missing_field, expected_message', [
        ('email', 'Email, password and name are required fields'),
        ('password', 'Email, password and name are required fields'),
        ('name', 'Email, password and name are required fields')
    ])
    @allure.title("Проверка регистрации пользователя при одном незаполненном поле из обязательных полей")
    def test_register_user_without_one_field_fails(self,return_register_data,missing_field, expected_message):
        with allure.step(f"Поле '{missing_field}' не заполняется"):
            return_register_data[missing_field] = ''
        with allure.step("Попытка регистрации пользователя"):
            response = user_methods.UserMethods.register_user(return_register_data)
        with allure.step("Проверка статус-кода ошибки и сообщения"):
            assert response.status_code == 403 and (response.json()['success'] == False) and (response.json()['message'] == expected_message)

