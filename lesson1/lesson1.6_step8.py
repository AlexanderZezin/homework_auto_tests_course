import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_1 = browser.find_element(By.NAME, "first_name")
    input_1.send_keys("Name")

    input_2 = browser.find_element(By.NAME, "last_name")
    input_2.send_keys("Lastname")

    input_3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input_3.send_keys("Moskow")

    input_4 = browser.find_element(By.ID, "country")
    input_4.send_keys("Russia")

    button = browser.find_element(By.XPATH, "//body/div/form/div[6]/button[3]")
    button.click()
finally:
    time.sleep(30)
    browser.quit()