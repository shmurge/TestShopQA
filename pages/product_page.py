from decimal import Decimal, ROUND_HALF_UP

import allure
from time import sleep
import random

from elements.base_element import BaseElement
from elements.button import Button
from elements.input import Input
from locators.locs_product_page import ProductPageLocators, AddToCartModal
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

        self.product_title_on_page = BaseElement(
            self.browser, 'Наименование товара на странице', *ProductPageLocators.PRODUCT_TITLE
        )
        self.product_price_on_page = BaseElement(
            self.browser, 'Стоимость товара на странице', *ProductPageLocators.PRODUCT_PRICE
        )
        self.add_to_cart_button = Button(
            self.browser, 'Добавить в корзину', *ProductPageLocators.ADD_TO_CART_BUTTON
        )
        self.radio_button_material = Button(
            self.browser, 'Выбрать материал', *ProductPageLocators.RADIO_BUTTON_MATERIAL
        )
        self.radio_button_color = Button(self.browser, 'Выбрать цвет', *ProductPageLocators.RADIO_BUTTON_COLOR)
        self.product_description = BaseElement(
            self.browser, 'Краткое описание товара', *ProductPageLocators.PRODUCT_DESCRIPTION
        )
        self.add_one_unit_button = Button(
            self.browser, 'Добавить одну единицу товара', *ProductPageLocators.ADD_ONE_BUTTON
        )
        self.remove_one_unit_button = Button(
            self.browser, 'Удалить одну единицу товара', *ProductPageLocators.REMOVE_ONE_BUTTON
        )
        self.units_quantity_input = Input(
            self.browser, 'Счетчик единиц товара', *ProductPageLocators.QUANTITY_INPUT
        )
        self.add_to_cart_modal = BaseElement(
            self.browser, 'Модалка "Добавить в корзину"', *AddToCartModal.ADD_TO_CART_MODAL
        )
        self.proceed_to_checkout_button = Button(
            self.browser, 'Перейти к оформлению', *AddToCartModal.PROCEED_TO_CHECKOUT_BUTTON
        )
        self.continue_shopping_button = Button(
            self.browser, 'Продолжить покупки', *AddToCartModal.CONTINUE_SHOPPING_BUTTON
        )

    def add_prod_to_cart_and_continue_shopping(self):
        with allure.step('Добавить товар в корзину'):
            self.add_to_cart_button.click()
            if self.add_to_cart_modal.is_visible(timeout=2, frequency=0.5):
                self.continue_shopping_button.click()

    def add_to_cart_modal_is_displayed(self):
        with allure.step(f'Отображается {self.add_to_cart_modal.name}'):
            self.add_to_cart_modal.is_visible(), (f'Не отображается {self.add_to_cart_modal.name}\n'
                                                  f'Скриншот {self.attach_screenshot(self.add_to_cart_modal.name)}')

    def add_multiple_units_of_prod(self, quantity=1):
        with allure.step('Добавить несколько единиц одного товара'):
            count = 1

            for _ in range(quantity):
                self.add_one_unit_button.click()
                count += 1
                self.wait.until(EC.text_to_be_present_in_element_attribute(
                    self.units_quantity_input.locator, 'value', str(count))
                )


    def check_title_and_price_in_prod_page(self, exp_title, exp_price):
        with allure.step('Проверить наименование и стоимость товара на странице товара'):
            act_title, act_price = self.get_title_and_price_on_product_page()

            assert act_title == exp_title, (f'Некорректное наименование товара\n'
                                            f'ОР: {exp_title}\n'
                                            f'ФР: {act_title}\n'
                                            f'Скриншот {self.attach_screenshot(self.product_title_on_page.name)}')

            assert act_title == exp_title, (f'Некорректная стоимость товара\n'
                                            f'ОР: {exp_price}\n'
                                            f'ФР: {act_price}\n'
                                            f'Скриншот {self.attach_screenshot(self.product_price_on_page.name)}')

    # def check_title_and_price_in_modal(self, exp_title, exp_price):
    #     with allure.step('Проверить наименование товара и стоимость в модалке'):
    #         act_title, act_price = self.get_title_and_price_in_modal()
    #
    #         assert act_title == exp_title, (f'Некорректное наименование товара\n'
    #                                         f'ОР: {exp_title}\n'
    #                                         f'ФР: {act_title}\n'
    #                                         f'Скриншот {self.attach_screenshot(self.product_title_in_modal.name)}')
    #
    #         assert act_title == exp_title, (f'Некорректная стоимость товара\n'
    #                                         f'ОР: {exp_price}\n'
    #                                         f'ФР: {act_price}\n'
    #                                         f'Скриншот {self.attach_screenshot(self.product_price_in_modal.name)}')

    def click_on_continue_shopping(self):
        with allure.step('Продолжить покупки'):
            self.continue_shopping_button.click()

    def cost_calculation(self, price):
        quantity = self.get_prod_units_quantity_on_product_page()
        price = price.replace(',', '')

        start_index = price.find(' ') + 1
        new_price = float(price[start_index:]) * quantity
        price = self.format_number(new_price)

        return price

    def get_primary_info_about_product_on_product_page(self):
        with allure.step('Получить основную информацию о товаре'):
            title, price = self.get_title_and_price_on_product_page()
            quantity = self.get_prod_units_quantity_on_product_page()

        return title, price, quantity

    def get_title_and_price_on_product_page(self):
        title = self.product_title_on_page.get_text_of_element()
        price = self.product_price_on_page.get_text_of_element()
        price = self.cost_calculation(price=price)

        return title, price

    def get_prod_units_quantity_on_product_page(self):
        return int(self.units_quantity_input.get_attribute('value'))

    def get_prod_description(self):
        return self.product_description.get_text_of_element()

    # def get_title_and_price_in_modal(self):
    #     title = self.product_title_in_modal.get_text_of_element()
    #     price = self.product_price_in_modal.get_text_of_element()
    #
    #     return title, price

    def get_additional_info_about_product_on_product_page(self):
        material = self.select_product_material()
        color = self.select_product_color()

        return material, color

    @staticmethod
    def format_number(value):
        # Форматирует число в строку вида $ x,xxx,xxx.xx
        d = Decimal(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        s = f"$ {d:,.2f}"

        return s

    def select_product_material(self):
        if self.radio_button_material.is_visible(timeout=2, frequency=0.5):
            buttons = self.radio_button_material.get_elements()
            b = random.choice(buttons)
            self.radio_button_material.click(b)
            value = self.radio_button_material.get_attribute(attribute='data-value_name', element=b)

            return value

        return None

    def select_product_color(self):
        if self.radio_button_material.is_visible(timeout=2, frequency=0.5):
            buttons = self.radio_button_color.get_elements()
            b = random.choice(buttons)
            self.radio_button_material.click(b)
            value = self.radio_button_material.get_attribute(attribute='data-value_name', element=b)

            return value

        return None
