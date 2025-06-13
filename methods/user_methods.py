import requests

from data import Url


class UserMethods:
    @staticmethod
    def register_user(register_body):
        response = requests.post(f'{Url.BASE_URL}{Url.REGISTER_URL}', json=register_body)
        return response

    @staticmethod
    def auth_user(auth_body):
        response = requests.post(f'{Url.BASE_URL}{Url.AUTH_URL}', json=auth_body)
        return response

    @staticmethod
    def delete_user(auth_header):
        response = requests.delete(f'{Url.BASE_URL}{Url.DELETE_USER_URL}', headers=auth_header)
        return response