import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.wait = WebDriverWait(browser, timeout=15, poll_frequency=1)

    def open(self):
        with allure.step(f'Открыть страницу: {self.PAGE_URL}'):
            self.browser.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f'Страница {self.PAGE_URL} открыта'):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def open_link_in_new_tab(self, element):
        with allure.step('Открыть в новой вкладке'):
            action = AC(self.browser)
            action.key_down(Keys.COMMAND)
            action.click(element)
            action.key_up(Keys.COMMAND)
            action.perform()

    @allure.step('Переключиться на новую вкладку')
    def switch_to_new_tab(self):
        tabs = self.browser.window_handles
        self.browser.switch_to.window(tabs[1])

    @allure.step('Переключиться на предыдущую вкладку')
    def switch_to_previous_tab(self):
        tabs = self.browser.window_handles
        self.browser.switch_to.window(tabs[0])

    @allure.step('Прикрепить скриншот')
    def attach_screenshot(self, screenshot_name):
        allure.attach(
            body=self.browser.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )
