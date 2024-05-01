import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time, math

lst_url = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]


@pytest.mark.parametrize('url', lst_url)
def test_authorization(browser, url):
    browser.get(f"{url}")
    browser.implicitly_wait(10)

    button1 = browser.find_element(By.ID, "ember33")
    button1.click()

    input1 = browser.find_element(By.ID, "id_login_email")
    input1.send_keys("alexanderzezin@gmail.com")

    input2 = browser.find_element(By.ID, "id_login_password")
    input2.send_keys("graby31415926")

    button1 = browser.find_element(By.CSS_SELECTOR, ".button_with-loader")
    button1.click()
    time.sleep(5)
    if WebDriverWait(browser, 15).until(
            expected_conditions.url_to_be(f"{url}?auth=login")):
        input3 = browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area")
        input3.send_keys(f"{math.log(int(time.time() + 4.3))}")

    button2 = WebDriverWait(browser, 15).until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
    )

    button2.click()

    text = WebDriverWait(browser, 15).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint"))).text

    with open("pytest.txt", "a+") as file:
        if text != "Correct!":
            file.write(text + ' ')
