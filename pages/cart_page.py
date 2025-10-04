from decimal import Decimal, ROUND_HALF_UP

import allure
import random

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
        self.subtotal_price = BaseElement(
            self.browser, 'Общая стоимость без комиссии', *CartPageLocators.SUBTOTAL_PRICE
        )
        self.taxes = BaseElement(self.browser, 'Комиссия', *CartPageLocators.TAXES)
        self.total_price = BaseElement(
            self.browser, 'Общая стоимость с комиссией', *CartPageLocators.TOTAL_PRICE
        )
        self.delete_product_button = Button(
            self.browser, 'Удалить товар из корзины', *CartPageLocators.DELETE_PRODUCT_BUTTON
        )

    def order_overview_is_displayed(self):
        with allure.step(f'{self.order_overview.name} отображается'):
            self.assert_data_equal_data(
                act_res=self.order_overview.is_visible(),
                exp_res=True,
                message=f'{self.order_overview.name} не отображается'
            )

    def should_be_message_if_cart_is_empty(self):
        with allure.step(f'Отображается сообщение {self.empty_cart_message.name}'):
            act = self.empty_cart_message.get_text_of_element()

            self.assert_data_equal_data(
                act_res=act,
                exp_res=InfoMessage.CART_IS_EMPTY,
                message=f'{self.empty_cart_message.name} не отображается'
            )

    def check_prod_title_price_and_quantity(self, exp_title, exp_price, exp_quantity: int, full_match=False):
        with allure.step('Проверить наличие товаров в корзине'):
            titles = [t.text for t in self.product_title.get_elements()]
            prices = [p.text for p in self.product_price.get_elements()]
            quantities = [int(q.get_attribute('value')) for q in self.units_quantity_input.get_elements()]

            self.product_is_on_order_overview(exp_title, titles, full_match)

            with allure.step('Проверить количество и стоимость товара'):
                for i in range(len(titles)):
                    if exp_title in titles[i]:
                        self.check_product_quantity(quantities[i], exp_quantity)
                        self.check_product_price(prices[i], exp_price)

    def product_is_on_order_overview(self, prod_title, prods_list: list, full_match=False):
        f = False

        if full_match:
            self.assert_data_in_data(
                act_res=prod_title,
                exp_res=prods_list,
                message=f'Товар {prod_title} не найден в корзине'
            )
        else:
            for t in prods_list:
                if prod_title in t:
                    f = True
                    break

            self.assert_data_equal_data(
                act_res=f,
                exp_res=True,
                message=f'Товар {prod_title} не найден в корзине'
            )

    def product_should_not_be_on_order_overview(self, prod_title):
        with allure.step(f'Товар {prod_title} отсутствует в корзине после удаления'):
            f = True
            self.order_overview.is_present()
            titles = [t.text for t in self.product_title.get_elements()]

            for t in titles:
                if prod_title in t:
                    f = False
                    break

            self.assert_data_equal_data(
                act_res=f,
                exp_res=True,
                message=f'Товар {prod_title} отображется в корзине после удаления'
            )

    def remove_product_from_cart(self, prod_title: str):
        with allure.step(f'Удалить товар {prod_title} из корзины'):
            titles = [t.text for t in self.product_title.get_elements()]
            remove_buttons = self.delete_product_button.get_elements()

            for i in range(len(titles)):
                if prod_title in titles[i]:
                    self.delete_product_button.scroll_to_element(remove_buttons[i])
                    remove_buttons[i].click()
                    self.wait.until(self.ec.invisibility_of_element_located(remove_buttons[i]))


    def remove_random_product_from_cart(self):
        with allure.step(f'Удалить рандомный товар из корзины'):
            titles = [t.text for t in self.product_title.get_elements()]
            remove_buttons = self.delete_product_button.get_elements()
            prod_title = random.choice(titles)

            for i in range(len(titles)):
                if prod_title in titles[i]:
                    self.delete_product_button.scroll_to_element(remove_buttons[i])
                    remove_buttons[i].click()
                    self.wait.until(self.ec.invisibility_of_element_located(remove_buttons[i]))

            return prod_title

    def check_product_quantity(self, act_quan, exp_quan):
        with allure.step('Проверить количество единиц товара'):
            self.assert_data_equal_data(
                act_res=act_quan,
                exp_res=exp_quan,
                message='Некорректное количество единиц товара'
            )

    def check_product_price(self, act_price, exp_price):
        with allure.step('Проверить стоимость товара'):
            self.assert_data_equal_data(
                act_res=act_price,
                exp_res=exp_price,
                message='Некорректная стоимость товара'
            )

    def check_subtotal_price(self):
        with allure.step(f'Проверить {self.subtotal_price.name}'):
            act = self.get_subtotal_price()
            exp = self.subtotal_price.get_text_of_element()

            self.assert_data_equal_data(
                act_res=act,
                exp_res=exp,
                message=f'Некорректная {self.subtotal_price.name}'
            )

    def tax_should_be_15_percent(self):
        with allure.step(f'{self.taxes.name} должна составлять 15%'):
            subtotal_price = self.parse_price_to_num(self.get_subtotal_price())
            act_tax = self.parse_num_to_price((subtotal_price / 100) * 15)
            exp_tax = self.taxes.get_text_of_element()

            self.assert_data_equal_data(
                act_res=act_tax,
                exp_res=exp_tax,
                message='Некорректный размер комиссии'
            )

    def check_total_price_with_tax(self):
        with allure.step(f'Проверить {self.total_price.name}'):
            act = self.get_total_price_with_tax()
            exp = self.total_price.get_text_of_element()

            self.assert_data_equal_data(
                act_res=act,
                exp_res=exp,
                message=f'Некорректная {self.total_price.name}'
            )

    def get_subtotal_price(self):
        prices = [p.text for p in self.product_price.get_elements()]
        new_prices = [self.parse_price_to_num(p) for p in prices]

        summ_prices = sum(new_prices)

        return self.parse_num_to_price(summ_prices)

    def get_total_price_with_tax(self):
        tax = self.parse_price_to_num(self.taxes.get_text_of_element())
        subtotal_price = self.parse_price_to_num(self.get_subtotal_price())

        return self.parse_num_to_price(subtotal_price + tax)

    @staticmethod
    def parse_num_to_price(value: (float, str)):
        # Форматирует число в строку вида $ x,xxx,xxx.xx
        d = Decimal(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        s = f"$ {d:,.2f}"

        return s

    @staticmethod
    def parse_price_to_num(value: str):
        # Форматирует строку вида $ x,xxx,xxx.xx в число
        index = value.find(' ') + 1
        num_value = float(value.replace(',', '')[index:])

        return num_value
