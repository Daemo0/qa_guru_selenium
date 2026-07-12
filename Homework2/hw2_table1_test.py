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
    driver.implicitly_wait(5)

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def table1(driver):
    driver.get("https://the-internet.herokuapp.com/tables")
    table1_locator = (By.ID, "table1")
    return TableElement(driver, table1_locator)


class TestValidationTable1:

    def test_table1_first_row_and_due(self, table1):
        headers = table1.get_headers()
        first_row = table1.get_row_data(0)
        due_value = table1.get_cell_value(row_index=2, column_index=3)

        print("Заголовки таблицы:", headers)
        print("Первая строка данных:", first_row)
        print(f"Значение в строке 3, колонке 'Due': {due_value}")

        assert "Last Name" in headers, "Заголовок 'Last Name' не найден"
        assert "Smith" in first_row, "Фамилия 'Smith' должна быть в первой строке"
        assert due_value == "$100.00", f"Ожидалось $100.00, но получено {due_value}"

        print("\n✅ Тест №1 успешно пройден!")

    def test_table1_second_row_and_website(self, table1):
        headers = table1.get_headers()
        second_row = table1.get_row_data(1)
        website_value = table1.get_cell_value(row_index=3, column_index=4)

        print("Заголовки таблицы:", headers)
        print("Вторая строка данных:", second_row)
        print(f"Значение в строке 4, колонке 'Web Site': {website_value}")

        assert "First Name" in headers, "Заголовок 'Last Name' не найден"
        assert "Frank" in second_row, "Имя 'Frank' должно быть во второй строке"
        assert website_value == "http://www.timconway.com", f"Ожидалось http://www.timconway.com, но получено {website_value}"

        print("\n✅ Тест №2 успешно пройден!")

    def test_table1_third_row_and_action(self, table1):
        headers = table1.get_headers()
        third_row = table1.get_row_data(2)
        action_value = table1.get_cell_value(row_index=0, column_index=5)

        print("Заголовки таблицы:", headers)
        print("Третья строка данных:", third_row)
        print(f"Значение в строке 1, колонке 'Web Site': {action_value}")

        assert "Email" in headers, "Заголовок 'Email' не найден"
        assert "jdoe@hotmail.com" in third_row, "Email 'jdoe@hotmail.com' должен быть в третьей строке"
        assert action_value == "edit delete", f"Ожидалось edit delete, но получено {action_value}"

        print("\n✅ Тест №3 успешно пройден!")

    def test_table1_fourth_row_and_lastname(self, table1):
        headers = table1.get_headers()
        fourth_row = table1.get_row_data(3)
        lastname_value = table1.get_cell_value(row_index=1, column_index=0)

        print("Заголовки таблицы:", headers)
        print("Четвертая строка данных:", fourth_row)
        print(f"Значение в строке 2, колонке 'Last Name': {lastname_value}")

        assert "Due" in headers, "Заголовок 'Email' не найден"
        assert "$50.00" in fourth_row, "Due '$50.00' должен быть в четвертой строке"
        assert lastname_value == "Bach", f"Ожидалось Bach, но получено {lastname_value}"

        print("\n✅ Тест №4 успешно пройден!")

    def test_negative_header(self, table1):
        headers = table1.get_headers()
        fourth_row = table1.get_row_data(3)
        lastname_value = table1.get_cell_value(row_index=1, column_index=0)

        print("Заголовки таблицы:", headers)
        print("Четвертая строка данных:", fourth_row)
        print(f"Значение в строке 2, колонке 'Last Name': {lastname_value}")

        assert "Hehe" not in headers, "Заголовок 'Hehe' найден"
        assert "$50.00" in fourth_row, "Due '$50.00' должен быть в четвертой строке"
        assert lastname_value == "Bach", f"Ожидалось Bach, но получено {lastname_value}"

        print("\n✅ Тест №6 успешно пройден!")

    def test_negative_value_in_row(self, table1):
        headers = table1.get_headers()
        fourth_row = table1.get_row_data(3)
        lastname_value = table1.get_cell_value(row_index=1, column_index=0)

        print("Заголовки таблицы:", headers)
        print("Четвертая строка данных:", fourth_row)
        print(f"Значение в строке 2, колонке 'Last Name': {lastname_value}")

        assert "Due" in headers, "Заголовок 'Due' не найден"
        assert "$70.00" not in fourth_row, "Due '$70.00' не должен быть в четвертой строке"
        assert lastname_value == "Bach", f"Ожидалось Bach, но получено {lastname_value}"

        print("\n✅ Тест №7 успешно пройден!")

    def test_negative_cell_value(self, table1):
        headers = table1.get_headers()
        first_row = table1.get_row_data(0)
        website_value = table1.get_cell_value(row_index=2, column_index=3)

        print("Заголовки таблицы:", headers)
        print("Первая строка данных:", first_row)
        print(f"Значение в строке 3, колонке 'Website': {website_value}")

        assert "Last Name" in headers, "Заголовок 'Last Name' не найден"
        assert "Smith" in first_row, "Фамилия 'Smith' должна быть в первой строке"
        assert not website_value == "http://www.jdoe.com", f"Вместо ожидаемого значения получено {website_value}"

        print("\n✅ Тест №8 успешно пройден!")
