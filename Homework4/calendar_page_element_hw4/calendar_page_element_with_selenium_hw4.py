from typing import Tuple
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calendar:
    YEAR_OF_BIRTH_SELECT = (By.CSS_SELECTOR, ".react-datepicker__year-select")
    MONTH_OF_BIRTH_SELECT = (By.CSS_SELECTOR, ".react-datepicker__month-select")
    BANNER_TEXT = (By.XPATH, "//*[contains(text(), 'Level up your automation')]")
    CLOSE_BANNER_BTN = (By.CSS_SELECTOR, "#fixedban > div > div > button")

    def __init__(self, driver, input_field_element):
        self.driver = driver
        self.input_field = input_field_element
        self.wait = WebDriverWait(driver, 10)

    def _wait_and_click(self, locator) -> None:
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def close_banner_if_present(self) -> None:
            self.wait.until(
                EC.visibility_of_element_located(self.BANNER_TEXT),
            )
            self._wait_and_click(self.CLOSE_BANNER_BTN)


    def select_date(self, date: Tuple[str, str, str]):
        day, month, year = date
        close_banner_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#fixedban > div > div > button"))
        )
        close_banner_btn.click()
        self.input_field.click()
        Select(self.driver.find_element(*self.YEAR_OF_BIRTH_SELECT)).select_by_value(year)
        Select(self.driver.find_element(*self.MONTH_OF_BIRTH_SELECT)).select_by_value(month)
        self.driver.find_element(By.CSS_SELECTOR, f'.react-datepicker__day[data-day="{day}"]').click()


class AutomationPracticeFormPage:
    CALENDAR_INPUT = (By.ID, "dateOfBirthInput")
    URL = "https://qa-guru.github.io/one-page-form/automation-practice-form.html"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.open()
        input_field = self.wait.until(EC.presence_of_element_located(self.CALENDAR_INPUT))
        self.birthday_calendar = Calendar(self.driver, input_field)

    def open(self) -> None:
        self.driver.get(self.URL)
        self.driver.maximize_window()


class CalendarTestSuite:
    @staticmethod
    def test_select_birthday_date():
        driver = webdriver.Chrome()
        try:
            page = AutomationPracticeFormPage(driver)
            page.birthday_calendar.select_date(("15", "6", "2000"))
            input_field = page.birthday_calendar.input_field
            expected_value = "15 Jul 2000"
            actual_value = input_field.get_attribute("value")
            assert actual_value == expected_value, f"Expected '{expected_value}', got '{actual_value}'"
            print('Проверка прошла успешно!')
        finally:
            driver.quit()


if __name__ == "__main__":
    test_suite = CalendarTestSuite()
    test_suite.test_select_birthday_date()
