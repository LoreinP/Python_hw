from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get = ("https://uitestingplayground.com/dinamicid")

button_without_id = driver.find_element(By.CSS_SELECTOR,"button.btn-primary")
button_without_id.click()

driver.quit()
