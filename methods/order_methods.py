import requests

from data import Url


class OrderMethods:
    @staticmethod
    def get_ingredients():
        response = requests.get(f'{Url.BASE_URL}{Url.GET_INGREDIENTS_URL}')
        return response

    @staticmethod
    def create_order(order_body,auth_header):
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_ORDER_URL}', json=order_body, headers=auth_header)
        return response
