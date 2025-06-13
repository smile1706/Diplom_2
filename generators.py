from faker import Faker


fake = Faker()

def generate_credentials():
    email = fake.email(domain='yandx.ru')
    password = fake.password(length=8)
    return email, password

# Генерация данных для регистрации
def generate_register_body(user_credentials):
    email, password = user_credentials
    return {
        "email": email,
        "password": password,
        "name": fake.user_name()
    }

def generate_auth_body(user_credentials_tuple):
    (email, password) = user_credentials_tuple
    return {
        "email": email,
        "password": password
    }

def generate_auth_header(access_token):
    return {
        "Authorization": access_token
    }

def generate_order_body(hash_ids):
    return {
        "ingredients": hash_ids
    }
