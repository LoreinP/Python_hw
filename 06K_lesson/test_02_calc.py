import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calc_submission(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    browser.find_element(By.XPATH, "//span[text()='7']").click()
    browser.find_element(By.XPATH, "//span[text()='+']").click()
    browser.find_element(By.XPATH, "//span[text()='8']").click()
    browser.find_element(By.XPATH, "//span[text()='=']").click()

    delay = browser.find_element(By.CSS_SELECTOR, "input#delay")
    delay.clear()
    delay.send_keys("45")

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    browser.quit()
