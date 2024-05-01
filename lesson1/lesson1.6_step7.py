import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # Поиск всех элементов с тегом 'input'
    # .find_elements возвращает список найденых элементов или [] если нет элементов
    elements = browser.find_elements(By.TAG_NAME, "input")
    for elem in elements:
        elem.send_keys("Привет")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
