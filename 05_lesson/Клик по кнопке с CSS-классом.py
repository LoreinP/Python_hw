from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("htt://www.example.com")

for i in range(3):
    blue_button = driver.find_element(By.CSS_SELECTOR,"button[class = 'btn btn-primary']")
    blue_button.click()


driver.quit()