import allure

from config.links import Links
from data_for_tests.data_for_tests import InfoMessage
from elements.base_element import BaseElement
from elements.button import Button
from elements.input import Input
from locators.locs_cart_page import CartPageLocators
from pages.header_page import HeaderPage


class CartPage(HeaderPage):
    PAGE_URL = Links.CART_PAGE

    def __init__(self, browser):
        super().__init__(browser)

        self.order_overview = BaseElement(self.browser, 'Блок с заказами', *CartPageLocators.ORDER_OVERVIEW)
        self.empty_cart_message = BaseElement(
            self.browser, 'Сообщение "Ваша корзина пуста"', *CartPageLocators.EMPTY_CART_MESSAGE
        )
        self.product_title = BaseElement(self.browser, 'Наименование товара', *CartPageLocators.PRODUCT_TITLE)
        self.product_price = BaseElement(self.browser, 'Стоимость товара', *CartPageLocators.PRODUCT_PRICE)
        self.units_quantity_input = Input(
            self.browser, 'Счетчик единиц товара', *CartPageLocators.QUANTITY_INPUT
        )

    def order_overview_is_displayed(self):
        with (allure.step(f'{self.order_overview.name} отображается')):
            assert self.order_overview.is_visible(), (f'{self.order_overview.name} не отображается!\n'
                                                      f'Скриншот {self.attach_screenshot(self.order_overview.name)}')

    def should_be_message_if_cart_is_empty(self):
        with allure.step(f'Отображается сообщение {self.empty_cart_message.name}'):
            act = self.empty_cart_message.get_text_of_element()

            assert act == InfoMessage.CART_IS_EMPTY, (f'Некорректное имя пользователя в профиле\n'
                                                      f'ОР: {InfoMessage.CART_IS_EMPTY}\n'
                                                      f'ФР: {act}\n'
                                                      f'Скриншот {self.attach_screenshot(self.empty_cart_message.name)}')

    def check_prod_title_price_and_quantity(self, exp_title, exp_price, exp_quantity: int):
        with allure.step('Проверить наличие товаров в корзине'):
            titles = [t.text for t in self.product_title.get_elements()]
            prices = [p.text for p in self.product_price.get_elements()]
            quantities = [int(q.get_attribute('value')) for q in self.units_quantity_input.get_elements()]

            self.product_is_on_order_overview(exp_title, titles)

            with allure.step('Проверить количество и стоимость товара'):
                for i in range(len(titles)):
                    if exp_title in titles[i]:
                        self.check_product_quantity(quantities[i], exp_quantity)
                        self.check_product_price(prices[i], exp_price)

    def product_is_on_order_overview(self, prod_title, prods_list: list):

        with allure.step('Искомый товар найден в корзине'):
            f = False

            for t in prods_list:
                if prod_title in t:
                    f = True
                    break

            assert f is True, (f'Товар {prod_title} не найден в корзине!\n'
                               f'Скриншот {self.attach_screenshot(prod_title)}')

    def check_product_quantity(self, act_quan, exp_quan):
        with allure.step('Проверить количество единиц товара'):
            assert exp_quan == act_quan, f'Некорректное количество единиц товара!\n' \
                                         f'ОР: {exp_quan}\n' \
                                         f'ФР: {act_quan}\n' \
                                         f'Скриншот {self.attach_screenshot(exp_quan)}'

    def check_product_price(self, act_price, exp_price):
        with allure.step('Проверить стоимость товара'):
            assert exp_price == act_price, f'Некорректная стоимость товара!\n' \
                                           f'ОР: {exp_price}\n' \
                                           f'ФР: {act_price}\n' \
                                           f'Скриншот {self.attach_screenshot(exp_price)}'
