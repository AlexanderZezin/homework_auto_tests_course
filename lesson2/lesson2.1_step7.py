from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin
import re, time

def func_x(x):
    text = browser.find_element(By.CSS_SELECTOR, "div form div .nowrap:first-child").text
    regex = r"([^\s]+)(?=,)"
    match = re.findall(regex, text)
    func = match[0].replace('ln', 'log')
    res = eval(func.replace('x', x))
    return res


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elem = browser.find_element(By.ID, "treasure")
    x = elem.get_attribute("valuex")
    res = func_x(x)

    input_1 = browser.find_element(By.ID, "answer")
    input_1.send_keys(res)

    option_1 = browser.find_element(By.ID, "robotCheckbox")
    option_1.click()

    option_2 = browser.find_element(By.ID, "robotsRule")
    option_2.click()

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
