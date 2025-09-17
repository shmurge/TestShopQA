import allure
from pages.header_page import HeaderPage
from config.links import Links
from elements.base_element import BaseElement
from elements.button import Button
from locators.locs_cart_page import CartPageLocators
from data_for_tests.data_for_tests import InfoMessage


class CartPage(HeaderPage):
    PAGE_URL = Links.CART_PAGE

    def __init__(self, browser):
        super().__init__(browser)

        self.order_overview = BaseElement(self.browser, 'Блок с заказами', *CartPageLocators.ORDER_OVERVIEW)
        self.empty_cart_message = BaseElement(
            self.browser, 'Сообщение "Ваша корзина пуста"', *CartPageLocators.EMTPTY_CART_MESSAGE
        )

    def order_overview_is_displayed(self):
        with (allure.step(f'{self.order_overview.name} отображается')):
            assert self.order_overview.is_visible(), (f'{self.order_overview.name} не отображается!'
                                                      f'{self.attach_screenshot(self.order_overview.name)}')

    def should_be_message_if_cart_is_empty(self):
        with allure.step(f'Отображается сообщение {self.empty_cart_message.name}'):
            act = self.empty_cart_message.get_text_of_element().strip()

            assert act == InfoMessage.CART_IS_EMPTY, (f'Некорректное имя пользователя в профиле\n'
                                                      f'ОР: {InfoMessage.CART_IS_EMPTY}\n'
                                                      f'ФР: {act}\n'
                                                      f'{self.attach_screenshot(self.empty_cart_message.name)}')
