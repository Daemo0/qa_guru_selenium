import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://qa-guru.github.io/one-page-form/text-box.html"


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait(3)

    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 5)


POSITIVE_TEST_DATA = [
    {
        "name": "Денис Максимов",
        "email": "den.maximov@mail.ru",
        "current_address": "443000 Самара, ул. Буянова",
        "permanent_address": "443001 Самара, ул. Буянова",
        "expected": ["Денис Максимов", "den.maximov@mail.ru", "443000 Самара, ул. Буянова", "443001 Самара, ул. Буянова"]
    },
    {
        "name": "1",
        "email": "1@b.com",
        "current_address": "1",
        "permanent_address": "1",
        "expected": ["1", "1@b.com", "1", "1"]
    }
]

INVALID_EMAILS = [
    "d en.maximov@mail.ru",
    "den.max imov@mail.ru",
    "den.maximov @mail.ru",
    "den.maximov@ mail.ru",
    "den.maximov@ma il.ru",
    "d$n.m@x|mov@mail.ru",
    "@mail.ru",
    "den.maximov@.ru",
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
    USER_NAME = (By.ID, "userName")
    USER_EMAIL = (By.ID, "userEmail")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    SUBMIT = (By.ID, "submit")
    OUTPUT = (By.ID, "output")


def fill_form(driver, name, email, current_address, permanent_address):
    driver.find_element(*Locators.USER_NAME).send_keys(name)
    driver.find_element(*Locators.USER_EMAIL).send_keys(email)
    driver.find_element(*Locators.CURRENT_ADDRESS).send_keys(current_address)
    driver.find_element(*Locators.PERMANENT_ADDRESS).send_keys(permanent_address)


def click_submit(driver, wait):
    wait.until(EC.element_to_be_clickable(Locators.SUBMIT)).click()


def submit_and_wait_result(driver, wait):
    wait.until(EC.element_to_be_clickable(Locators.SUBMIT)).click()
    wait.until(EC.visibility_of_element_located(Locators.OUTPUT))


def get_result_text(driver):
    return driver.find_element(*Locators.OUTPUT).text


def is_output_visible(driver):
    return driver.find_element(*Locators.OUTPUT).is_displayed()


class TestTextBoxForm:

    @pytest.mark.positive
    @pytest.mark.parametrize("test_data", POSITIVE_TEST_DATA)
    def test_positive_valid_data(self, driver, wait, test_data):
        fill_form(driver, test_data["name"], test_data["email"], test_data["current_address"], test_data["permanent_address"])
        submit_and_wait_result(driver, wait)
        result_text = get_result_text(driver)

        assert test_data["name"] in result_text, "Имя не найдено"
        assert test_data["email"] in result_text, "Email не найден"
        assert test_data["current_address"] in result_text, "Адрес не найден"
        assert test_data["permanent_address"] in result_text, "Постоянный адрес не найден"

        print(f"Positive test passed: {test_data['name']}")

    @pytest.mark.negative
    @pytest.mark.parametrize("invalid_email", INVALID_EMAILS)
    def test_negative_email_special_chars(self, driver, wait, invalid_email):
        fill_form(driver, "Макс Денисов", invalid_email, "Адрес 1", "Адрес 2")
        click_submit(driver, wait)

        assert not is_output_visible(driver), f"Output появился при невалидном email '{invalid_email}'"
        print(f"{invalid_email} - отклонен")

    @pytest.mark.negative
    def test_negative_email_without_at(self, driver, wait):
        fill_form(driver, "Макс Денисов", "max.denisovexample.com", "Адрес 1", "Адрес 2")
        click_submit(driver, wait)

        assert not is_output_visible(driver), "Output появился при email без @"
        print("Negative test: email without @ passed")

    @pytest.mark.negative
    def test_negative_empty_form(self, driver, wait):
        click_submit(driver, wait)

        assert not is_output_visible(driver), "Output появился при отправке пустой формы"
        print("Negative test: empty form passed")

    @pytest.mark.negative
    def test_negative_email_too_long(self, driver, wait):
        long_local = "a" * 150
        long_domain = "b" * 100
        long_email = f"{long_local}@{long_domain}.com"

        print(f"Длина email: {len(long_email)} символов")

        fill_form(driver, "Макс Денисов", long_email, "Адрес 1", "Адрес 2")
        click_submit(driver, wait)

        assert not is_output_visible(driver), f"Output появился при слишком длинном email ({len(long_email)} символов)"
        print("Negative test: too long email passed")

    @pytest.mark.security
    @pytest.mark.parametrize("payload", SQL_PAYLOADS)
    def test_security_sql_injection(self, driver, wait, payload):
        fill_form(driver, payload, "den.maximov@mail.ru", payload, payload)
        click_submit(driver, wait)

        page_source = driver.page_source.lower()
        assert "sql" not in page_source and "error" not in page_source, f"SQL-инъекция вызвала ошибку: {payload[:20]}..."

        print(f"SQL-инъекция безопасна: {payload[:20]}...")

    @pytest.mark.security
    @pytest.mark.parametrize("payload", XSS_PAYLOADS)
    def test_security_xss_injection(self, driver, wait, payload):
        fill_form(driver, payload, "den.maximov@mail.ru", payload, payload)
        click_submit(driver, wait)

        page_source = driver.page_source
        assert "alert" not in page_source.lower() or "&lt;" in page_source, f"XSS-инъекция не экранирована: {payload[:20]}..."

        print(f"XSS-инъекция безопасна: {payload[:30]}...")


if __name__ == "__main__":
    pytest.main(["-v", __file__])
