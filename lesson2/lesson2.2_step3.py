from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num_1 = browser.find_element(By.ID, "num1").text
    op = browser.find_element(By.XPATH, "//body/div/form/h2/span[3]").text.strip()
    num_2 = browser.find_element(By.ID, "num2").text
    res = eval(f"{num_1}{op}{num_2}")

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(res))

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()