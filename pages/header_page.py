import allure
from pages.base_page import BasePage
from elements.base_element import BaseElement
from elements.button import Button
from elements.input import Input
from locators.locs_header_page import HeaderPageLocators


class HeaderPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

        self.main_logo = BaseElement(self.browser, 'Лого', *HeaderPageLocators.MAIN_LOGO)
        self.cart_button = Button(self.browser, 'Корзина', *HeaderPageLocators.BUTTON_CART)
        self.main_search_button = Button(self.browser, 'Главный поиск', *HeaderPageLocators.BUTTON_MAIN_SEARCH)
        self.sign_in_button = Button(self.browser, 'Войти', *HeaderPageLocators.BUTTON_SIGN_IN)

    def go_to_main_page(self):
        with allure.step('Перейти на главную страницу'):
            self.main_logo.click()

    def go_to_login_page(self):
        with allure.step('Перейти на страницу логина'):
            self.sign_in_button.click()

    def go_to_cart_page(self):
        with allure.step('Перейти на страницу корзины'):
            self.cart_button.click()

    def open_main_search(self):
        with allure.step('Открыть главный поиск'):
            self.main_search_button.click()
