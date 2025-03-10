from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

sleep(10)

button = driver.find_element(By.CSS_SELECTOR, "button")
for bu in range(5):
    button.click()

delete_button = driver.find_elements(By.CLASS_NAME, "added_mannually")

sleep(5)

driver.quit()

