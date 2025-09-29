import allure

from elements.base_element import BaseElement


class Button(BaseElement):

    def __init__(self, browser, name, how, what):
        super().__init__(browser, name, how, what)

        self.name = f'Кнопка: {name}'
