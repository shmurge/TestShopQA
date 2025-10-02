import random

import allure

from config.links import Links
from data_for_tests.data_for_tests import InfoMessage
from elements.base_element import BaseElement
from elements.button import Button
from elements.input import Input
from locators.locs_main_page import MainPageLocators
from pages.header_page import HeaderPage


class MainPage(HeaderPage):
    PAGE_URL = Links.MAIN_PAGE

    def __init__(self, browser):
        super().__init__(browser)

        self.search_input = Input(self.browser, 'Поиск', *MainPageLocators.SEARCH_INPUT)
        self.searching_result_cnt = BaseElement(
            self.browser, 'Счетчик найденных товаров', *MainPageLocators.SEARCHING_RESULT_CNT
        )
        self.message_no_searching_results = BaseElement(
            self.browser, 'Сообщение на странице "Ничего не найдено"',
            *MainPageLocators.MESSAGE_ON_PAGE_NO_SEARCHING_RESULTS
        )
        self.product_title = Button(self.browser, 'Наименование товара', *MainPageLocators.PRODUCT_TITLE)
        self.product_price = Button(self.browser, 'Цена товара', *MainPageLocators.PRODUCT_PRICE)

    def main_page_is_displayed(self):
        with allure.step('Отображается главная страница'):
            self.assert_data_equal_data(
                act_res=self.search_input.is_visible(),
                exp_res=True,
                message=f'{self.search_input.name} не отображается'
            )

    def check_placeholder_in_search_input(self, exp):
        with allure.step(f'Проверить плэйсхолдер в {self.search_input.name}'):
            act = self.search_input.get_placeholder()

            self.assert_data_equal_data(
                act_res=act,
                exp_res=exp,
                message=f'Некорректный плэйсхолдер в {self.search_input.name}'
            )

    def select_random_product(self):
        titles = self.product_title.get_elements()
        prices = self.product_price.get_elements()
        if len(titles) > 1:
            rand_index = random.randrange(0, len(titles))
            t = titles[rand_index].text.strip()
            p = prices[rand_index].text.strip()
            el = titles[rand_index]
        else:
            t = titles[0].text.strip()
            p = prices[0].text.strip()
            el = titles[0]

        with allure.step(f'Выбрать товар: {t}'):
            self.product_title.scroll_to_element(el)
            self.product_title.click(el)

        return t, p

    def search_product(self, data):
        with allure.step(f'Поиск товара: {data}'):
            self.search_input.click()
            self.search_input.fill_autocomplete_input(data)

    def check_searching_result(self, data):
        with allure.step('Проверить результаты поиска товаров'):
            self.found_prods_contain_keyword_in_title(data)
            self.check_result_count()

    def found_prods_contain_keyword_in_title(self, keyword):
        with allure.step(f'Найденные товары содержат {keyword} в наименовании'):
            self.searching_result_cnt.is_visible()
            titles = [t.text.strip() for t in self.product_title.get_elements()]

            for title in titles:
                self.assert_data_in_data(
                    act_res=keyword.lower(),
                    exp_res=title.lower(),
                    message=f'Найденный товар {title} не содержит {keyword} в наименовании'
                )

    def check_result_count(self):
        with allure.step('Корректное количество найденных товаров в счетчике'):
            titles = self.product_title.get_elements()
            cnt_res = self.searching_result_cnt.get_text_of_element()
            parenthesis_index = cnt_res.find('(') + 1
            space_index = cnt_res.find(' ')
            res_count = int(cnt_res[parenthesis_index:space_index])

            self.assert_data_equal_data(
                act_res=len(titles),
                exp_res=res_count,
                message='Некорректый результат в счетчике найденных товаров'
            )

    def check_message_with_no_results(self):
        with allure.step('Отображается попап с отсутствием результатов поиска'):
            query = 'iqwjhhuchoihdqhd'
            self.search_input.fill_autocomplete_input(query)
            act = self.message_no_searching_results.get_text_of_element()
            exp = InfoMessage().message_no_results(query)

            self.assert_data_equal_data(
                act_res=act,
                exp_res=exp,
                message='Некорректно сообщение'
            )
