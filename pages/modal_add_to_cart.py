import allure
import pytest
from time import sleep

from config.links import Links
from elements.input import Input
from elements.base_element import BaseElement
from elements.button import Button
from locators.locs_modal_add_to_cart import ModalAddToCartLocators
from pages.base_page import BasePage


class ModalAddToCart(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

        self.add_to_cart_modal = BaseElement(
            self.browser, 'Модалка "Добавить в корзину"', *ModalAddToCartLocators.ADD_TO_CART_MODAL
        )
        self.proceed_to_checkout_button = Button(
            self.browser, 'Перейти к оформлению', *ModalAddToCartLocators.PROCEED_TO_CHECKOUT_BUTTON
        )
        self.continue_shopping_button = Button(
            self.browser, 'Продолжить покупки', *ModalAddToCartLocators.CONTINUE_SHOPPING_BUTTON
        )
        self.close_modal_button = Button(
            self.browser, 'Закрыть модалку', *ModalAddToCartLocators.CLOSE_ADD_TO_CART_MODAL_BUTTON
        )
        self.product_title_on_modal = BaseElement(
            self.browser, 'Наименование товара в модалке', *ModalAddToCartLocators.PRODUCT_TITLE
        )
        self.product_price_on_modal = BaseElement(
            self.browser, 'Стоимость товара в модалке', *ModalAddToCartLocators.PRODUCT_PRICE
        )
        self.product_total_price_on_modal = BaseElement(
            self.browser, 'Итоговая стоимость в модалке', *ModalAddToCartLocators.TOTAL_PRICE
        )
        self.add_one_unit_button = Button(
            self.browser, 'Добавить одну единицу товара в модалке', *ModalAddToCartLocators.ADD_ONE_BUTTON
        )
        self.remove_one_unit_button = Button(
            self.browser, 'Удалить одну единицу товара в модалке', *ModalAddToCartLocators.REMOVE_ONE_BUTTON
        )
        self.units_quantity_input = Input(
            self.browser, 'Счетчик единиц товара в модалке', *ModalAddToCartLocators.QUANTITY_INPUT
        )

    def close_modal(self):
        with allure.step(f'Закрыть {self.add_to_cart_modal.name}'):
            self.close_modal_button.click()

    def modal_should_not_be_displayed(self):
        with allure.step(f'{self.add_to_cart_modal.name} не отображается!'):
            assert self.add_to_cart_modal.is_not_visible(timeout=2, frequency=0.5)

    def check_prod_title_price_and_quantity(self, exp_title, exp_price, exp_quan):
        with allure.step('Проверить наименование, стоимость и количество товаров в модалке'):
            self.check_product_title(exp_title)
            self.check_product_price(exp_price)
            self.check_product_units_quantity(exp_quan)

    def check_product_title(self, exp, full_match=False):
        with allure.step(f'Проверить {self.product_title_on_modal.name}'):
            act = self.product_title_on_modal.get_text_of_element()
            if full_match:
                assert exp == act, (f'Некорректное {self.product_title_on_modal.name}!\n'
                                    f'ОР: {exp}\n'
                                    f'ФР: {act}\n'
                                    f'Скриншот {self.attach_screenshot(self.product_title_on_modal.name)}')
            else:
                assert exp in act, (f'Некорректное {self.product_title_on_modal.name}!\n'
                                    f'ОР: {exp}\n'
                                    f'ФР: {act}\n'
                                    f'Скриншот {self.attach_screenshot(self.product_title_on_modal.name)}')

    def check_product_price(self, exp):
        with allure.step(f'Проверить {self.product_price_on_modal.name}'):
            act = self.product_price_on_modal.get_text_of_element()
            assert exp == act, (f'Некорректная {self.product_price_on_modal.name}!\n'
                                f'ОР: {exp}\n'
                                f'ФР: {act}\n'
                                f'Скриншот {self.attach_screenshot(self.product_price_on_modal.name)}')

    def check_product_units_quantity(self, exp: int):
        with allure.step('Проверить количество единиц товара'):
            act = self.get_prod_units_quantity_on_modal()
            assert exp == act, (f'Некорректное количество единиц товара!\n'
                                f'ОР: {exp}\n'
                                f'ФР: {act}\n'
                                f'Скриншот {self.attach_screenshot("К-во единиц товара")}')

    def check_product_total_price(self, exp):
        with allure.step(f'Проверить {self.product_total_price_on_modal.name}'):
            act = self.product_total_price_on_modal.get_text_of_element()
            assert exp == act, (f'Некорректная {self.product_total_price_on_modal.name}!\n'
                                f'ОР: {exp}\n'
                                f'ФР: {act}\n'
                                f'Скриншот {self.attach_screenshot(self.product_price_on_modal.name)}')

    def get_prod_units_quantity_on_modal(self):
        return int(self.units_quantity_input.get_attribute('value'))
