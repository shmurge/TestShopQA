from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from elements.base_element import BaseElement


class Input(BaseElement):

    def __init__(self, browser, name, how, what):
        super().__init__(browser, name, how, what)

        self.name = f'Поле: {name}'

    def clear_input(self):
        action = AC(self.browser)
        input_1 = self.get_element()
        input_value = input_1.get_attribute("value")

        while len(input_value) > 0:
            self.wait.until(EC.element_to_be_clickable(self.locator))
            action.double_click(input_1)
            action.send_keys_to_element(input_1, Keys.BACKSPACE).perform()
            input_value = input_1.get_attribute("value")

    def fill_input(self, data):
        action = AC(self.browser)
        input_1 = self.get_element()

        self.wait.until(EC.element_to_be_clickable(self.locator))
        action.click(input_1)
        action.send_keys_to_element(input_1, data).perform()

        return data

    def fill_autocomplete_input(self, data):
        action = AC(self.browser)
        input_1 = self.get_element()
        self.wait.until(EC.element_to_be_clickable(self.locator))
        action.click(input_1)
        action.send_keys_to_element(input_1, data)
        action.send_keys_to_element(input_1, Keys.ENTER).perform()

        return data

    def get_placeholder(self):
        return self.get_element().get_attribute('placeholder').strip()
