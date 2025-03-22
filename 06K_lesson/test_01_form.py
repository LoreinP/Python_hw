import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_but(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, "firstName").send_keys("Иван")
    driver.find_element(By.NAME, "lastName").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "email").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip").send_keys("")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR,"button[type=`submit`]").click()

    wait = WebDriverWait(driver,15)

    success_messege = wait.until(EC.visibility_of_element_located((By.XPATH, "//dif[contains(@class, alert-success')]")))
    alert_danger_color = "rgba(248, 215, 218, 1)"
    color_zip = zip.value_of_css_property("background-color")

    assert color_zip == alert_danger_color, f"Expected {alert_danger_color}, but got {color_zip}"

    alert_success_color = "rgba(209, 231, 221, 1)"
    fields = [first_name, last_name, address, email, phone_number, city, country, job_position, company]

    for field in fields:
        field_color = field.value_of_property("background-color")

    assert field_color == alert_success_color, f"Expected {alert_success_color} for {field.get_attribute('name')}, but got {field_color}"

    driver.quit()













