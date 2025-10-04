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
        self.ec = EC

    def open(self, page_url=None):
        page_url = page_url if page_url else self.PAGE_URL
        with allure.step(f'Открыть страницу: {page_url}'):
            self.browser.get(page_url)

    def is_opened(self, page_url=None):
        page_url = page_url if page_url else self.PAGE_URL
        with allure.step(f'Страница {page_url} открыта'):
            self.wait.until(EC.url_to_be(page_url))

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

        return screenshot_name

    def assert_data_equal_data(self, act_res, exp_res, message):
        assert act_res == exp_res, (f'{message}!\n'
                                    f'ОР: {exp_res}\n'
                                    f'ФР: {act_res}\n'
                                    f'{self.attach_screenshot("Screenshot")} прикреплен')

    def assert_data_in_data(self, act_res, exp_res, message):
        assert act_res in exp_res, (f'{message}!\n'
                                    f'{self.attach_screenshot("Screenshot")} прикреплен')

    def assert_data_not_in_data(self, act_res, exp_res, message):
        assert act_res not in exp_res, (f'{message}!\n'
                                        f'{self.attach_screenshot("Screenshot")} прикреплен')
