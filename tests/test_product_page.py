import allure
import pytest
from time import sleep

from config.base_test import BaseTest


class TestProductPage(BaseTest):

    @pytest.mark.test
    @allure.title('Добавление товара в корзину')
    def test_add_prod_to_cart_and_continue_shopping(self, pre_goto_prod_page):
        title, price, quantity = self.product_page.get_primary_info_about_product_on_product_page()
        self.product_page.add_prod_to_cart_and_continue_shopping()
        self.header_page.check_prods_quantity_in_header(exp=quantity)
        self.header_page.goto_cart_page()
        self.cart_page.is_opened()
        self.cart_page.order_overview_is_displayed()
        self.cart_page.check_prod_title_price_and_quantity(title, price, quantity)

    @pytest.mark.test
    @allure.title('Добавление в корзину нескольких единиц одного товара')
    @pytest.mark.parametrize('exp_quan', [1, 2, 3, 4, 5, 6, 7])
    def test_add_multiple_units_of_the_same_product(self, exp_quan, pre_goto_prod_page):
        self.product_page.add_multiple_units_of_prod(quantity=exp_quan)
        title, price, act_quan = self.product_page.get_primary_info_about_product_on_product_page()
        self.product_page.add_prod_to_cart_and_continue_shopping()
        self.header_page.check_prods_quantity_in_header(exp=act_quan)
        self.header_page.goto_cart_page()
        self.cart_page.is_opened()
        self.cart_page.order_overview_is_displayed()
        self.cart_page.check_prod_title_price_and_quantity(title, price, act_quan)
