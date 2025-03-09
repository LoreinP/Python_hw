from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome = webdriver.Firefox()
wait = WebDriverWait(chrome, 20)

chrome.get("http://uitestingplayground.com/ajax")


click_button = chrome.find_element(By.CSS_SELECTOR, ('button[class="btn btn-primary"]')).click()
green_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))).text

print(green_text)


chrome.quit()

