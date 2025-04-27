from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def set_delay(self, delay: int) -> None:
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(str(delay))

    def click_number(self, number: int) -> None:
        self.driver.find_element(By.XPATH, f"//span[text()='{number}']").click()

    def click_operator(self, operator: str) -> None:
        self.driver.find_element(By.XPATH, f"//span[text()='{operator}']").click()

    def click_equals(self) -> None:
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    def get_result(self, timeout: int = 46) -> str:
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text