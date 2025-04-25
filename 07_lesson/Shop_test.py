import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_purchase_total(driver):
    driver.get("https://www.saucedemo.com/")

    user_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    user_name.clear()
    user_name.send_keys("standard_user")

    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password.clear()
    password.send_keys("secret_sauce")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login-button"))).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie"))).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Лариса")

    driver.find_element(By.ID, "last-name").send_keys("Позднякова")
    driver.find_element(By.ID, "postal-code").send_keys("135135")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "continue"))).click()

    total = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))).text

    assert total == 'Total: $58.29'















