import allure
from pages.header_page import HeaderPage
from config.links import Links
from elements.button import BaseElement, Button
from locators.locs_cart_page import CartPageLocators


class CartPage(HeaderPage):
    PAGE_URL = Links.CART_PAGE

    def __init__(self, browser):
        super().__init__(browser)

        self.order_overview = BaseElement(self.browser, 'Блок с заказами', *CartPageLocators.ORDER_OVERVIEW)

    def order_overview_is_displayed(self):
        with allure.step(f'{self.order_overview.name} отображается'):
            assert self.order_overview.is_visible(), f'{self.order_overview.name} не отображается!'

