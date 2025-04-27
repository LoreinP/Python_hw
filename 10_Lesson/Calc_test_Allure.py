import allure
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Калькулятор")
@allure.title("Тестирование сложения")
@allure.description("Проверка функциональности сложения на калькуляторе")
@allure.severity(allure.severity_level.NORMAL)
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def tearDown(self):
        self.driver.quit()

    @allure.step("Отправка математического выражения {query}")
    def send(self, query: str) -> None:
        input_field = self.driver.find_element(By.ID, 'delay')
        input_field.clear()
        input_field.send_keys(query)

    @allure.step("Выполнение операции 7 + 8")
    def get_operations(self) -> None:
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    @allure.step("Проверка результата")
    def check_result(self) -> bool:
        return WebDriverWait(self.driver, 46).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )

    @allure.step("Выполнение теста сложения")
    def test_addition(self):
        self.send("7 + 8")
        self.get_operations()
        result = self.check_result()
        assert result, "Ожидаемый результат не найден: '15'"

