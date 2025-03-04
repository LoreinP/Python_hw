from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get('http://the-internet.herokuapp.com/add_remove_elements/')


sleep(10)


# 5 раз кликнуть на кнопку
button = webdriver.find_element(By.CSS_SELECTOR, "#Add element")
for bu in range(5):
     button.click(bu)


# собрать список кнопок Delete
# delete_button = webdriver.find_element(By.CSS_SELECTOR, "button.added_mannually")
# print(len(delete_button))
# вывести размер списка


sleep(5)


# вывести размер списка
# sleep(5)

