from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from math import log, sin
import time, re

link = "http://suninjuly.github.io/explicit_wait2.html"
driver = webdriver.Chrome()
driver.get(link)


# Ищет значение оптимальной цены в заданном месте
def get_op():
    text = driver.find_element(By.XPATH, "//body/div/p[2]").text
    regex = r"(\$.+?)(?=\.)"
    match = re.findall(regex, text)
    return match[0]


# Находит формулу в тексте и вычисляет ее со значением x
def func_x(text, x):
    regex = r"([^\s]+)(?=,)"
    match = re.findall(regex, text)
    func = match[0].replace('ln', 'log')
    res = eval(func.replace('x', x))
    return res


try:
    optimal_price = get_op()
    # Ждет 12 сек пока значение в искомой области станет равно опимальной цене и нажимает кнопку
    price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), optimal_price))
    button_1 = driver.find_element(By.ID, "book")
    button_1.click()

    text = driver.find_element(By.CSS_SELECTOR, "label .nowrap:first-child").text
    x = driver.find_element(By.ID, "input_value").text
    res = func_x(text, x)

    input_1 = driver.find_element(By.ID, "answer")
    input_1.send_keys(res)
    # Прокручивает страницу на 300px для нажатия на кнопку
    ActionChains(driver).scroll_by_amount(0, 300)

    button_2 = driver.find_element(By.ID, "solve")
    button_2.click()
finally:
    time.sleep(15)
    driver.quit()
