import pytest
import allure
import os
from dotenv import load_dotenv, set_key
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default='ru', help='Choose language: ru or en')
    parser.addoption('--headless', action='store_true', help='Launching the browser in headless mode')
    parser.addoption('--login', action='store_true', help='Launching the browser with pre conditions: login')
    parser.addoption('--github_actions', action='store_true', help='Launching on Firefox in github actions')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    user_language = request.config.getoption("language")
    headless = request.config.getoption("--headless")
    github_actions = request.config.getoption("--github_actions")
    browser = None

    with allure.step(f"Запуск браузера: {browser_name}.  Язык браузера: {user_language}"):
        if browser_name == "chrome":
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
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
            firefox_options.set_preference('intl.accept_languages', user_language)
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


def set_env_key(key, value):
    project_root = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(project_root, '.env')

    load_dotenv(env_path)

    os.environ[key] = value
    set_key(env_path, key, value)
