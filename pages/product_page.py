import allure
from pages.base_page import BasePage
from elements.base_element import BaseElement
from elements.button import Button
from elements.input import Input
from locators.locs_product_page import ProductPageLocators


class ProductPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

        self.product_title = BaseElement(self.browser, 'Наименование товара', *ProductPageLocators.PRODUCT_TITLE)
        self.product_price = BaseElement(self.browser, 'Стоимость товара', *ProductPageLocators.PRODUCT_PRICE)

    def check_title_and_price(self, exp_title, exp_price):
        with allure.step('Проверить наименование и стоимость товара'):
            act_title = self.product_title.get_text_of_element().strip()
            act_price = self.product_price.get_text_of_element().strip()

            self.base_assertions.assert_data_equal_data(act_title, exp_title)
            self.base_assertions.assert_data_equal_data(act_price, exp_price)
