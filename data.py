class Url:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    REGISTER_URL = '/api/auth/register'
    DELETE_USER_URL = '/api/auth/user'
    AUTH_URL = '/api/auth/login'
    CREATE_ORDER_URL = '/api/orders'
    GET_INGREDIENTS_URL = '/api/ingredients'


class DataForAuth:
    CREATE_BODY = {
        "email" : "testdipl@yandx.ru",
        "password" : "qscqscqcq"
    }