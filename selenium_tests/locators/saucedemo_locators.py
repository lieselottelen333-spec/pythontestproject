from selenium.webdriver.common.by import By


class LoginLocators:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")


class ProductLocators:
    ADD_BACKPACK = (
        By.ID, "add-to-cart-sauce-labs-backpack"
    )
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")


class CartLocators:
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    REMOVE_BACKPACK = (
        By.ID, "remove-sauce-labs-backpack"
    )
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING = (
        By.ID, "continue-shopping"
    )


class CheckoutLocators:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_MESSAGE = (
        By.CLASS_NAME, "complete-header"
    )