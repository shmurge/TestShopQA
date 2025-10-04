import allure
import pytest

from config.base_test import BaseTest


@allure.suite('Корзина')
class TestCartPage(BaseTest):

    @allure.title('Если корзина пуста, пользователь увидит сообщение')
    def test_user_see_message_if_cart_is_empty(self):
        self.cart_page.open()
        self.cart_page.is_opened()

        self.cart_page.should_be_message_if_cart_is_empty()

    @allure.title('Итоговая стоимость одной единицы товара без комиссии должна быть корректной')
    def test_subtotal_price_for_one_product_should_be_correct(self, pre_add_random_product_to_cart):
        self.cart_page.open()
        self.cart_page.is_opened()

        self.cart_page.check_subtotal_price()

    @allure.title('Комиссия (налог) на один товар должна составлять 15 процентов от общей стоимости')
    def test_taxes_for_one_product_should_be_correct(self, pre_add_random_product_to_cart):
        self.cart_page.open()
        self.cart_page.is_opened()

        self.cart_page.tax_should_be_15_percent()

    @allure.title('Итоговая стоимость одного товара с учетом комиссии должна быть корректной')
    def test_total_price_with_tax_for_one_product_should_be_correct(self, pre_add_random_product_to_cart):
        self.cart_page.open()
        self.cart_page.is_opened()

        self.cart_page.check_total_price_with_tax()

    @allure.title('Итоговая стоимость нескольких товаров без комиссии должна быть корректной')
    def test_subtotal_price_for_several_products_should_be_correct(self, pre_add_several_random_products_to_cart):
        self.cart_page.open()
        self.cart_page.is_opened()

        self.cart_page.check_subtotal_price()

    @allure.title('Комиссия (налог) на несколько товаров должна составлять 15 процентов от общей стоимости')
    def test_taxes_for_several_products_should_be_correct(self, pre_add_several_random_products_to_cart):
        self.cart_page.open()
        self.cart_page.is_opened()

        self.cart_page.tax_should_be_15_percent()

    @allure.title('Итоговая стоимость нескольких товаров с учетом комиссии должна быть корректной')
    def test_total_price_with_tax_for_several_products_should_be_correct(self, pre_add_several_random_products_to_cart):
        self.cart_page.open()
        self.cart_page.is_opened()

        self.cart_page.check_total_price_with_tax()

    @allure.title('Отображается сообщение "Корзина пуста" после удаления единственного товара из козины')
    def test_remove_only_one_product_from_cart(self, pre_add_random_product_to_cart):
        product_title = self.product_page.get_prod_title_on_page()

        self.cart_page.open()
        self.cart_page.is_opened()
        self.cart_page.remove_product_from_cart(product_title)

        self.cart_page.should_be_message_if_cart_is_empty()

    @pytest.mark.test
    @allure.title('Удаленный товар не должен отображаться в списке товаров')
    def test_remove_only_one_product_from_cart(self, pre_add_several_random_products_to_cart):
        self.cart_page.open()
        self.cart_page.is_opened()
        prod_title = self.cart_page.remove_random_product_from_cart()

        self.cart_page.product_should_not_be_on_order_overview(prod_title)
