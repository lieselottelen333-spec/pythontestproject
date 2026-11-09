import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_tests.locators.saucedemo_locators import (
    ProductLocators,
    CartLocators,
    CheckoutLocators
)


@allure.suite("Покупка")
@allure.title("Успешная покупка товара")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "richter")
def test_successful_purchase(authorized_user):
    driver = authorized_user
    wait = WebDriverWait(driver, 10)

    with allure.step("Добавление товара в корзину"):
        driver.find_element(*ProductLocators.ADD_BACKPACK).click()

    with allure.step("Открытие корзины"):
        driver.find_element(*ProductLocators.CART_ICON).click()

    with allure.step("Проверка наличия товара в корзине"):
        item = wait.until(EC.visibility_of_element_located(CartLocators.CART_ITEM))
        assert item.is_displayed(), "Товар не найден в корзине"

    with allure.step("Переход к оформлению заказа"):
        driver.find_element(*CartLocators.CHECKOUT_BUTTON).click()

    with allure.step("Заполнение данных покупателя"):
        driver.find_element(*CheckoutLocators.FIRST_NAME).send_keys("Olga")
        driver.find_element(*CheckoutLocators.LAST_NAME).send_keys("Tester")
        driver.find_element(*CheckoutLocators.POSTAL_CODE).send_keys("12345")

    with allure.step("Продолжение оформления"):
        driver.find_element(*CheckoutLocators.CONTINUE_BUTTON).click()

    with allure.step("Завершение покупки"):
        driver.find_element(*CheckoutLocators.FINISH_BUTTON).click()

    with allure.step("Проверка успешного завершения покупки"):
        success = wait.until(EC.visibility_of_element_located(CheckoutLocators.SUCCESS_MESSAGE))
        assert success.text == "Thank you for your order!", "Покупка не была успешно завершена"