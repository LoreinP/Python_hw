from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")

input = driver.find_element(By.CSS_SELECTOR, '.form-control')

input.send_text = ('SkyPro')

button = driver.find_element(By.CSS_SELECTOR, '#updatingButton')
button.click()
#name = button.find_element(By.CSS_SELECTOR, "innerText")

print(button.text)

driver.quit()