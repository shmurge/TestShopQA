import allure
import pytest

from config.base_test import BaseTest
from data_for_tests.data_for_tests import ProductInfo


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

    @allure.title('Закрытие модалки "Добавить в корзину"')
    def test_close_modal_add_to_cart(self, pre_go_to_customize_desk_page):
        self.product_page.open_modal_add_to_cart()
        self.modal_add_to_cart.close_modal()
        self.modal_add_to_cart.modal_should_not_be_displayed()

    @allure.title('Проверка полной информации о товаре на странице')
    def test_check_complete_prod_info_on_page(self, pre_go_to_customize_desk_page):
        self.product_page.check_title_and_price_in_prod_page(
            exp_title=ProductInfo.CUSTOMIZE_DESK_SHORT_TITLE,
            exp_price=ProductInfo.CUSTOMIZE_DESC_DEFAULT_PRICE
        )
        self.product_page.check_product_description_on_page(exp=ProductInfo.DESCRIPTION_CUSTOMIZE_DESK)

    @allure.title('Цена стола из алюминия отличается от дефолтной')
    def test_price_of_aluminium_table_differs_from_the_default(self, pre_go_to_customize_desk_page):
        self.product_page.choose_material_on_page(material='aluminium')

        self.product_page.check_title_and_price_in_prod_page(
            exp_title=ProductInfo.CUSTOMIZE_DESK_SHORT_TITLE,
            exp_price=ProductInfo.CUSTOMIZE_DESC_ALUMINIUM_PRICE
        )

    @allure.title('Наименование и цена товара в модалке корректные')
    def test_title_and_price_in_modal_should_be_correct(self, pre_go_to_customize_desk_page):
        title, price, act_quan = self.product_page.get_primary_info_about_product_on_product_page()
        self.product_page.open_modal_add_to_cart()
        self.modal_add_to_cart.check_prod_title_price_and_quantity(title, price, act_quan)

    @allure.title('Количество единиц товара и итоговая стоимость в модалке корректные')
    @pytest.mark.parametrize('exp_quan', [1, 2, 5, 8, 11, 15, 20])
    def test_should_be_correct_unit_quan_and_total_price_in_modal(self, exp_quan, pre_go_to_customize_desk_page):
        self.product_page.add_multiple_units_of_prod(quantity=exp_quan)
        price = self.product_page.get_prod_price_on_page()
        act_quan = self.product_page.get_prod_units_quantity_on_product_page()
        self.product_page.open_modal_add_to_cart()
        self.modal_add_to_cart.check_product_units_quantity(act_quan)
        self.modal_add_to_cart.check_product_total_price(price)

    @allure.title('Наименование товара в модалке меняется в соответствии с опциями')
    @pytest.mark.xfail
    @pytest.mark.parametrize(
        'material, color, result_title',
        [
            ('steel', 'white', ProductInfo.T_CUSTOMIZE_DESK_STEEL_WHITE),
            ('steel', 'black', ProductInfo.T_CUSTOMIZE_DESK_STEEL_BLACK),
            ('aluminium', 'white', ProductInfo.T_CUSTOMIZE_DESK_ALUM_WHITE),
            ('custom', 'white', ProductInfo.T_CUSTOMIZE_DESK_CUSTOM_WHITE),
            ('custom', 'black', ProductInfo.T_CUSTOMIZE_DESK_CUSTOM_BLACK),
        ]
    )
    def test_product_title_in_modal_changes_due_to_options(
            self, pre_go_to_customize_desk_page, material, color, result_title
    ):
        self.product_page.choose_material_on_page(material)
        self.product_page.choose_color_on_page(color)
        self.product_page.open_modal_add_to_cart()
        self.modal_add_to_cart.check_product_title(result_title, full_match=True)

    @allure.title('Наименование товара в козине меняется в соответствии с опциями')
    @pytest.mark.parametrize(
        'material, color, result_title',
        [
            ('steel', 'white', ProductInfo.T_CUSTOMIZE_DESK_STEEL_WHITE),
            ('steel', 'black', ProductInfo.T_CUSTOMIZE_DESK_STEEL_BLACK),
            ('aluminium', 'white', ProductInfo.T_CUSTOMIZE_DESK_ALUM_WHITE),
            ('custom', 'white', ProductInfo.T_CUSTOMIZE_DESK_CUSTOM_WHITE),
            ('custom', 'black', ProductInfo.T_CUSTOMIZE_DESK_CUSTOM_BLACK),
        ]
    )
    def test_product_title_in_cart_changes_due_to_options(
            self, pre_go_to_customize_desk_page, material, color, result_title
    ):
        self.product_page.choose_material_on_page(material)
        self.product_page.choose_color_on_page(color)
        title = result_title
        price = self.product_page.get_prod_price_on_page(cost_calculation=False)
        act_quan = self.product_page.get_prod_units_quantity_on_product_page()
        self.product_page.add_prod_to_cart_and_continue_shopping()
        self.cart_page.check_prods_quantity_in_header(act_quan)
        self.header_page.goto_cart_page()
        self.cart_page.is_opened()
        self.cart_page.check_prod_title_price_and_quantity(
            exp_title=title,
            exp_price=price,
            exp_quantity=act_quan,
            full_match=True  # Полное совпадение наименования товара
        )
