import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@allure.title("Validate Purchase Total Process")
def test_purchase_total(driver):
    with allure.step("Navigating to Sauce Demo website"):
        driver.get("https://www.saucedemo.com/")

    with allure.step("Enter username"):
        user_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        user_name.clear()
        user_name.send_keys("standard_user")

    with allure.step("Click the login button"):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        ).click()

    with allure.step("Add Sauce Labs Backpack to cart"):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        ).click()

    with allure.step("Add Sauce Labs Bolt T-Shirt to cart"):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))
        ).click()

    with allure.step("Add Sauce Labs Onesie to cart"):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie"))
        ).click()

    with allure.step("Navigate to shopping cart"):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        ).click()

    with allure.step("Click checkout"):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

    with allure.step("Fill in first name"):
        first_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        first_name_input.send_keys("Лариса")

    with allure.step("Fill in last name and email"):
        last_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "last-name"))
        )
        last_name_input.send_keys("Позднякова")

        postal_code_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "postal-code"))
        )
        postal_code_input.send_keys("135135")

    with allure.step("Click continue to finish the purchase"):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue"))
        ).click()

    with allure.step("Verify if the purchase is successful"):

        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
        ).text
        assert success_message == "Total: $58.29"