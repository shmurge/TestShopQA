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
    PRODUCTS_SEARCH_QUERY = ['Desk', 'Chair', 'Warranty', 'Drawer', 'Box', 'Cabinet', 'Three-Seat Sofa']


class InfoMessage:
    CART_IS_EMPTY = 'Your cart is empty!'

    @staticmethod
    def message_no_results(query):
        return f'No results\nNo results for "{query}".'


class ErrorMessage:
    EMAIL_ALREADY_EXIST = 'Another user is already registered using this email address.'
    PASSWORDS_MISSMATCH = 'Passwords do not match; please retype them.'
    WRONG_LOGIN_OR_PASSWORD = 'Wrong login/password'


class PlaceHolder:
    CREATE_ACCOUNT_FORM_USERNAME_INPUT = 'e.g. John Doe'

    LOGIN_FORM_EMAIL_INPUT = 'Email'
    LOGIN_FORM_PASSWORD_INPUT = 'Password'

    MAIN_PAGE_SEARCH_INPUT = 'Search...'


class ProductInfo:
    CUSTOMIZE_DESK_SHORT_TITLE = 'Customizable Desk'
    T_CUSTOMIZE_DESK_STEEL_WHITE = 'Customizable Desk (Steel, White)'
    T_CUSTOMIZE_DESK_STEEL_BLACK = 'Customizable Desk (Steel, Black)'
    T_CUSTOMIZE_DESK_ALUM_WHITE = 'Customizable Desk (Aluminium, White)'
    T_CUSTOMIZE_DESK_CUSTOM_WHITE = 'Customizable Desk (Custom, White)'
    T_CUSTOMIZE_DESK_CUSTOM_BLACK = 'Customizable Desk (Custom, Black)'
    DESCRIPTION_CUSTOMIZE_DESK = '160x80cm, with large legs.'
    CUSTOMIZE_DESC_DEFAULT_PRICE = '$ 750.00'
    CUSTOMIZE_DESC_ALUMINIUM_PRICE = '$ 800.40'
