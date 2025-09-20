import allure

from elements.base_element import BaseElement
from elements.button import Button
from elements.input import Input
from locators.locs_product_page import ProductPageLocators
from pages.base_page import BasePage


class ProductPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

        self.product_title = BaseElement(self.browser, 'Наименование товара', *ProductPageLocators.PRODUCT_TITLE)
        self.product_price = BaseElement(self.browser, 'Стоимость товара', *ProductPageLocators.PRODUCT_PRICE)

    def check_title_and_price(self, exp_title, exp_price):
        with allure.step('Проверить наименование и стоимость товара'):
            act_title = self.product_title.get_text_of_element()
            act_price = self.product_price.get_text_of_element()

            assert act_title == exp_title, (f'Некорректное наименование товара\n'
                                            f'ОР: {exp_title}\n'
                                            f'ФР: {act_title}',
                                            self.attach_screenshot(self.product_title.name))

            assert act_title == exp_title, (f'Некорректная стоимость товара\n'
                                            f'ОР: {exp_price}\n'
                                            f'ФР: {act_price}',
                                            self.attach_screenshot(self.product_price.name))
