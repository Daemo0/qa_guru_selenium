import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://qa-guru.github.io/one-page-form/login.html"


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(BASE_URL)

    yield driver

    driver.quit()


POSITIVE_TEST_DATA = [
    {
        "login": "qaguru@qa.guru",
        "password": "qaguru"
    },

    {
        "login": "QAGURU@QA.GURU",
        "password": "qaguru"},
]

NEGATIVE_TEST_LOGIN = [
    "qaguru@qa.guru",
    "unknown@qa.guru",
    " qaguru@qa.guru",
    "qagu ru@qa.guru",
    "qaguru @qa.guru",
    "qaguru@ qa.guru",
    "qaguru@q a.guru",
    "qaguru@qa .guru",
    "qaguru@qa. guru",
    "qaguru@qa.gu ru",
    "qaguru@qa.guru ",
    "qaguruqa.guru",
    "qaguru@",
    "@qa.guru",
]

NEGATIVE_TEST_PASSWORD = [
    " qaguru",
    " qagu ru",
    " qaguru ",
]

SQL_PAYLOADS = [
    "' UNION SELECT null, username, password FROM users --",
    "1' OR '1'='1",
    "SELECT * FROM users WHERE username = 'admin' AND password = ''"
]

XSS_PAYLOADS = [
    "<script>alert('XSS')</script>",
    "<iframe src='javascript:alert('XSS')'></iframe>",
    "&#x3C;script&#x3E;alert('XSS')&#x3C;/script&#x3E;",
]


class Locators:
    LOGIN = (By.ID, "login-input")
    PASSWORD = (By.ID, "password-input")
    SUBMIT = (By.ID, "submit-button")
    STATUS_MESSAGE = (By.ID, "error-message")


def clear_form(driver):
    driver.find_element(*Locators.LOGIN).clear()
    driver.find_element(*Locators.PASSWORD).clear()


def fill_form(driver, login, password):
    driver.find_element(*Locators.LOGIN).send_keys(login)
    driver.find_element(*Locators.PASSWORD).send_keys(password)


def click_submit(driver, timeout=10):
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(Locators.SUBMIT)).click()


def submit_and_wait_result(driver, timeout=10):
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(Locators.SUBMIT)).click()
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(Locators.STATUS_MESSAGE)).click()


def get_error_text(driver):
    return driver.find_element(*Locators.STATUS_MESSAGE).text


def is_error_visible(driver):
    return driver.find_element(*Locators.STATUS_MESSAGE).is_displayed()


class TestLoginForm:

    @pytest.mark.positive
    @pytest.mark.parametrize("test_data", POSITIVE_TEST_DATA)
    def test_positive_validation(self, driver, test_data):
        fill_form(driver, test_data["login"], test_data["password"])
        submit_and_wait_result(driver)
        result_text = get_error_text(driver)

        assert "Welcome!" not in result_text, f"Ожидалась ошибка, но получено: '{result_text}'"

        print(f"Positive tests passed")

    @pytest.mark.negitive
    @pytest.mark.parametrize("invalid_login", NEGATIVE_TEST_LOGIN)
    def test_negative_login(self, driver, invalid_login):
        fill_form(driver, invalid_login, "qaguru")
        submit_and_wait_result(driver)
        result_text = get_error_text(driver)

        assert "Wrong login or password" in result_text, f"Ожидалась ошибка, но получено: '{result_text}'"

    @pytest.mark.negitive
    @pytest.mark.parametrize("invalid_password", NEGATIVE_TEST_PASSWORD)
    def test_negative_login(self, driver, invalid_password):
        fill_form(driver, "qaguru@qaguru.ru", invalid_password)
        submit_and_wait_result(driver)
        result_text = get_error_text(driver)

        assert "Wrong login or password" in result_text, f"Ожидалась ошибка, но получено: '{result_text}'"

    @pytest.mark.negative
    def test_negative_empty_form(self, driver):
        click_submit(driver)

        assert is_error_visible(driver), "Error message не появился при отправке пустой формы"
        print("Negative test: empty form passed")

    @pytest.mark.negative
    def test_negative_empty_login(self, driver):
        fill_form(driver, '', "qaguru")
        submit_and_wait_result(driver)
        result_text = get_error_text(driver)

        assert "Login is required (minimum 3 characters)" in result_text, "Error message не появился при отправке пустого логина"
        print("Negative test: empty login passed")

    @pytest.mark.negative
    def test_negative_empty_password(self, driver):
        fill_form(driver, 'qaguru@qaguru.ru', "")
        submit_and_wait_result(driver)
        result_text = get_error_text(driver)

        assert "Password is required (minimum 6 characters)" in result_text, "Error message не появился при отправке пустого пароля"
        print("Negative test: empty password passed")

    @pytest.mark.security
    @pytest.mark.parametrize("payload", SQL_PAYLOADS)
    def test_security_sql_injection(self, driver, payload):
        fill_form(driver, payload, payload)
        click_submit(driver)

        page_source = driver.page_source.lower()
        assert "sql" in page_source or "error" in page_source, f"SQL-инъекция вызвала ошибку: {payload[:20]}..."

        print(f"SQL-инъекция безопасна: {payload[:20]}...")

    @pytest.mark.security
    @pytest.mark.parametrize("payload", XSS_PAYLOADS)
    def test_security_xss_injection(self, driver, payload):
        fill_form(driver, payload, payload)
        click_submit(driver)

        page_source = driver.page_source
        assert "alert" not in page_source.lower() or "&lt;" in page_source, f"XSS-инъекция не экранирована: {payload[:30]}..."

        print(f"XSS-инъекция безопасна: {payload[:30]}...")
