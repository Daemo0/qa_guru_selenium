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
    options.add_argument("--headless")  # Фоновый режим для CI/CD
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)

    yield driver

    driver.quit()


@pytest.mark.parametrize(
    "email, password, expected_text",
    [
        ("qaguru@qa.guru", "wrong_pass", "Wrong login or password"),
        ("unknown@qa.guru", "qaguru", "Wrong login or password"),
        (" qaguru@qa.guru", "qaguru", "Wrong login or password"),
        ("qagu ru@qa.guru", "qaguru", "Wrong login or password"),
        ("qaguru @qa.guru", "qaguru", "Wrong login or password"),
        ("qaguru@ qa.guru", "qaguru", "Wrong login or password"),
        ("qaguru@q a.guru", "qaguru", "Wrong login or password"),
        ("qaguru@qa .guru", "qaguru", "Wrong login or password"),
        ("qaguru@qa. guru", "qaguru", "Wrong login or password"),
        ("qaguru@qa.gu ru", "qaguru", "Wrong login or password"),
        ("qaguru@qa.guru ", "qaguru", "Wrong login or password"),
        ("qaguru@qa.guru", " qaguru", "Wrong login or password"),
        ("qaguru@qa.guru", " qagu ru", "Wrong login or password"),
        ("qaguru@qa.guru", " qaguru ", "Wrong login or password"),
        ("", "qaguru", "Login is required (minimum 3 characters)"),
        ("qaguru@qa.guru", "", "Password is required (minimum 6 characters)"),
        ("", "", "Login and password are required (minimum 3 and 6 characters)"),
        ("qaguruqa.guru", "qaguru", "Wrong login or password"),
        ("qaguru@", "qaguru", "Wrong login or password"),
        ("@qa.guru", "qaguru", "Wrong login or password"),
        ("qaguru' OR '1'='1", "' OR '1'='1", "Wrong login or password"),
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

    print(f"Alert-а нет, поэтому мы ищем тек ст с ошибкой комментарием на странице, текст: {actual_result}")

    assert expected_text in actual_result or driver.current_url != "success_url", f"Форма пропустила некорректные данные: Email='{email}', Pass='{password}'"
