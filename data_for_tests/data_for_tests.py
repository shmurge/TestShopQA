import os
from dotenv import load_dotenv
from faker import Faker

fake = Faker()
load_dotenv()


class UserData:
    LOGIN = os.getenv('LOGIN')
    PASSWORD = os.getenv('PASSWORD')
    USERNAME = os.getenv('USERNAME')


class InputData:
    USERNAME = f'{fake.first_name()} {fake.last_name()}'
    VALID_EMAIL = fake.email()
    VALID_PASSWORD = fake.password(length=8, lower_case=True, upper_case=True, digits=True, special_chars=True)


class ErrorMessage:
    EMAIL_ALREADY_EXIST = 'Another user is already registered using this email address.'
    PASSWORDS_MISSMATCH = 'Passwords do not match; please retype them.'


class PlaceHolder:
    CREATE_ACCOUNT_USERNAME_INPUT = 'e.g. John Doe'