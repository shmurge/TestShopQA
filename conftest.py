import os

import pytest
import allure

from dotenv import load_dotenv
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Choose browser: chrome or firefox')
    parser.addoption('--headless', action='store_true', help='Launching the browser in headless mode')
    parser.addoption('--github_actions', action='store_true', help='Launching on Firefox in github actions')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    headless = request.config.getoption("--headless")
    github_actions = request.config.getoption("--github_actions")
    browser = None

    with allure.step(f"Запуск браузера: {browser_name}."):
        if browser_name == "chrome":
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--disable-notifications")
            if headless:
                with allure.step("Браузер запущен в фоновом режиме"):
                    chrome_options.add_argument('--headless')
                    chrome_options.add_argument('--disable-gpu')
                    chrome_options.add_argument('--no-sandbox')
                    chrome_options.add_argument('--disable-dev-shm-usage')
            browser = webdriver.Chrome(options=chrome_options)
        elif browser_name == "firefox":
            firefox_options = FirefoxOptions()
            firefox_service = FirefoxService(
                executable_path="/snap/bin/geckodriver")  # если сломается, убрать эту строку
            firefox_options.add_argument("--disable-notifications")
            if headless:
                with allure.step("Браузер запущен в фоновом режиме"):
                    firefox_options.add_argument("--headless")
                    firefox_options.add_argument('--disable-gpu')
                    firefox_options.add_argument('--no-sandbox')
                    firefox_options.add_argument('--disable-dev-shm-usage')
            if github_actions:
                browser = webdriver.Firefox(options=firefox_options, service=firefox_service)  # и отсюда убрать service
            else:
                browser = webdriver.Firefox(options=firefox_options)
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser.maximize_window()

    yield browser
    browser.quit()


@pytest.fixture()
def pre_login(browser):
    load_dotenv()

    page = LoginPage(browser)
    page.open()
    page.fill_login_form(
        login=os.getenv('LOGIN'),
        password=os.getenv('PASSWORD')
    )
    page = AccountPage(browser)

    page.user_information_is_correct(
        username=os.getenv('USERNAME'),
        user_email=os.getenv('LOGIN')
    )

@pytest.fixture()
def pre_goto_prod_page(browser):
    page = MainPage(browser)
    page.open()
    page.is_opened()
    page.select_random_product()
