import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_tests.locators.saucedemo_locators import LoginLocators


@allure.suite("Авторизация")
@allure.title("Неуспешная авторизация с невалидными данными")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "richter")
def test_invalid_login(driver):
    wait = WebDriverWait(driver, 10)

    with allure.step("Открытие сайта"):
        driver.get("https://www.saucedemo.com/")

    with allure.step("Ввод логина"):
        driver.find_element(*LoginLocators.USERNAME).send_keys("standard_user")

    with allure.step("Ввод неправильного пароля"):
        driver.find_element(*LoginLocators.PASSWORD).send_keys("wrong_password")

    with allure.step("Нажатие кнопки входа"):
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    with allure.step("Проверка сообщения об ошибке"):
        error = wait.until(EC.visibility_of_element_located(LoginLocators.ERROR_MESSAGE))
        assert "Username and password do not match" in error.text, \
            "Не отображается корректное сообщение об ошибке"

    with allure.step("Проверка, что пользователь остался на странице логина"):
        assert "inventory.html" not in driver.current_url, \
            "Пользователь смог войти с неправильными данными"