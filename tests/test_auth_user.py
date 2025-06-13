import allure
import pytest

from methods import user_methods
from data import *

@allure.epic("Логин пользователя")
class TestAuthUser:
    @allure.title("Вход под существующим пользователем")
    def test_auth_exist_user_successful(self):
        with allure.step("Авторизация с существующими данными"):
            response = user_methods.UserMethods.auth_user(DataForAuth.CREATE_BODY)
        with allure.step("Проверка статус-кода и сообщения"):
            assert response.status_code == 200 and (response.json()['success'] == True)

    @pytest.mark.parametrize('incorrect_field, expected_message', [
        ('password', 'email or password are incorrect'),
        ('email', 'email or password are incorrect')
    ])
    @allure.title("Вход с неверным логином и паролем")
    def test_auth_user_with_incorrect_credentials_fails(self,incorrect_field, expected_message):
        with allure.step(f"Изменение данных ключа '{incorrect_field}'"):
            incorrect_data_body = DataForAuth.CREATE_BODY.copy()
            incorrect_data_body[incorrect_field] = 'edited_field'
        with allure.step("Попытка авторизации с измененными данными"):
            response = user_methods.UserMethods.auth_user(incorrect_data_body)
        with allure.step("Проверка статус-кода ошибки и сообщения"):
            assert response.status_code == 401 and (response.json()['success'] == False) and (response.json()['message'] == expected_message)
