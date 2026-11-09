from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_tests.locators.saucedemo_locators import (
    ProductLocators,
    CartLocators,
    CheckoutLocators
)


def test_successful_purchase(authorized_user):

    driver = authorized_user
    wait = WebDriverWait(driver, 10)

    # 1. Добавление товара в корзину
    driver.find_element(
        *ProductLocators.ADD_BACKPACK
    ).click()

    # 2. Открывтие корзины
    driver.find_element(
        *ProductLocators.CART_ICON
    ).click()

    # 3.  Наличие товара
    item = wait.until(
        EC.visibility_of_element_located(
            CartLocators.CART_ITEM
        )
    )

    assert item.is_displayed(), "Товар не найден в корзине"

    # 4. Checkout
    driver.find_element(
        *CartLocators.CHECKOUT_BUTTON
    ).click()

    # 5.  Данные покупателя
    driver.find_element(
        *CheckoutLocators.FIRST_NAME
    ).send_keys("Olga")

    driver.find_element(
        *CheckoutLocators.LAST_NAME
    ).send_keys("Tester")

    driver.find_element(
        *CheckoutLocators.POSTAL_CODE
    ).send_keys("12345")

    # 6.  Оформление
    driver.find_element(
        *CheckoutLocators.CONTINUE_BUTTON
    ).click()

    # 7. Завершение покупки
    driver.find_element(
        *CheckoutLocators.FINISH_BUTTON
    ).click()

    # 8. Проверка успешной покупки
    success = wait.until(
        EC.visibility_of_element_located(
            CheckoutLocators.SUCCESS_MESSAGE
        )
    )

    assert success.text == "Thank you for your order!", \
        "Покупка не была успешно завершена"