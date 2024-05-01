from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin
import time, re

link = "http://suninjuly.github.io/redirect_accept.html"
driver = webdriver.Chrome()
driver.get(link)


def func_x(text, x):
    regex = r"([^\s]+)(?=,)"
    match = re.findall(regex, text)
    func = match[0].replace('ln', 'log')
    res = eval(func.replace('x', x))
    return res


try:
    button = driver.find_element(By.CSS_SELECTOR, "button.trollface")
    button.click()

    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

    text = driver.find_element(By.XPATH, "//body/form/div/div/div/label/span[1]").text
    x = driver.find_element(By.ID, "input_value").text
    res = func_x(text, x)

    input_1 = driver.find_element(By.ID, "answer")
    input_1.send_keys(res)

    button = driver.find_element(By.CSS_SELECTOR, ".btn")
    button.click()
finally:
    time.sleep(10)
    driver.quit()
