import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test01():
    print("Проверка ввода текущего адреса")

    driver = webdriver.Chrome()

    try:
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)

        full_name_field = driver.find_element(By.ID, "userName")

        full_name_field.send_keys("Иван Иванов")

        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivan@example.com")

        current_address_field = driver.find_element(By.ID, "currentAddress")
        current_address_field.send_keys("г. Караганда, ул. Садовая, д. 1, кв. 2")

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, "output")

        assert "г. Караганда, ул. Садовая, д. 1, кв. 2" in result_box.text
        print("Тест успешно пройден!")

    finally:
        driver.quit()


def test02():
    print("Проверка ввода постоянного адреса")

    driver = webdriver.Chrome()

    try:
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)

        full_name_field = driver.find_element(By.ID, "userName")

        full_name_field.send_keys("Иван Иванов")

        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivan@example.com")

        permanent_address_field = driver.find_element(By.ID, "permanentAddress")
        permanent_address_field.send_keys("г. Чебоксары, ул. Полевая, д. 3, кв. 4")

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, "output")

        assert "г. Чебоксары, ул. Полевая, д. 3, кв. 4" in result_box.text
        print("Тест успешно пройден!")

    finally:
        driver.quit()


test01()
test02()