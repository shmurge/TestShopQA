from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class BaseElement:

    def __init__(self, browser: WebDriver, name, how, what):
        self.browser = browser
        self.name = name
        self.locator = how, what
        self.wait = WebDriverWait(browser, timeout=15, poll_frequency=1)

    def get_element(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.locator))
            return self.browser.find_element(*self.locator)
        except TimeoutException:
            f'Элемент {self.name} не найден!'

    def get_elements(self):
        self.wait.until(EC.visibility_of_element_located(self.locator))
        return self.browser.find_elements(*self.locator)

    def find_element_by_text(self, text):
        self.wait.until(EC.visibility_of_element_located(('xpath', f"//*[text()='{text}']")))
        element = self.browser.find_element('xpath', f"//*[text()='{text}']")

        return element

    def select_element_by_text(self, text):
        self.wait.until(EC.visibility_of_element_located(('xpath', f"//*[text()='{text}']")))
        element = self.browser.find_element('xpath', f"//*[text()='{text}']")
        self.wait.until(EC.element_to_be_clickable(element))
        element.click()

    def click(self, element=None):
        element = element if element else self.get_element()
        self.wait.until(EC.element_to_be_clickable(element))
        element.click()

    def double_click(self, element=None):
        element = element if element else self.get_element()
        self.wait.until(EC.element_to_be_clickable(element))
        action = AC(self.browser)
        action.double_click(element).perform()

    def submit(self, element=None):
        element = element if element else self.get_element()
        element.submit()

    def scroll_to_element(self, element=None):
        element = element if element else self.get_element()
        self.browser.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element
        )

    def move_to_element(self, element=None):
        element = element if element else self.get_element()
        action = AC(self.browser)
        action.move_to_element(element)
        action.perform()

    def get_text_of_element(self, element=None):
        element = element if element else self.get_element()

        return element.text.strip()

    def is_visible(self, timeout=15, frequency=1, element=None):
        element = element if element else self.locator
        self.wait = WebDriverWait(self.browser, timeout, frequency)
        try:
            self.wait.until(EC.visibility_of_element_located(element))
        except TimeoutException:
            return False
        return True

    def is_not_visible(self, timeout=1, frequency=0.5, element=None):
        element = element if element else self.locator
        self.wait = WebDriverWait(self.browser, timeout, frequency)
        try:
            self.wait.until(EC.invisibility_of_element_located(element))
        except TimeoutException:
            return False
        return True

    # def is_not_visible(self, timeout=1, frequency=0.5, element=None):
    #     element = element if element else self.locator
    #     self.wait = WebDriverWait(self.browser, timeout, frequency)
    #     try:
    #         self.wait.until_not(EC.visibility_of_element_located(element))
    #     except TimeoutException:
    #         return False
    #     return True

    def is_displayed(self, element=None):
        element = element if element else self.get_element()

        return element.is_displayed()

    def get_attribute(self, attribute, element=None):
        element = element if element else self.get_element()

        return element.get_attribute(attribute)
