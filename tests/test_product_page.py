import allure
import pytest
from time import sleep

from config.base_test import BaseTest


class TestProductPage(BaseTest):

    @allure.title('Добавление товара в корзину')
    def test_add_prod_to_cart_and_continue_shopping(self, pre_goto_prod_page):
        title, price = self.product_page.add_prod_to_cart_and_continue_shopping()
        self.header_page.check_prods_quantity_in_header(exp=1)
        self.header_page.goto_cart_page()
        self.cart_page.is_opened()
        self.cart_page.order_overview_is_displayed()
        self.cart_page.check_prod_title_and_price(title, price)

    @pytest.mark.test
    @allure.title('Добавление в корзину нескольких единиц одного товара')
    def test_add_multiple_units_of_the_same_product(self, pre_goto_prod_page):
        self.product_page.add_multiple_units_of_prod()
        title, price = self.product_page.add_prod_to_cart_and_continue_shopping()
        self.header_page.check_prods_quantity_in_header(2)



