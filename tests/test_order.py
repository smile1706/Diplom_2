import allure

from generators import generate_order_body
from methods import order_methods


@allure.epic("Создание заказа")
class TestCreateOrder:
    @allure.title("Создание заказа без авторизации пользователя")
    def test_create_order_not_authorized_fails(self):
        with allure.step("Запрос ингредиентов"):
            ingredients = order_methods.OrderMethods.get_ingredients().json()
        with allure.step("Создание списка ингредиентов для заказа"):
            hash_ids = [ingredients['data'][0]['_id'], ingredients['data'][5]['_id']]
        with allure.step("Создание заказа"):
            response = order_methods.OrderMethods.create_order(order_body=generate_order_body(hash_ids),auth_header="")
        with allure.step("Проверка статус-кода и сообщения"):
            assert response.status_code == 200 and (response.json()['success'] == True)

    @allure.title("Создание заказа с авторизацией пользователя")
    def test_create_order_authorized_successful(self,return_auth_header_and_create_delete_user_after_tests):
        with allure.step("Запрос ингредиентов"):
            ingredients = order_methods.OrderMethods.get_ingredients().json()
        with allure.step("Создание списка ингредиентов для заказа"):
            hash_ids = [ingredients['data'][0]['_id'], ingredients['data'][7]['_id'], ingredients['data'][11]['_id']]
        with allure.step("Создание заказа"):
            response = order_methods.OrderMethods.create_order(generate_order_body(hash_ids),auth_header=return_auth_header_and_create_delete_user_after_tests)
        with allure.step("Проверка статус-кода и сообщения"):
            assert response.status_code == 200 and (response.json()['success'] == True)

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients_successful(self,return_auth_header_and_create_delete_user_after_tests):
        with allure.step("Запрос ингредиентов"):
            ingredients = order_methods.OrderMethods.get_ingredients().json()
        with allure.step("Создание списка ингредиентов для заказа"):
            hash_ids = [ingredients['data'][0]['_id'], ingredients['data'][6]['_id'], ingredients['data'][9]['_id'], ingredients['data'][7]['_id']]
        with allure.step("Создание заказа"):
            response = order_methods.OrderMethods.create_order(generate_order_body(hash_ids),auth_header=return_auth_header_and_create_delete_user_after_tests)
        with allure.step("Проверка статус-кода и сообщения"):
            assert response.status_code == 200 and (response.json()['success'] == True)

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients_fails(self,return_auth_header_and_create_delete_user_after_tests):
        with allure.step("Список ингредиентов пуст"):
            ingredients = []
        with allure.step("Создание заказа"):
            response = order_methods.OrderMethods.create_order(generate_order_body(ingredients), auth_header=return_auth_header_and_create_delete_user_after_tests)
        with allure.step("Проверка статус-кода ошибки и сообщения"):
            assert response.status_code == 400 and (response.json()['success'] == False) and (response.json()['message'] == 'Ingredient ids must be provided')

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_incorrect_ingredients_hash_fails(self,return_auth_header_and_create_delete_user_after_tests):
        with allure.step("Запрос ингредиентов"):
            ingredients = order_methods.OrderMethods.get_ingredients().json()
        with allure.step("Создание списка ингредиентов для заказа"):
            hash_ids = [ingredients['data'][0]['_id'], ingredients['data'][6]['_id']]
        with allure.step("Внесение ошибки в хеш ингредиента для заказа"):
            hash_ids[0] = hash_ids[0] + '123'
        with allure.step("Создание заказа"):
            response = order_methods.OrderMethods.create_order(generate_order_body(hash_ids), auth_header=return_auth_header_and_create_delete_user_after_tests)
        with allure.step("Проверка статус-кода ошибки"):
            assert response.status_code == 500
