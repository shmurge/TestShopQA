import allure

from elements.base_element import BaseElement
from elements.button import Button
from elements.input import Input
from locators.locs_header_page import HeaderPageLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

        self.main_logo = BaseElement(self.browser, 'Лого', *HeaderPageLocators.MAIN_LOGO)
        self.cart_button = Button(self.browser, 'Корзина', *HeaderPageLocators.LINK_CART)
        self.counter_on_cart = BaseElement(
            self.browser, 'Кол-во товаров в корзине', *HeaderPageLocators.COUNTER_ON_CART
        )
        self.main_search_button = Button(self.browser, 'Главный поиск', *HeaderPageLocators.BUTTON_MAIN_SEARCH)
        self.sign_in_button = Button(self.browser, 'Войти', *HeaderPageLocators.LINK_SIGN_IN)
        self.username_in_header = BaseElement(self.browser, 'Имя пользователя', *HeaderPageLocators.USERNAME)
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
        act = self.username_in_header.get_text_of_element()
        with allure.step(f'{self.username_in_header.name} в хэдере корректное'):
            self.assert_data_equal_data(
                act_res=act,
                exp_res=exp,
                message=f'{self.username_in_header.name} некорректно'
            )

    def goto_my_account(self):
        with allure.step('Перейти в аккаунт'):
            self.username_in_header.move_to_element()
            self.my_account_button.click()

    def logout(self):
        with allure.step('Выход из аккаунта'):
            self.username_in_header.move_to_element()
            self.logout_button.click()

    def sign_in_button_is_displayed(self):
        with allure.step(f'{self.sign_in_button.name} отображается'):
            self.assert_data_equal_data(
                act_res=self.sign_in_button.is_visible(),
                exp_res=True,
                message=f'{self.sign_in_button.name} не отображается'
            )

    def check_prods_quantity_in_header(self, exp: int):
        with allure.step('Проверить количество товаров в счетчике хэдера'):
            act = int(self.counter_on_cart.get_text_of_element())

            self.assert_data_equal_data(
                act_res=act,
                exp_res=exp,
                message='Некорректное количество товаров в счетчике хэдера'
            )
