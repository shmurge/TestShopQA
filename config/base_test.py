import pytest
# from pages.header_page import HeaderPage
from pages.create_account_page import CreateAccountPage
# from pages.account_page import AccountPage
# from pages.main_page import MainPage
from pages.login_page import LoginPage


class BaseTest:
    # header_page = HeaderPage
    create_account_page = CreateAccountPage
    # account_page = AccountPage
    # main_page = MainPage
    login_page = LoginPage

    @pytest.fixture(autouse=True)
    def setup(self, request, browser):
        request.cls.browser = browser

        # request.cls.header_page = HeaderPage(browser)
        request.cls.create_account_page = CreateAccountPage(browser)
        # request.cls.account_page = AccountPage(browser)
        # request.cls.main_page = MainPage(browser)
        request.cls.login_page = LoginPage(browser)
