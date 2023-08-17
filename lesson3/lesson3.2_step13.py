from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


def page(link):
    driver = webdriver.Chrome()
    driver.get(link)
    driver.implicitly_wait(5)
    input_1 = driver.find_element(By.XPATH, "//body/div[1]/form/div[1]/div[1]/input")
    input_1.send_keys("FirstName")
    input_2 = driver.find_element(By.XPATH, "//body/div[1]/form/div[1]/div[2]/input")
    input_2.send_keys("LastName")
    input_3 = driver.find_element(By.XPATH, "//body/div[1]/form/div[1]/div[3]/input")
    input_3.send_keys("e-mail")
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    welcome_text = driver.find_element(By.TAG_NAME, "h1").text
    return welcome_text


# Класс должен начинаться с "Test..." имена методов в классе - "test_..."
# Класс должен наследоваться от unittest.TestCase
class TestAbs(unittest.TestCase):
    def test_first_page(self):
        self.assertEqual(page(link = "http://suninjuly.github.io/registration1.html"),
                         second="Congratulations! You have successfully registered!",
                         msg="Test_1: OK")

    def test_second_page(self):
        self.assertEqual(page(link = "http://suninjuly.github.io/registration2.html"),
                         second="Congratulations! You have successfully registered!",
                         msg="Test_2: OK")


if __name__ == '__main__':
    unittest.main()
