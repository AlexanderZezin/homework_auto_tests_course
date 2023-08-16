from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin
import time, re


def func_x():
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    text = browser.find_element(By.CSS_SELECTOR, "div form div .nowrap:first-child").text
    regex = r"([^\s]+)(?=,)"
    match = re.findall(regex, text)
    func = match[0].replace('ln', 'log')
    res = eval(func.replace('x', x))
    return res


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = func_x()

    input_1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_1.send_keys(x)

    option_1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option_1.click()

    option_2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option_2.click()

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
