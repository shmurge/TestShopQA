import allure
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

    def main_page_is_displayed(self):
        with allure.step('Отображается главная страница'):
            assert self.search_input.is_visible(), 'Главная страница не отображается!'

