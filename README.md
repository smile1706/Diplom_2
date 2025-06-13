## Дипломный проект. Задание 2: API-тесты
<hr>

## Студент: Муталлапов Динар

## <h>Когорта: #21</h>
<hr>

## <h>Project: Stellar Burgers API</h>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты:</h>

> pytest -v

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve allure_results


<hr>

<h3 align="left" style="color:green">Project files and description:</h3>

| Название файла        | Содержание файла                  |
|-----------------------|-----------------------------------|
| tests dir             | Директория с тестами              |
| test_auth_user.py     | Тесты на авторизацию пользователя |
| test_order.py         | Тесты на оформление заказа        |
| test_register_user.py | Тесты на регистрацию пользователя |
| conftest.py           | Фикстуры                          |
| methods dir           | Директория с методами             |
| order_methods.py      | http клиент к order методам       |
| user_methods.py       | http клиент к user методам        |
| generators.py         | Генератор данных и body запросов  |
| data.py               | Файл с URL и данными пользователя |
| requirements.txt      | Файл с зависимостями              |
| allure_results dir    | Папка с отчетами Allure           |


