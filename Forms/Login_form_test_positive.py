import time

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

LOGIN_INPUT = (By.ID, "login-input")
PASSWORD_INPUT = (By.ID, "password-input")
SUBMIT_BUTTON = (By.ID, "submit-button")
STATUS_MESSAGE = (By.ID, "error-message")


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)

    yield driver

    driver.quit()


@pytest.mark.parametrize(
    "email, password, expected_text",
    [
        ("qaguru@qa.guru", "qaguru", "Welcome!"),
        ("QAGURU@QA.GURU", "qaguru", "Welcome!"),
    ]
)
def test_login_form(driver, email, password, expected_text):

    driver.get("https://qa-guru.github.io/one-page-form/login.html")

    email_field = driver.find_element(*LOGIN_INPUT)
    password_field = driver.find_element(*PASSWORD_INPUT)
    submit_button = driver.find_element(*SUBMIT_BUTTON)

    email_field.clear()
    email_field.send_keys(email)

    password_field.clear()
    password_field.send_keys(password)

    submit_button.click()

    actual_result = driver.find_element(*STATUS_MESSAGE).text

    time.sleep(3)

    print(f"Alert-а нет, поэтому мы ищем текст с ошибкой комментарием на странице, текст: {actual_result}")

    assert expected_text in actual_result, f"Ожидался успешный вход, но получено: '{actual_result}'"
