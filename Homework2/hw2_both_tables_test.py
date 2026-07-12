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
def tables(driver):
    driver.get("https://the-internet.herokuapp.com/tables")
    table1_locator = (By.ID, "table1")
    table2_locator = (By.ID, "table2")
    return [TableElement(driver, table1_locator), TableElement(driver, table2_locator)]


class TestValidationBothTables:

    def test_both_tables_first_row_due_action(self, tables):
        table1 = tables[0]
        headers_1 = table1.get_headers()
        first_row_1 = table1.get_row_data(0)
        due_value_1 = table1.get_cell_value(row_index=2, column_index=3)

        table2 = tables[1]
        headers_2 = table2.get_headers()
        first_row_2 = table2.get_row_data(0)
        action_value_2 = table2.get_cell_value(row_index=3, column_index=5)

        print("Данные таблицы 1")
        print("Заголовки таблицы:", headers_1)
        print("Первая строка данных:", first_row_1)
        print(f"Значение в строке 1, колонке 'Due': {due_value_1}")

        print("Данные таблицы 2")
        print("Заголовки таблицы:", headers_2)
        print("Первая строка данных:", first_row_2)
        print(f"Значение в строке 1, колонке 'Due': {action_value_2}")

        assert "Last Name" in headers_1, "Заголовок 'Last Name' в таблице 1 не найден"
        assert "Smith" in first_row_1, "Фамилия 'Smith' в таблице 1 должна быть в первой строке"
        assert due_value_1 == "$100.00", f"Ожидалось $100.00, но  в таблице 1 получено {due_value_1}"

        assert "First Name" in headers_2, "Заголовок 'Last Name' в таблице 2 не найден"
        assert "John" in first_row_2, "Имя 'John' в таблице 2 должно быть в первой строке"
        assert action_value_2 == "edit delete", f"Ожидалось edit delete, но  в таблице 1 получено {action_value_2}"

        print("\n✅ Тест №1 успешно пройден!")

    def test_both_tables_second_row_and_website(self, tables):
        table1 = tables[0]
        headers_1 = table1.get_headers()
        second_row_1 = table1.get_row_data(1)
        website_value_1 = table1.get_cell_value(row_index=3, column_index=4)

        table2 = tables[1]
        headers_2 = table2.get_headers()
        second_row_2 = table2.get_row_data(1)
        website_value_2 = table2.get_cell_value(row_index=1, column_index=4)

        print("Данные таблицы 1")
        print("Заголовки таблицы:", headers_1)
        print("Вторая строка данных:", second_row_1)
        print(f"Значение в строке 2, колонке 'Web Site': {website_value_1}")

        print("Данные таблицы 2")
        print("Заголовки таблицы:", headers_2)
        print("Вторая строка данных:", second_row_2)
        print(f"Значение в строке 3, колонке 'Web Site': {website_value_2}")

        assert "First Name" in headers_1, "Заголовок 'Last Name' в таблице 1 не найден"
        assert "Frank" in second_row_1, "Имя 'Frank' в таблице 1 должно быть во второй строке"
        assert website_value_1 == "http://www.timconway.com", f"Ожидалось http://www.timconway.com, но в таблице 1 получено {website_value_1}"

        assert "Email" in headers_2, "Заголовок 'Email' в таблице 2 не найден"
        assert "fbach@yahoo.com" in second_row_2, "Email 'fbach@yahoo.com' в таблице 2 должно быть во второй строке"
        assert website_value_2 == "http://www.frank.com", f"Ожидалось http://www.frank.com, но в таблице 2 получено {website_value_2}"

        print("\n✅ Тест №2 успешно пройден!")

    def test_both_tables_third_row_action_due(self, tables):
        table1 = tables[0]
        headers_1 = table1.get_headers()
        third_row_1 = table1.get_row_data(2)
        action_value_1 = table1.get_cell_value(row_index=0, column_index=5)

        table2 = tables[1]
        headers_2 = table2.get_headers()
        third_row_2 = table2.get_row_data(2)
        due_value_2 = table2.get_cell_value(row_index=1, column_index=3)

        print("Данные таблицы 1")
        print("Заголовки таблицы:", headers_1)
        print("Третья строка данных:", third_row_1)
        print(f"Значение в строке 1, колонке 'Action': {action_value_1}")

        print("Данные таблицы 2")
        print("Заголовки таблицы:", headers_2)
        print("Третья строка данных:", third_row_2)
        print(f"Значение в строке 2, колонке 'Due': {due_value_2}")

        assert "Email" in headers_1, "Заголовок 'Email' в таблице 1 не найден"
        assert "jdoe@hotmail.com" in third_row_1, "Email 'jdoe@hotmail.com' в таблице 1 должен быть в третьей строке"
        assert action_value_1 == "edit delete", f"Ожидалось edit delete, но в таблице 1 получено {action_value_1}"

        assert "Last Name" in headers_2, "Заголовок 'Last Name' в таблице 2 не найден"
        assert "Doe" in third_row_2, "Email 'Doe' в таблице 2 должен быть в третьей строке"
        assert due_value_2 == "$51.00", f"Ожидалось $51.00, но в таблице 2 получено {due_value_2}"

        print("\n✅ Тест №3 успешно пройден!")

    def test_both_tables_fourth_row_lastname_email(self, tables):
        table1 = tables[0]
        headers_1 = table1.get_headers()
        fourth_row_1 = table1.get_row_data(3)
        lastname_value_1 = table1.get_cell_value(row_index=1, column_index=0)

        table2 = tables[1]
        headers_2 = table2.get_headers()
        fourth_row_2 = table2.get_row_data(3)
        email_value_2 = table2.get_cell_value(row_index=0, column_index=2)

        print("Данные таблицы 1")
        print("Заголовки таблицы:", headers_1)
        print("Четвертая строка данных:", fourth_row_1)
        print(f"Значение в строке 2, колонке 'Last Name': {lastname_value_1}")

        print("Данные таблицы 2")
        print("Заголовки таблицы:", headers_2)
        print("Четвертая строка данных:", fourth_row_2)
        print(f"Значение в строке 1, колонке 'Email': {email_value_2}")

        assert "Due" in headers_1, "Заголовок 'Due' в таблице 1 не найден"
        assert "$50.00" in fourth_row_1, "Due '$50.00' в таблице 1 должен быть в четвертой строке"
        assert lastname_value_1 == "Bach", f"Ожидалось Bach, но в таблице 1 получено {lastname_value_1}"

        assert "Web Site" in headers_2, "Заголовок 'Email' в таблице 2 не найден"
        assert "http://www.timconway.com" in fourth_row_2, "Due 'http://www.timconway.com' в таблице 2 должен быть в четвертой строке"
        assert email_value_2 == "jsmith@gmail.com", f"Ожидалось jsmith@gmail.com, но в таблице 2 получено {email_value_2}"

        print("\n✅ Тест №4 успешно пройден!")

    def test_both_tables_negative_header(self, tables):
        table1 = tables[0]
        headers_1 = table1.get_headers()
        fourth_row_1 = table1.get_row_data(3)
        due_value_1 = table1.get_cell_value(row_index=1, column_index=0)

        table2 = tables[1]
        headers_2 = table2.get_headers()
        fourth_row_2 = table2.get_row_data(3)
        email_value_2 = table2.get_cell_value(row_index=0, column_index=2)

        print("Данные таблицы 1")
        print("Заголовки таблицы:", headers_1)
        print("Четвертая строка данных:", fourth_row_1)
        print(f"Значение в строке 2, колонке 'Last Name': {due_value_1}")

        print("Данные таблицы 2")
        print("Заголовки таблицы:", headers_2)
        print("Четвертая строка данных:", fourth_row_2)
        print(f"Значение в строке 1, колонке 'Email': {email_value_2}")

        assert "Due" in headers_1, "Заголовок 'Due' в таблице 1 не найден"
        assert "$50.00" in fourth_row_1, "Due '$50.00' в таблице 1 должен быть в четвертой строке"
        assert due_value_1 == "Bach", f"Ожидалось Bach, но в таблице 1 получено {due_value_1}"

        assert "Hehe" not in headers_2, "Заголовок 'Hehe' в таблице 2 найден"
        assert "http://www.timconway.com" in fourth_row_2, "Due 'http://www.timconway.com' в таблице 2 должен быть в четвертой строке"
        assert email_value_2 == "jsmith@gmail.com", f"Ожидалось jsmith@gmail.com, но в таблице 2 получено {email_value_2}"

        print("\n✅ Тест №5 успешно пройден!")
