import allure
import pytest
from time import sleep

from config.base_test import BaseTest


class TestProductPage(BaseTest):

    @allure.title('Добавление товара в корзину')
    def test_add_prod_to_cart_and_continue_shopping(self, pre_goto_prod_page):
        title, price, quantity = self.product_page.get_primary_info_about_product_on_product_page()
        self.product_page.add_prod_to_cart_and_continue_shopping()
        self.header_page.check_prods_quantity_in_header(exp=quantity)
        self.header_page.goto_cart_page()
        self.cart_page.is_opened()
        self.cart_page.order_overview_is_displayed()
        self.cart_page.check_prod_title_price_and_quantity(title, price, quantity)

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

    @pytest.mark.test
    @allure.title('Закрытие модалки "Добавить в корзину"')
    def test_close_modal_add_to_cart(self, pre_go_to_customize_desk_page):
        self.product_page.open_modal_add_to_cart()
        self.modal_add_to_cart.close_modal()
        self.modal_add_to_cart.modal_should_not_be_displayed()

    @pytest.mark.test
    @allure.title('Наименование и цена товара в модалке корректные')
    def test_title_and_price_in_modal_should_be_correct(self, pre_go_to_customize_desk_page):
        title, price = self.product_page.get_title_and_price_on_product_page()
        act_quan = self.product_page.get_prod_units_quantity_on_product_page()
        self.product_page.open_modal_add_to_cart()
        self.modal_add_to_cart.check_prod_title_price_and_quantity(title, price, act_quan)

    @pytest.mark.test
    @allure.title('Количество единиц товара и итоговая стоимость в модалке корректные')
    @pytest.mark.parametrize('exp_quan', [1, 2, 3, 4, 5, 6, 7])
    def test_close_modal_add_to_cart(self, exp_quan, pre_go_to_customize_desk_page):
        self.product_page.add_multiple_units_of_prod(quantity=exp_quan)
        title, price = self.product_page.get_title_and_price_on_product_page()
        act_quan = self.product_page.get_prod_units_quantity_on_product_page()
        self.product_page.open_modal_add_to_cart()
        self.modal_add_to_cart.check_product_units_quantity(act_quan)
        self.modal_add_to_cart.check_product_total_price(price)
