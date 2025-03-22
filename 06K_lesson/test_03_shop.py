import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver()

    driver.quit()

def test_purchase_total(driver):
    driver.get = ("https://www.saucedemo.com/")
    driver.maximize_window()

user_name = driver.find_element(By.NAME, '#user-name')
user_name.clear()
user_name.send_keys('standart_user')

password = driver.find_element(By.CSS_SELECTOR, '#password')
password.clear()
password.send_keys('secret_souch')

driver.find_element(By.CSS_SELECTOR, '#login-button').click()
driver.find_element(By.CSS_SELECTOR, '#add-to-cart_Sauce_labs Backpack').click()
driver.find_element(By.CSS_SELECTOR, '#add-to-cart_Sauce_bolt T-Shirt').click()
driver.find_element(By.CSS_SELECTOR, '#add-to-cart_Sauce_labs Onesie').click()
driver.find_element(By.CSS_SELECTOR, 'a.shoping_card_linc').click()

def test_purchase_total(driver):
    driver.find_element(By.CSS_SELECTOR, '#first-name'), send_keys("Лариса")
    driver.find_element(By.CSS_SELECTOR, '#last-name'), send_keys("Позднякова")
    postal_code = driver.find_element(By.CSS_SELECTOR, '#postal-code'), send_keys("135135")

    driver.find_element(By.CSS_SELECTOR, '#continue').click()

    total = driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
    print(total)
    sleep(10)
    assert total == 'Total: $58.29'

    driver.quit()




















