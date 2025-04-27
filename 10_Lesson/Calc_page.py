import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.delay_input_selector = "#delay"
        self.buttons_xpath = {
            '7': "//span[text()='7']",
            '8': "//span[text()='8']",
            '+': "//span[text()='+']",
            '=': "//span[text()='=']"
        }
        self.result_selector = ".screen"

    def set_delay(self, delay: int) -> None:
        delay_input = self.driver.find_element(By.CSS_SELECTOR, self.delay_input_selector)
        delay_input.clear()
        delay_input.send_keys(str(delay))

    def click_button(self, button: str) -> None:
        button_xpath = self.buttons_xpath.get(button)
        if button_xpath:
            self.driver.find_element(By.XPATH, button_xpath).click()
        else:
            raise ValueError(f"Button {button} is not recognized.")

    def get_result(self) -> str:
        result_element = self.driver.find_element(By.CSS_SELECTOR, self.result_selector)
        return result_element.text

