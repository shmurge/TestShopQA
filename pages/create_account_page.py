import allure
import pytest
from selenium.webdriver.support import expected_conditions as EC
from elements.base_element import BaseElement
from elements.button import Button
from elements.input import Input
from pages.base_page import BasePage
from config.links import Links
# from locators.locs_create_account_page import CreateAccountPageLocators
# from locators.locs_account_page import AccountPageLocators
from conftest import set_env_key

from time import sleep


class CreateAccountPage(BasePage):
    PAGE_URL = Links.CREATE_ACCOUNT_PAGE

    def __init__(self, browser):
        super().__init__(browser)

