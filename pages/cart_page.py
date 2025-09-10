import allure
from pages.header_page import HeaderPage
from config.links import Links
from elements.button import BaseElement, Button
from locators.locs_cart_page import CartPageLocators


class CartPage(HeaderPage):
    PAGE_URL = Links.CART_PAGE

    def __init__(self, browser):
        super().__init__(browser)

        self.order_overview = BaseElement(self.browser, 'Обзор заказа', *CartPageLocators.ORDER_OVERVIEW)

    def cart_page_is_displayed(self):
        with allure.step('Отображается страница корзины'):
            assert self.order_overview.is_visible(), 'Страница корзины не отображается!'

