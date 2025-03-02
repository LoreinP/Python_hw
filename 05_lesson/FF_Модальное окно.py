from time import sleep
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# открыть страницу
driver.get("http://the-internet.herokuapp.com/entry_ad/.")

sleep(5)

# нажать на кнопку Close
close_button = driver.find_element(By.CSS_SELECTOR, ".modal-footer .close-button")
close_button.click()

sleep(5)

alert = Alert(driver)
alert.accept()

sleep(10)

driver.quit()




