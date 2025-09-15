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
        self.cart_button = Button(self.browser, 'Корзина', *HeaderPageLocators.LINK_CART)
        self.main_search_button = Button(self.browser, 'Главный поиск', *HeaderPageLocators.BUTTON_MAIN_SEARCH)
        self.sign_in_button = Button(self.browser, 'Войти', *HeaderPageLocators.LINK_SIGN_IN)
        self.username = BaseElement(self.browser, 'Имя пользователя', *HeaderPageLocators.USERNAME)
        self.my_account_button = Button(self.browser, 'Мой аккаунт', *HeaderPageLocators.MY_ACCOUNT_BUTTON)
        self.logout_button = Button(self.browser, 'Выйти', *HeaderPageLocators.LOGOUT_BUTTON)

    def goto_main_page(self):
        with allure.step('Перейти на главную страницу'):
            self.main_logo.click()

    def goto_login_page(self):
        with allure.step('Перейти на страницу логина'):
            self.sign_in_button.click()

    def goto_cart_page(self):
        with allure.step('Перейти на страницу корзины'):
            self.cart_button.click()

    def open_main_search(self):
        with allure.step('Открыть главный поиск'):
            self.main_search_button.click()

    def username_is_correct(self, exp):
        act = self.username.get_text_of_element().strip()
        with allure.step(f'{self.username.name} в хэдере соответствует'):
            self.base_assertions.assert_data_equal_data(act, exp)

    def goto_my_account(self):
        with allure.step('Перейти в аккаунт'):
            self.username.move_to_element()
            self.my_account_button.click()

    def logout(self):
        with allure.step('Выход из аккаунта'):
            self.username.move_to_element()
            self.logout_button.click()

    def sign_in_button_is_displayed(self):
        with allure.step(f'{self.sign_in_button.name} отображается'):
            self.sign_in_button.is_visible()
