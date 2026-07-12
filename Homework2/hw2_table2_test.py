import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class TableElement:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.table = driver.find_element(*locator)

    def get_headers(self) -> list[str]:
        header_elements = self.table.find_elements(By.CSS_SELECTOR, "thead th")
        return [header.text for header in header_elements]

    def get_row_data(self, row_index: int) -> list[str]:
        rows = self.table.find_elements(By.CSS_SELECTOR, "tbody tr")
        cells = rows[row_index].find_elements(By.TAG_NAME, "td")
        return [cell.text for cell in cells]

    def get_cell_value(self, row_index: int, column_index: int) -> str:
        rows = self.table.find_elements(By.CSS_SELECTOR, "tbody tr")
        cells = rows[row_index].find_elements(By.TAG_NAME, "td")
        return cells[column_index].text

    def get_row_count(self):
        rows = self.table.find_elements(By.CSS_SELECTOR, "tbody tr")
        return len(rows)


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def table2(driver):
    driver.get("https://the-internet.herokuapp.com/tables")
    table2_locator = (By.ID, "table2")
    return TableElement(driver, table2_locator)


class TestValidationTable2:

    def test_table2_first_row_and_action(self, table2):
        headers = table2.get_headers()
        first_row = table2.get_row_data(0)
        action_value = table2.get_cell_value(row_index=3, column_index=5)

        print("Заголовки таблицы:", headers)
        print("Первая строка данных:", first_row)
        print(f"Значение в строке 4, колонке 'Action': {action_value}")

        assert "First Name" in headers, "Заголовок 'Last Name' не найден"
        assert "John" in first_row, "Имя 'John' должно быть в первой строке"
        assert action_value == "edit delete", f"Ожидалось edit delete, но получено {action_value}"

        print("\n✅ Тест №1 успешно пройден!")

    def test_table2_second_row_and_website(self, table2):
        headers = table2.get_headers()
        second_row = table2.get_row_data(1)
        website_value = table2.get_cell_value(row_index=1, column_index=4)

        print("Заголовки таблицы:", headers)
        print("Вторая строка данных:", second_row)
        print(f"Значение в строке 3, колонке 'Web Site': {website_value}")

        assert "Email" in headers, "Заголовок 'Email' не найден"
        assert "fbach@yahoo.com" in second_row, "Email 'fbach@yahoo.com' должно быть во второй строке"
        assert website_value == "http://www.frank.com", f"Ожидалось http://www.frank.com, но получено {website_value}"

        print("\n✅ Тест №2 успешно пройден!")

    def test_table2_third_row_and_due(self, table2):
        headers = table2.get_headers()
        third_row = table2.get_row_data(2)
        due_value = table2.get_cell_value(row_index=1, column_index=3)

        print("Заголовки таблицы:", headers)
        print("Третья строка данных:", third_row)
        print(f"Значение в строке 2, колонке 'Due': {due_value}")

        assert "Last Name" in headers, "Заголовок 'Last Name' не найден"
        assert "Doe" in third_row, "Email 'Doe' должен быть в третьей строке"
        assert due_value == "$51.00", f"Ожидалось $51.00, но получено {due_value}"

        print("\n✅ Тест №3 успешно пройден!")

    def test_table2_fourth_row_and_email(self, table2):
        headers = table2.get_headers()
        fourth_row = table2.get_row_data(3)
        email_value = table2.get_cell_value(row_index=0, column_index=2)

        print("Заголовки таблицы:", headers)
        print("Четвертая строка данных:", fourth_row)
        print(f"Значение в строке 1, колонке 'Email': {email_value}")

        assert "Web Site" in headers, "Заголовок 'Email' не найден"
        assert "http://www.timconway.com" in fourth_row, "Due 'http://www.timconway.com' должен быть в четвертой строке"
        assert email_value == "jsmith@gmail.com", f"Ожидалось jsmith@gmail.com, но получено {email_value}"

        print("\n✅ Тест №4 успешно пройден!")

    def test_negative_header(self, table2):
        headers = table2.get_headers()
        fourth_row = table2.get_row_data(3)
        lastname_value = table2.get_cell_value(row_index=1, column_index=0)

        print("Заголовки таблицы:", headers)
        print("Четвертая строка данных:", fourth_row)
        print(f"Значение в строке 2, колонке 'Last Name': {lastname_value}")

        assert "Hehe" not in headers, "Заголовок 'Hehe' найден"
        assert "$50.00" in fourth_row, "Due '$50.00' должен быть в четвертой строке"
        assert lastname_value == "Bach", f"Ожидалось Bach, но получено {lastname_value}"

        print("\n✅ Тест №6 успешно пройден!")

    def test_negative_value_in_row(self, table2):
        headers = table2.get_headers()
        fourth_row = table2.get_row_data(3)
        lastname_value = table2.get_cell_value(row_index=1, column_index=0)

        print("Заголовки таблицы:", headers)
        print("Четвертая строка данных:", fourth_row)
        print(f"Значение в строке 2, колонке 'Last Name': {lastname_value}")

        assert "Due" in headers, "Заголовок 'Due' не найден"
        assert "$70.00" not in fourth_row, "Due '$70.00' не должен быть в четвертой строке"
        assert lastname_value == "Bach", f"Ожидалось Bach, но получено {lastname_value}"

        print("\n✅ Тест №7 успешно пройден!")

    def test_negative_cell_value(self, table2):
        headers = table2.get_headers()
        first_row = table2.get_row_data(0)
        website_value = table2.get_cell_value(row_index=2, column_index=3)

        print("Заголовки таблицы:", headers)
        print("Первая строка данных:", first_row)
        print(f"Значение в строке 3, колонке 'Website': {website_value}")

        assert "Last Name" in headers, "Заголовок 'Last Name' не найден"
        assert "Smith" in first_row, "Фамилия 'Smith' должна быть в первой строке"
        assert not website_value == "http://www.jdoe.com", f"Вместо ожидаемого значения получено {website_value}"

        print("\n✅ Тест №8 успешно пройден!")
