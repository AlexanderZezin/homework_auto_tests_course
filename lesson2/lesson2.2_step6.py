from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
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
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value").text
    text = browser.find_element(By.XPATH, "//body/div/form/div[1]/label/span[1]").text
    res = func_x(x)
    input_1 = browser.find_element(By.ID, "answer")
    input_1.send_keys(res)

    ActionChains(browser).scroll_by_amount(0, 170).perform()
    time.sleep(1)

    option_1 = browser.find_element(By.ID, "robotCheckbox")
    option_1.click()

    option_2 = browser.find_element(By.ID, "robotsRule")
    option_2.click()
    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

