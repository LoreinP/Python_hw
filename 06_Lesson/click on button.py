from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/ajax")

driver.implicitly_wait(20)

driver.find_element(By.ID, "ajaxButton").click()

element = driver.find_element(By.CSS_SELECTOR, "p.bg-success")

print(element.text)

driver.quit()
