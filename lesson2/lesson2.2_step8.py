from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elems_input = browser.find_elements(By.CLASS_NAME, "form-control")
    for elem in elems_input:
        elem.send_keys("ggg")

    with open("text.txt", 'w') as file:
        pass

    elem = browser.find_element(By.ID, "file")
    elem.send_keys(os.path.abspath("text.txt"))

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
