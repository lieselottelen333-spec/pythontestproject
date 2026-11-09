import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_tests.locators.saucedemo_locators import LoginLocators


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())

    browser = webdriver.Chrome(service=service)
    browser.maximize_window()

    yield browser

    browser.quit()


@pytest.fixture
def authorized_user(driver):

    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    # Ввод логина
    wait.until(
        EC.visibility_of_element_located(
            LoginLocators.USERNAME
        )
    ).send_keys("standard_user")

    # Ввод пароля
    driver.find_element(
        *LoginLocators.PASSWORD
    ).send_keys("secret_sauce")

    # Нажатие кнопки авторизации
    driver.find_element(
        *LoginLocators.LOGIN_BUTTON
    ).click()

    # Проверка успешной авторизации
    wait.until(
        EC.url_contains("inventory.html")
    )

    return driver