import allure
import random
from pages.header_page import HeaderPage
from config.links import Links
from elements.base_element import BaseElement
from elements.button import Button
from elements.input import Input
from locators.locs_main_page import MainPageLocators


class MainPage(HeaderPage):
    PAGE_URL = Links.MAIN_PAGE

    def __init__(self, browser):
        super().__init__(browser)

        self.search_input = Input(self.browser, 'Поиск', *MainPageLocators.SEARCH_INPUT)
        self.product_title = Button(self.browser, 'Наименование товара', *MainPageLocators.PRODUCT_TITLE)
        self.product_price = Button(self.browser, 'Цена товара', *MainPageLocators.PRODUCT_PRICE)

    def main_page_is_displayed(self):
        with allure.step('Отображается главная страница'):
            assert self.search_input.is_visible(), (f'{self.search_input.name} не отображается!'
                                                    f'{self.attach_screenshot(self.search_input.name)}')

    def select_random_product(self):
        titles = self.product_title.get_elements()
        prices = self.product_price.get_elements()
        rand_index = random.randrange(0, len(titles))
        t = titles[rand_index].text
        p = prices[rand_index].text
        el = titles[rand_index]

        with allure.step(f'Выбрать товар: {t}'):
            self.product_title.scroll_to_element(el)
            self.product_title.click(el)

        return t, p
