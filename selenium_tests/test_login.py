from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_tests.locators.saucedemo_locators import LoginLocators


def test_invalid_login(driver):

    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    # 1. Авторизация
    driver.find_element(
        *LoginLocators.USERNAME
    ).send_keys("standard_user")

    # 2. Неправильный пароль
    driver.find_element(
        *LoginLocators.PASSWORD
    ).send_keys("wrong_password")

    # 3. Кнопка входа
    driver.find_element(
        *LoginLocators.LOGIN_BUTTON
    ).click()

    # 4. Появление сообщения об ошибке
    error = wait.until(
        EC.visibility_of_element_located(
            LoginLocators.ERROR_MESSAGE
        )
    )

    # 5.  Текст ошибки
    assert "Username and password do not match" in error.text, \
        "Не отображается корректное сообщение об ошибке"

    # 6.  Пользователь остался на странице авторизации
    assert "inventory.html" not in driver.current_url, \
        "Пользователь смог войти с неправильными данными"