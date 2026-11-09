from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_tests.locators.saucedemo_locators import (
    ProductLocators,
    CartLocators
)


def test_clear_cart(authorized_user):

    driver = authorized_user
    wait = WebDriverWait(driver, 10)

    # 1. Добавление товара в корзину
    driver.find_element(
        *ProductLocators.ADD_BACKPACK
    ).click()

    # 2. Открытин корзины
    driver.find_element(
        *ProductLocators.CART_ICON
    ).click()

    # 3. Товар добавлен
    wait.until(
        EC.visibility_of_element_located(
            CartLocators.CART_ITEM
        )
    )

    # 4. Удаление товара
    driver.find_element(
        *CartLocators.REMOVE_BACKPACK
    ).click()

    # 5.  Корзина пустая
    wait.until(
        EC.invisibility_of_element_located(
            CartLocators.CART_ITEM
        )
    )

    assert len(
        driver.find_elements(*CartLocators.CART_ITEM)
    ) == 0, "Корзина не пустая"

    # 6. Возвращение в каталог
    driver.find_element(
        *CartLocators.CONTINUE_SHOPPING
    ).click()

    # 7. Проверка возврата в каталог
    wait.until(
        EC.url_contains("inventory.html")
    )

    assert "inventory.html" in driver.current_url, \
        "Пользователь не вернулся в каталог"