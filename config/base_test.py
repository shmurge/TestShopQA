import pytest

from pages.account_page import AccountPage
from pages.cart_page import CartPage
from pages.create_account_page import CreateAccountPage
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.modal_add_to_cart import ModalAddToCart
from pages.product_page import ProductPage


class BaseTest:
    account_page = AccountPage
    cart_page = CartPage
    create_account_page = CreateAccountPage
    header_page = HeaderPage
    login_page = LoginPage
    main_page = MainPage
    modal_add_to_cart = ModalAddToCart
    product_page = ProductPage

    @pytest.fixture(autouse=True)
    def setup(self, request, browser):
        request.cls.browser = browser

        request.cls.account_page = AccountPage(browser)
        request.cls.cart_page = CartPage(browser)
        request.cls.create_account_page = CreateAccountPage(browser)
        request.cls.header_page = HeaderPage(browser)
        request.cls.login_page = LoginPage(browser)
        request.cls.main_page = MainPage(browser)
        request.cls.modal_add_to_cart = ModalAddToCart(browser)
        request.cls.product_page = ProductPage(browser)
